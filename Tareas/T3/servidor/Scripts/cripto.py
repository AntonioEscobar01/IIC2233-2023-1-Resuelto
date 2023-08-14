import random
import json
import os

# Servidor


def serializar(mensaje: object) -> bytearray:
    string_json = json.dumps(mensaje.__dict__)
    bytes_json = string_json.encode('utf-8')
    return bytearray(bytes_json)


def encriptar(msg: bytearray, ID) -> bytearray:
    msg_encriptar = msg.copy()
    with open(os.path.join('parametros.json')) as archivo:
        parametros = json.load(archivo)
    PONDERADOR_ENCRIPTACION = parametros["PONDERADOR_ENCRIPTACION"]
    random.seed(ID)
    n = random.randint(1, len(msg_encriptar))
    numero_mover = n * PONDERADOR_ENCRIPTACION
    for _ in range(numero_mover):
        ultimo = msg_encriptar.pop(len(msg_encriptar)-1)
        msg_encriptar.insert(0, ultimo)
    byte_aux = msg_encriptar[n]
    msg_encriptar[n] = msg_encriptar[0]
    msg_encriptar[0] = byte_aux
    return msg_encriptar


def codificar(msg_sin_copiar: bytearray) -> bytearray:
    msg = msg_sin_copiar.copy()
    largo_codificado = len(msg).to_bytes(4, byteorder="little")
    array_codificado = bytearray(largo_codificado)
    for index in range(0, len(msg) // 128):
        numero_chunk = (index).to_bytes(4, byteorder="big")
        array_codificado.extend(numero_chunk)
        chunk = msg[index * 128: index * 128 + 128]
        array_codificado.extend(chunk)
    resto = msg[len(msg) - (len(msg) % 128):]
    while len(resto) < 128:
        resto.extend(bytes([0]))
    array_codificado.extend(resto)
    return array_codificado


def decodificar(msg_sin_copiar: bytearray) -> bytearray:
    msg = msg_sin_copiar.copy()
    array_decodificado = bytearray()
    largo_mensaje = int.from_bytes(msg[:4], byteorder='little')
    mensaje_sin_largo = msg[4:]
    for index in range(0, largo_mensaje // 128):
        inicio = index * 128 + (index + 1) * 4
        chunk = mensaje_sin_largo[inicio:inicio + 128]
        array_decodificado.extend(chunk)
    resto = mensaje_sin_largo[len(mensaje_sin_largo) - 128:]
    array_decodificado.extend(resto)
    return array_decodificado[:largo_mensaje]


def desencriptar(msg: bytearray, ID) -> bytearray:
    msg_desencriptar = msg.copy()
    with open(os.path.join('parametros.json')) as archivo:
        parametros = json.load(archivo)
    PONDERADOR_ENCRIPTACION = parametros["PONDERADOR_ENCRIPTACION"]
    random.seed(ID)
    n = random.randint(1, len(msg_desencriptar))
    numero_mover = n * PONDERADOR_ENCRIPTACION
    byte_aux = msg_desencriptar[0]
    msg_desencriptar[0] = msg_desencriptar[n]
    msg_desencriptar[n] = byte_aux
    for _ in range(numero_mover):
        primero = msg_desencriptar.pop(0)
        msg_desencriptar.append(primero)
    return msg_desencriptar


def deserializar(array: bytearray):
    return json.loads(array.decode('utf-8'))


if __name__ == "__main__":

    # Testear encriptar
    ID = 1001
    random.seed(ID)
    msg_original = bytearray(b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x00\x01\x02\x03\x04\x05')
    msg_esperado = bytearray(b'\x01\x04\x05\x06\x07\x08\x09\x00\x01\x02\x03\x04\x05\x03\x02')

    msg_encriptado = encriptar(msg_original, ID)
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
        print(msg_encriptado)
        print(msg_esperado)
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")

# Testear desencriptar
    msg_desencriptado = desencriptar(msg_esperado, ID)
    if msg_desencriptado != msg_original:
        print("[ERROR] Mensaje descencriptado erroneamente")
        print(msg_desencriptado)
        print(msg_original)
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")
