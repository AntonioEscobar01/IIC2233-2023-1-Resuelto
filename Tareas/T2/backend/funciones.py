from PyQt5.QtGui import QPixmap
from random import uniform
import parametros as p
import os


def leer_mapa(mapa: str) -> list:
    if mapa.endswith('.txt'):
        ruta = os.path.join('frontend', 'assets', 'mapas', mapa)
        with open(ruta, 'r') as archivo_cargar:
            lineas = archivo_cargar.readlines()
    else:
        lineas = mapa.split('\n')
    lista_lineas = [linea.strip('\n') for linea in lineas]
    mapa = []
    for linea in lista_lineas:
        fila = []
        for letra in linea:
            fila.append(letra)
        mapa.append(fila)

    return mapa


def juntar_mapa(mapa: list) -> str:
    mapa_string = str()
    for fila in mapa:
        fila_actual = ''
        for caracter in fila:
            fila_actual += caracter
        fila_actual += '\n'
        mapa_string += fila_actual
    return mapa_string[:len(mapa_string)-1]


def cargar_pixmaps_fantasmas(ruta) -> list:
    lista_fantasma = list()
    for i in range(3):
        pixmap = QPixmap(ruta[i])
        lista_fantasma.append(pixmap)
    return lista_fantasma


def transformar_segundos_string(segundos: int) -> str:
    minutos = segundos // 60
    segundos = segundos % 60
    return f'{minutos:02}:{segundos:02}'


def calcular_puntuacion(tiempo_restante: int, vidas_restantes: int) -> str:
    vidas_ocupadas = (p.CANTIDAD_VIDAS - vidas_restantes)
    puntuacion = (tiempo_restante * p.MULTIPLICADOR_PUNTAJE)
    if vidas_ocupadas == 0:
        return str(puntuacion)
    else:
        return str(puntuacion / vidas_ocupadas)


def calcular_tiempo_fantasmas() -> int:
    ponderador = uniform(float(p.MIN_VELOCIDAD), float(p.MAX_VELOCIDAD))
    tiempo_movimiento = 1 / ponderador
    return int(tiempo_movimiento * 1000)

# Para calcular el tiempo, multiplicamos por mil para pasar de seg a miliseg
# y transformamos a int porque los qtimers solo aceptan intervalos en ints
