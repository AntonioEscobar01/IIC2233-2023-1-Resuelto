from Scripts.cripto import (serializar, encriptar, codificar,
                            decodificar, desencriptar, deserializar)
from Entidades import Mensaje, Cliente
import socket
import threading
import sys
import os
import json


class Servidor:
    id_clientes = 0

    def __init__(self, port: int, host: str):
        self.chunk_size = 2**12
        self.host = host
        self.port = port
        self.sockets = {}
        self.clientes = {}
        with open(os.path.join('parametros.json')) as archivo:
            self.parametros = json.load(archivo)
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_listen()
        self.accept_connections()

    def bind_listen(self) -> None:
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen(250)
        print('-' * 100)
        print(f'''{'*** Servidor Conectado ***'.center(100)}''')
        info = f'Servidor escuchando en {self.host} : {self.port}'
        print(f'{info.center(100)}')
        print('-' * 100)
        print(f'''{'CLIENTE'.center(32)}|{
            'EVENTO'.center(32)}|{'DETALLES'.center(34)}''')
        print('-' * 100)

    def accept_connections(self) -> None:
        thread = threading.Thread(
            target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self) -> None:
        while True:
            if self.id_clientes < self.parametros["NUMERO_JUGADORES"]:
                socket_cliente, address = self.socket_server.accept()
                self.sockets[socket_cliente] = address
                self.id_clientes += 1
                cliente = Cliente(self.id_clientes,
                                  self.parametros[f'id_{self.id_clientes}'])
                self.clientes[socket_cliente] = cliente
                listening_client_thread = threading.Thread(
                    target=self.listen_client_thread,
                    args=(socket_cliente, ),
                    daemon=True)
                listening_client_thread.start()
                mensaje_conectar = Mensaje('conectar',
                                           self.parametros[f'id_{self.id_clientes}'],
                                           True, self.id_clientes)
                self.enviar_mensaje(mensaje_conectar, socket_cliente, 'ID')
                print(f'''{(cliente.name).center(32)}|{
                    'Conectado'.center(32)}|{
                        'Se ha conectado un cliente'.center(34)}''')
            else:
                socket_cliente, address = self.socket_server.accept()
                self.sockets[socket_cliente] = address
                cliente = Cliente(0, 'ID')
                self.clientes[socket_cliente] = cliente
                listening_client_thread = threading.Thread(
                    target=self.listen_client_thread,
                    args=(socket_cliente, ),
                    daemon=True)
                listening_client_thread.start()
                mensaje_conectar = Mensaje('lleno', '', True, self.id_clientes)
                self.enviar_mensaje(mensaje_conectar, socket_cliente, 'ID')

    def listen_client_thread(self, socket_cliente: socket) -> None:
        while True:
            try:
                bytes_mensaje = self.recibir_bytes(socket_cliente)
                mensaje_decodificado = decodificar(bytes_mensaje)
                desencriptado = desencriptar(mensaje_decodificado,
                                             self.clientes[socket_cliente].name)
                mensaje_final = deserializar(desencriptado)
                mensaje = Mensaje(**mensaje_final)
                self.manejar_mensaje(mensaje, socket_cliente)
            except ConnectionResetError:
                nombre = self.clientes[socket_cliente].name
                print(f'''{nombre.center(32)}|{'Desconectado'.center(32)}|{
                    '-'.center(34)}''')
                del self.sockets[socket_cliente]
                del self.clientes[socket_cliente]
                break

    def recibir_bytes(self, socket_cliente: socket) -> bytearray:
        bytes_leidos = bytearray()
        respuesta = socket_cliente.recv(self.chunk_size)
        bytes_leidos += respuesta
        return bytes_leidos

    def manejar_mensaje(self, mensaje: Mensaje, c_socket: socket) -> None:
        if mensaje.operacion == 'empezar':
            nombre = self.clientes[c_socket].name
            print(f'''{nombre.center(32)}|{
                'Accion'.center(32)}|{'Empezar'.center(34)}''')
            for socket_usuario, cliente in self.clientes.items():
                empezar = Mensaje('empezar', '', '', cliente.numero)
                self.enviar_mensaje(empezar, socket_usuario, cliente.name)

    def enviar_mensaje(self, mensaje: Mensaje,
                       socket_cliente: socket, nombre: str) -> None:
        mensaje_serializado = serializar(mensaje)
        mensaje_encriptado = encriptar(mensaje_serializado, nombre)
        mensaje_codificado = codificar(mensaje_encriptado)
        socket_cliente.sendall(mensaje_codificado)


if __name__ == '__main__':
    PORT = 3247 if len(sys.argv) < 2 else int(sys.argv[1])
    HOST = 'localhost' if len(sys.argv) < 3 else sys.argv[2]
    server = Servidor(PORT, HOST)
