from typing import List
import json
from errors import JsonError, SequenceError


def deserializar_diccionario(mensaje_codificado: bytearray) -> dict:
    try:
        mensaje_decodificado = mensaje_codificado.decode('utf-8')
        diccionario = json.loads(mensaje_decodificado)
        return diccionario
    except json.JSONDecodeError:
        raise JsonError()


def decodificar_largo(mensaje: bytearray) -> int:
    numero = int.from_bytes(mensaje[0:4], byteorder='big')
    return numero


def separar_msg_encriptado(mensaje: bytearray) -> List[bytearray]:
    m_bytes_secuencia = bytearray()
    m_reducido = bytearray()
    secuencia_codificada = bytearray()
    largo = decodificar_largo(mensaje)
    m_bytes_secuencia = mensaje[4: largo + 4]
    secuencia_codificada = mensaje[len(mensaje) - (2 * largo):]
    m_reducido = mensaje[largo + 4:len(mensaje) - (2 * largo)]

    return [m_bytes_secuencia, m_reducido, secuencia_codificada]


def decodificar_secuencia(secuencia_codificada: bytearray) -> List[int]:
    lista = list()
    for index in range(0, len(secuencia_codificada), 2):
        numero = int.from_bytes(secuencia_codificada[index: index+2], byteorder='big')
        lista.append(numero)
    return lista


def desencriptar(mensaje: bytearray) -> bytearray:
    mensaje_separado = separar_msg_encriptado(mensaje)
    secuencia = decodificar_secuencia(mensaje_separado[2])
    mensaje_desencriptado = mensaje_separado[1]
    mensaje_bytes = mensaje_separado[0]
    for index, numero in enumerate(secuencia):
        byte_insertar = mensaje_bytes[index]
        mensaje_desencriptado.insert(numero, byte_insertar)
    return mensaje_desencriptado


if __name__ == "__main__":
    mensaje = bytearray(b'\x00\x00\x00\x04"a}a{tm": 1\x00\x01\x00\x05\x00\n\x00\x03')
    desencriptado = desencriptar(mensaje)
    diccionario = deserializar_diccionario(desencriptado)
    print(diccionario)
