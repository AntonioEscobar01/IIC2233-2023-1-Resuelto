from typing import List
import json
from errors import JsonError, SequenceError


def serializar_diccionario(dictionary: dict) -> bytearray:
    try:
        string_json = json.dumps(dictionary)
        bytes_json = string_json.encode('utf-8')
        return bytearray(bytes_json)
    except TypeError:
        raise JsonError()


def verificar_secuencia(mensaje: bytearray, secuencia: List[int]) -> None:
    numero_mayor = max(secuencia)

    largo_mensaje = len(mensaje)
    largo_lista = len(secuencia)
    largo_set = len(set(secuencia))
    if numero_mayor < largo_mensaje and largo_set == largo_lista:
        return None
    else:
        raise SequenceError()


def codificar_secuencia(secuencia: List[int]) -> bytearray:
    array = bytearray()
    for numero in secuencia:
        numero_b = numero.to_bytes(2, byteorder="big")
        array.extend(numero_b)
    return array


def codificar_largo(largo: int) -> bytearray:
    largo_b = largo.to_bytes(4, byteorder="big")
    return bytearray(largo_b)


def separar_msg(mensaje: bytearray, secuencia: List[int]) -> List[bytearray]:
    m_bytes_secuencia = bytearray()
    m_reducido = bytearray()
    for index, item in enumerate(mensaje):
        if index not in secuencia:
            m_reducido.append(item)
    for index_2 in secuencia:
        m_bytes_secuencia.append(mensaje[index_2])

    return [m_bytes_secuencia, m_reducido]


def encriptar(mensaje: bytearray, secuencia: List[int]) -> bytearray:
    verificar_secuencia(mensaje, secuencia)

    m_bytes_secuencia, m_reducido = separar_msg(mensaje, secuencia)
    secuencia_codificada = codificar_secuencia(secuencia)

    return (
        codificar_largo(len(secuencia))
        + m_bytes_secuencia
        + m_reducido
        + secuencia_codificada
    )


if __name__ == "__main__":
    original = serializar_diccionario({"tama": 1})
    encriptado = encriptar(original, [1, 5, 10, 3])
    print(original)
    print(encriptado)
