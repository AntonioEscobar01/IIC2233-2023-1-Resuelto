from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPixmap
from backend.funciones import cargar_pixmaps_fantasmas

import parametros as p


class Roca(QObject):

    def __init__(self, x: int, y: int, fila: int, columna: int) -> None:
        super().__init__()

        self.x = x
        self.y = y
        self.fila = fila
        self.columna = columna


class Luigi(QObject):
    senal_actualizar_pixmap = pyqtSignal(list)
    senal_actualizar_label = pyqtSignal(int, int)
    senal_mover_label = pyqtSignal()

    def __init__(self, x: int, y: int, fila: int, columna: int) -> None:
        super().__init__()
        self.__x = x
        self.__y = y
        self.fila = fila
        self.columna = columna
        self.direcciones = {'up': (0, -36), 'down': (0, 36),
                            'left': (-39, 0), 'right': (39, 0)}
        self.crear_pixmaps()

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, p: int) -> None:
        if p < 500:
            self.__x = 500
        elif p > 810:
            self.__x = 810
        else:
            self.__x = p

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, p: int) -> None:
        if p < 49:
            self.__y = 49
        elif p > 515:
            self.__y = 515
        else:
            self.__y = p

    @property
    def centro_x(self) -> int:
        return self.x + 18

    @property
    def centro_y(self) -> int:
        return self.y + 19

    def crear_pixmaps(self):
        self.luigi_up = list()
        self.luigi_down = list()
        self.luigi_left = list()
        self.luigi_right = list()
        for i in range(3):
            pixmap_up = QPixmap(p.RUTA_LUIGI_UP[i])
            pixmap_down = QPixmap(p.RUTA_LUIGI_DOWN[i])
            pixmap_left = QPixmap(p.RUTA_LUIGI_LEFT[i])
            pixmap_right = QPixmap(p.RUTA_LUIGI_RIGHT[i])
            self.luigi_up.append(pixmap_up)
            self.luigi_down.append(pixmap_down)
            self.luigi_left.append(pixmap_left)
            self.luigi_right.append(pixmap_right)
        self.pixmap_direccion = {'up': self.luigi_up,
                                 'down': self.luigi_down,
                                 'left': self.luigi_left,
                                 'right': self.luigi_right}

    def mover_luigi(self, direccion):
        incremento = self.direcciones[direccion]
        self.senal_actualizar_pixmap.emit(self.pixmap_direccion[direccion])
        self.x += incremento[0]
        self.y += incremento[1]
        self.senal_actualizar_label.emit(self.x, self.y)
        self.senal_mover_label.emit()


class FantasmaH(QObject):
    def __init__(self, x: int, y: int, fila: int, columna: int) -> None:
        super().__init__()
        self.__x = x
        self.y = y
        self.__fila = fila
        self.columna = columna
        self.direc_actual = 'right'
        self.pixmap_r = cargar_pixmaps_fantasmas(p.RUTA_FHD)
        self.pixmap_l = cargar_pixmaps_fantasmas(p.RUTA_FHL)
        self.pix_actual = cargar_pixmaps_fantasmas(p.RUTA_FHD)

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, p: int) -> None:
        if p < 500:
            self.__x = 500
        elif p > 810:
            self.__x = 810
        else:
            self.__x = p

    @property
    def fila(self) -> int:
        return self.__fila

    @fila.setter
    def fila(self, p: int) -> None:
        if p < 0:
            self.__fila = 0
        elif p > 8:
            self.__fila = 8
        else:
            self.__fila = p


class FantasmaV(QObject):
    def __init__(self, x: int, y: int, fila: int, columna: int) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.fila = fila
        self.columna = columna
        self.direc_actual = 'down'
