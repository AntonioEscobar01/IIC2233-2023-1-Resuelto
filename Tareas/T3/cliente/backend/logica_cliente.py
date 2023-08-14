from Scripts.cripto import (serializar, encriptar, codificar,
                            decodificar, desencriptar, deserializar)
from PyQt5.QtCore import pyqtSignal, QObject
import threading
import socket


class Mensaje:

    def __init__(self, operacion=None, data=None,
                 estado=None, numero=None):
        self.operacion = operacion
        self.data = data
        self.estado = estado
        self.numero = numero

    def __repr__(self) -> str:
        return f"*Mensaje: status {self.estado}*"


class Cliente(QObject):

    senal_empezar = pyqtSignal()
    senal_agregar_nombre = pyqtSignal(tuple)
    senal_lleno = pyqtSignal()

    def __init__(self, port: int, host: str):
        super().__init__()
        self.conectado = False
        self.port = port
        self.host = host
        self.chunk_size = 2**12
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = 'ID'
        self.numero_jugador = int()
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            self.listen()

        except ConnectionError:
            print('Conexion terminada')
            self.socket_cliente.close()
            self.conectado = False
            exit()

    def salir(self) -> None:
        self.conectado = False
        self.socket_cliente.close()

    def enviar_mensaje(self, mensaje_enviar: Mensaje) -> None:
        mensaje_serializado = serializar(mensaje_enviar)
        mensaje_encriptado = encriptar(mensaje_serializado, self.name)
        mensaje_codificado = codificar(mensaje_encriptado)
        self.socket_cliente.sendall(mensaje_codificado)

    def listen(self):
        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

    def listen_thread(self):
        try:
            while self.conectado:
                data = self.socket_cliente.recv(self.chunk_size)
                mensaje_decodificado = decodificar(bytearray(data))
                mensaje_desencriptado = desencriptar(mensaje_decodificado,
                                                     self.name)
                mensaje_final = deserializar(mensaje_desencriptado)
                self.manejar_mensaje(mensaje_final)
        except ConnectionAbortedError:
            print('Conexion terminada')

    def manejar_mensaje(self, mensaje_dic):
        mensaje = Mensaje(**mensaje_dic)
        if mensaje.operacion == 'conectar':
            self.name = mensaje.data
            self.numero_jugador = mensaje.numero
            self.senal_agregar_nombre.emit((self.name, self.numero_jugador))
            mensaje_enviar = Mensaje('comunicar',
                                     f'recivi mi id {self.numero_jugador}',
                                     'activo', self.numero_jugador)
            self.enviar_mensaje(mensaje_enviar)
        elif mensaje.operacion == 'lleno':
            self.senal_lleno.emit()
            self.salir()
        elif mensaje.operacion == 'empezar':
            self.senal_empezar.emit()

    def comenzar(self):
        enviar = Mensaje('empezar', '', '', self.numero_jugador)
        self.enviar_mensaje(enviar)
