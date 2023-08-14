from PyQt5.QtCore import QObject, pyqtSignal
from backend.funciones import juntar_mapa
import parametros as p


class Constructor(QObject):
    senal_posicion_label = pyqtSignal(tuple, int)
    senal_casilla_ocupada = pyqtSignal()
    senal_empezar_juego = pyqtSignal(str, str)
    senal_cerrar_ventana = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()

        self.mapa = [['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-']]

        self.cantidad_luigi = p.CANTIDAD_LUIGI
        self.cantidad_ladrillo = p.MAXIMO_PARED
        self.cantidad_fuego = p.MAXIMO_FUEGO
        self.cantidad_FV = p.MAXIMO_FANTASMAS_VERTICAL
        self.cantidad_FH = p.MAXIMO_FANTASMAS_HORIZONTAL
        self.cantidad_estrella = p.CANTIDAD_ESTRELLA
        self.cantidad_rocas = p.MAXIMO_ROCA

        self.objetos = {
            'L': self.cantidad_luigi, 'P': self.cantidad_ladrillo,
            'F': self.cantidad_fuego, 'V': self.cantidad_FV,
            'H': self.cantidad_FH, 'S': self.cantidad_estrella,
            'R': self.cantidad_rocas}

    def calcular_posicion_label(self, x, y, etiqueta):
        posicion_real_x = 500
        posicion_real_y = 49
        while posicion_real_x + p.GRILLA_X <= x:
            posicion_real_x += p.GRILLA_X
        while posicion_real_y + p.GRILLA_Y <= y:
            posicion_real_y += p.GRILLA_Y
        posicion = (posicion_real_x, posicion_real_y)
        fila = (posicion_real_y - 49) // p.GRILLA_Y
        columna = (posicion_real_x - 500) // p.GRILLA_X
        if self.mapa[fila][columna] == '-':
            cantidad_objeto = self.objetos[etiqueta]
            if cantidad_objeto > 0:
                cantidad_objeto -= 1
                self.mapa[fila][columna] = etiqueta
                self.objetos[etiqueta] = cantidad_objeto
                self.senal_posicion_label.emit(posicion, cantidad_objeto)
        elif self.mapa[fila][columna] != '-':
            self.senal_casilla_ocupada.emit()

    def limpiar_tablero(self):
        for fila in range(p.LARGO_GRILLA - 2):
            for columna in range(p.ANCHO_GRILLA - 2):
                self.mapa[fila][columna] = '-'
        self.objetos['L'] = p.CANTIDAD_LUIGI
        self.objetos['P'] = p.MAXIMO_PARED
        self.objetos['F'] = p.MAXIMO_FUEGO
        self.objetos['V'] = p.MAXIMO_FANTASMAS_VERTICAL
        self.objetos['H'] = p.MAXIMO_FANTASMAS_HORIZONTAL
        self.objetos['S'] = p.CANTIDAD_ESTRELLA
        self.objetos['R'] = p.MAXIMO_ROCA

    def empezar(self, nombre_usuario):
        numero_luigi = self.objetos['L']
        numero_estrella = self.objetos['S']
        if numero_luigi == 0 and numero_estrella == 0:
            mapa_string = juntar_mapa(self.mapa)
            self.senal_empezar_juego.emit(mapa_string, nombre_usuario)
            self.senal_cerrar_ventana.emit()
