from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from backend.entidades import Luigi, Roca, FantasmaH, FantasmaV
from backend.funciones import (leer_mapa, transformar_segundos_string,
                               calcular_puntuacion, calcular_tiempo_fantasmas)
import parametros as p


class Juego(QObject):
    # definir señales
    senal_mostrar_ventana = pyqtSignal()
    senal_mostrar_luigi = pyqtSignal(int, int)
    senal_colocar_bloque = pyqtSignal(tuple)
    senal_actualizar_vidas = pyqtSignal(str)
    senal_borrar_labels = pyqtSignal()
    senal_levantar_luigi = pyqtSignal()
    senal_colocar_roca = pyqtSignal(tuple)
    senal_mover_roca = pyqtSignal(tuple)
    senal_pop_ganar = pyqtSignal(str, str)
    senal_pop_perder = pyqtSignal(str)
    senal_colocar_f = pyqtSignal(tuple)
    senal_actualizar_tiempo = pyqtSignal(str)
    senal_habilitar_teclas = pyqtSignal(bool)
    senal_mover_fantasma = pyqtSignal(tuple)
    senal_borrar_fantasma = pyqtSignal(tuple)
    senal_enviar_tiempo = pyqtSignal(int)

    def __init__(self) -> None:
        super().__init__()
        self.mapa = list()
        self.mapa_sin_editar = None
        self.lista_rocas = list()
        self.fantasmas_v = list()
        self.fantasmas_h = list()
        self.segundos_restantes = p.TIEMPO_CUENTA_REGRESIVA
        self.juego_pausado = False
        self.inf_activado = False
        self.kil_activado = False
        self.nombre_usuario = str()
        self.vidas = p.CANTIDAD_VIDAS
        self.direcciones = {'up': (-1, 0), 'down': (1, 0),
                            'left': (0, -1), 'right': (0, 1)}
        self.tiempo_fantasmas = calcular_tiempo_fantasmas()
        self.crear_luigi()
        self.timer_juego = QTimer(self)
        self.timer_juego.setInterval(1000)
        self.timer_juego.timeout.connect(self.disminuir_tiempo)
        self.timer_fantasmas = QTimer(self)
        self.timer_fantasmas.setInterval(self.tiempo_fantasmas)
        self.timer_fantasmas.timeout.connect(self.mover_fantasmas)

    def cargar_mapa(self, mapa_nuevo):
        if type(mapa_nuevo) is str:
            self.mapa = leer_mapa(mapa_nuevo)[:]
        elif type(mapa_nuevo) is list:
            self.mapa = mapa_nuevo[:]
        for fila in range(p.LARGO_GRILLA - 2):
            for columna in range(p.ANCHO_GRILLA - 2):
                caracter = self.mapa[fila][columna]
                x = p.INICIO_X + (columna * p.GRILLA_X)
                y = p.INICIO_Y + (fila * p.GRILLA_Y)
                if caracter in ['P', 'F', 'S']:
                    self.senal_colocar_bloque.emit((x, y, caracter))
                elif caracter == 'L':
                    self.luigi.x = x
                    self.luigi.y = y
                    self.luigi.fila = fila
                    self.luigi.columna = columna
                    self.senal_mostrar_luigi.emit(self.luigi.x, self.luigi.y)
                elif caracter == 'R':
                    roca = Roca(x, y, fila, columna)
                    self.lista_rocas.append(roca)
                    self.senal_colocar_roca.emit((roca, x, y))
                elif caracter == 'H':
                    fantasma_h = FantasmaH(x, y, fila, columna)
                    self.fantasmas_h.append(fantasma_h)
                    self.senal_colocar_f.emit(('H', fantasma_h, x, y))
                elif caracter == 'V':
                    fantasma_v = FantasmaV(x, y, fila, columna)
                    self.fantasmas_v.append(fantasma_v)
                    self.senal_colocar_f.emit(('V', fantasma_v, x, y))
        self.kil_activado = False
        self.senal_levantar_luigi.emit()
        self.timer_fantasmas.start()

    def crear_luigi(self) -> None:
        self.luigi = Luigi(0, 0, 0, 0)

    def empezar(self, mapa, nombre):
        self.mapa_sin_editar = mapa[:]
        self.nombre_usuario = nombre
        self.senal_mostrar_ventana.emit()
        self.cargar_mapa(mapa[:])
        tiempo_inicial = transformar_segundos_string(self.segundos_restantes)
        self.senal_actualizar_tiempo.emit(tiempo_inicial)
        self.senal_enviar_tiempo.emit(int(self.tiempo_fantasmas / 3))
        self.timer_juego.start()

    def revisar_colisiones_luigi(self, direccion):
        fila_actual = self.luigi.fila
        columna_actual = self.luigi.columna
        fila_nueva = fila_actual + self.direcciones[direccion][0]
        columna_nueva = columna_actual + self.direcciones[direccion][1]
        if fila_nueva < (p.LARGO_GRILLA - 2) and \
                columna_nueva < (p.ANCHO_GRILLA - 2) and \
                fila_nueva >= 0 and columna_nueva >= 0:
            caracter = self.mapa[fila_nueva][columna_nueva]
            if caracter == '-' or caracter == 'S':
                self.mapa[fila_actual][columna_actual] = '-'
                self.mapa[fila_nueva][columna_nueva] = 'L'
                self.luigi.fila = fila_nueva
                self.luigi.columna = columna_nueva
                self.luigi.mover_luigi(direccion)

            elif caracter in ['F', 'V', 'H']:
                self.revisar_vidas()
                self.senal_borrar_labels.emit()
                self.lista_rocas = []
                self.fantasmas_h = []
                self.fantasmas_v = []
                self.cargar_mapa(self.mapa_sin_editar)

            elif caracter == 'R':
                f_sub_siguiente = fila_nueva + self.direcciones[direccion][0]
                c_sub_siguiente = columna_nueva + self.direcciones[direccion][1]
                if f_sub_siguiente < (p.LARGO_GRILLA - 2) and \
                        c_sub_siguiente < (p.ANCHO_GRILLA - 2) and \
                        f_sub_siguiente >= 0 and c_sub_siguiente >= 0:
                    caracter_siguiente = self.mapa[f_sub_siguiente][c_sub_siguiente]
                    if caracter_siguiente == '-':
                        roca = self.buscar_roca(fila_nueva, columna_nueva)
                        self.mapa[fila_actual][columna_actual] = '-'
                        self.mapa[fila_nueva][columna_nueva] = 'L'
                        self.mapa[f_sub_siguiente][c_sub_siguiente] = 'R'
                        self.luigi.fila = fila_nueva
                        self.luigi.columna = columna_nueva
                        self.luigi.mover_luigi(direccion)
                        x_roca = p.INICIO_X + (c_sub_siguiente * p.GRILLA_X)
                        y_roca = p.INICIO_Y + (f_sub_siguiente * p.GRILLA_Y)
                        self.senal_mover_roca.emit((roca, x_roca, y_roca))
                        roca.fila = f_sub_siguiente
                        roca.columna = c_sub_siguiente
                        roca.x = x_roca
                        roca.y = y_roca

    def mover_fantasmas(self):
        for fantasma_h in self.fantasmas_h[:]:
            fila_actual = fantasma_h.fila
            columna_actual = fantasma_h.columna
            direccion = fantasma_h.direc_actual
            if direccion == 'right':
                if columna_actual + 1 == (p.ANCHO_GRILLA - 2):
                    fantasma_h.pix_actual = fantasma_h.pixmap_l
                    fantasma_h.direc_actual = 'left'
                elif self.mapa[fila_actual][columna_actual + 1] in ['P', 'R', 'S']:
                    fantasma_h.pix_actual = fantasma_h.pixmap_l
                    fantasma_h.direc_actual = 'left'
                elif self.mapa[fila_actual][columna_actual + 1] in ['-', 'H', 'V']:
                    self.mapa[fila_actual][columna_actual] = '-'
                    self.mapa[fila_actual][columna_actual + 1] = 'H'
                    fantasma_h.columna = columna_actual + 1
                    x = fantasma_h.x + p.GRILLA_X
                    y = fantasma_h.y
                    fantasma_h.x = x
                    self.senal_mover_fantasma.emit(('H', fantasma_h, x, y))
                elif self.mapa[fila_actual][columna_actual + 1] == 'L':
                    self.revisar_vidas()
                    self.senal_borrar_labels.emit()
                    self.lista_rocas = []
                    self.fantasmas_h = []
                    self.fantasmas_v = []
                    self.cargar_mapa(self.mapa_sin_editar)
                    break
                elif self.mapa[fila_actual][columna_actual + 1] == 'F':
                    self.mapa[fila_actual][columna_actual] = '-'
                    self.senal_borrar_fantasma.emit(('H', fantasma_h))
                    self.fantasmas_h.remove(fantasma_h)
            elif direccion == 'left':
                if columna_actual - 1 < 0:
                    fantasma_h.pix_actual = fantasma_h.pixmap_r
                    fantasma_h.direc_actual = 'right'
                elif self.mapa[fila_actual][columna_actual - 1] in ['P', 'R', 'S']:
                    fantasma_h.pix_actual = fantasma_h.pixmap_r
                    fantasma_h.direc_actual = 'right'
                elif self.mapa[fila_actual][columna_actual - 1] in ['-', 'H', 'V']:
                    self.mapa[fila_actual][columna_actual] = '-'
                    self.mapa[fila_actual][columna_actual - 1] = 'H'
                    fantasma_h.columna = columna_actual - 1
                    x = fantasma_h.x - p.GRILLA_X
                    y = fantasma_h.y
                    fantasma_h.x = x
                    self.senal_mover_fantasma.emit(('H', fantasma_h, x, y))
                elif self.mapa[fila_actual][columna_actual - 1] == 'L':
                    self.revisar_vidas()
                    self.senal_borrar_labels.emit()
                    self.lista_rocas = []
                    self.fantasmas_h = []
                    self.fantasmas_v = []
                    self.cargar_mapa(self.mapa_sin_editar)
                    break
                elif self.mapa[fila_actual][columna_actual - 1] == 'F':
                    self.mapa[fila_actual][columna_actual] = '-'
                    self.senal_borrar_fantasma.emit(('H', fantasma_h))
                    self.fantasmas_h.remove(fantasma_h)

        for fantasma_v in self.fantasmas_v[:]:
            fila_actual = fantasma_v.fila
            columna_actual = fantasma_v.columna
            direccion = fantasma_v.direc_actual
            if direccion == 'down':
                if fila_actual + 1 == (p.LARGO_GRILLA - 2):
                    fantasma_v.direc_actual = 'up'
                elif self.mapa[fila_actual + 1][columna_actual] in ['P', 'R', 'S']:
                    fantasma_v.direc_actual = 'up'
                elif self.mapa[fila_actual + 1][columna_actual] in ['-', 'H', 'V']:
                    self.mapa[fila_actual][columna_actual] = '-'
                    self.mapa[fila_actual + 1][columna_actual] = 'V'
                    fantasma_v.fila = fila_actual + 1
                    x = fantasma_v.x
                    y = fantasma_v.y + p.GRILLA_Y
                    fantasma_v.y = y
                    self.senal_mover_fantasma.emit(('V', fantasma_v, x, y))
                elif self.mapa[fila_actual + 1][columna_actual] == 'L':
                    self.revisar_vidas()
                    self.senal_borrar_labels.emit()
                    self.lista_rocas = []
                    self.fantasmas_h = []
                    self.fantasmas_v = []
                    self.cargar_mapa(self.mapa_sin_editar)
                    break
                elif self.mapa[fila_actual + 1][columna_actual] == 'F':
                    self.mapa[fila_actual][columna_actual] = '-'
                    self.senal_borrar_fantasma.emit(('V', fantasma_v))
                    self.fantasmas_v.remove(fantasma_v)

            elif direccion == 'up':
                if fila_actual - 1 < 0:
                    fantasma_v.direc_actual = 'down'
                elif self.mapa[fila_actual - 1][columna_actual] in ['P', 'R', 'S']:
                    fantasma_v.direc_actual = 'down'
                elif self.mapa[fila_actual - 1][columna_actual] in ['-', 'H', 'V']:
                    self.mapa[fila_actual][columna_actual] = '-'
                    self.mapa[fila_actual - 1][columna_actual] = 'V'
                    fantasma_v.fila = fila_actual - 1
                    x = fantasma_v.x
                    y = fantasma_v.y - p.GRILLA_Y
                    fantasma_v.y = y
                    self.senal_mover_fantasma.emit(('V', fantasma_v, x, y))
                elif self.mapa[fila_actual - 1][columna_actual] == 'L':
                    self.revisar_vidas()
                    self.senal_borrar_labels.emit()
                    self.lista_rocas = []
                    self.fantasmas_h = []
                    self.fantasmas_v = []
                    self.cargar_mapa(self.mapa_sin_editar)
                    break
                elif self.mapa[fila_actual - 1][columna_actual] == 'F':
                    self.mapa[fila_actual][columna_actual] = '-'
                    self.senal_borrar_fantasma.emit(('V', fantasma_v))
                    self.fantasmas_v.remove(fantasma_v)

    def buscar_roca(self, fila, columna):
        for roca in self.lista_rocas:
            if roca.fila == fila and roca.columna == columna:
                return roca

    def disminuir_tiempo(self):
        self.segundos_restantes -= 1
        tiempo_str = transformar_segundos_string(self.segundos_restantes)
        self.senal_actualizar_tiempo.emit(tiempo_str)
        if self.segundos_restantes == 0:
            self.timer_juego.stop()
            self.perder()

    def revisar_vidas(self):
        if self.inf_activado is False:
            self.vidas -= 1
            self.timer_fantasmas.stop()
            self.senal_actualizar_vidas.emit(str(self.vidas))
            if self.vidas == 0:
                self.timer_juego.stop()
                self.perder()

    def pausar_juego(self):
        if self.juego_pausado is False:
            self.juego_pausado = True
            self.senal_habilitar_teclas.emit(False)
            if self.inf_activado is False:
                self.timer_juego.stop()
            self.timer_fantasmas.stop()
        elif self.juego_pausado is True:
            self.juego_pausado = False
            self.senal_habilitar_teclas.emit(True)
            if self.inf_activado is False:
                self.timer_juego.start()
            self.timer_fantasmas.start()

    def cheatcode_inf(self):
        if self.inf_activado is False:
            self.inf_activado = True
            self.timer_juego.stop()
            self.senal_actualizar_vidas.emit(str('INFINITAS'))
            self.senal_actualizar_tiempo.emit('INFINITO')

    def cheatcode_kil(self):
        for fantasma_v in self.fantasmas_v[:]:
            fila = fantasma_v.fila
            columna = fantasma_v.columna
            self.mapa[fila][columna] = '-'
            self.senal_borrar_fantasma.emit(('V', fantasma_v))
        for fantasma_h in self.fantasmas_h[:]:
            fila = fantasma_h.fila
            columna = fantasma_h.columna
            self.mapa[fila][columna] = '-'
            self.senal_borrar_fantasma.emit(('H', fantasma_h))
        self.fantasmas_h = []
        self.fantasmas_v = []
        self.kil_activado = True
        self.timer_fantasmas.stop()

    def ganar(self):
        self.timer_juego.stop()
        self.timer_fantasmas.stop()
        self.musica_ganar = QSound(p.RUTA_MUSICA_GANAR)
        self.musica_ganar.play()
        if self.inf_activado is True:
            puntuacion = calcular_puntuacion(p.TIEMPO_CUENTA_REGRESIVA,
                                             p.CANTIDAD_VIDAS)
        else:
            puntuacion = calcular_puntuacion(self.segundos_restantes,
                                             self.vidas)
        self.senal_pop_ganar.emit(self.nombre_usuario, puntuacion)

    def perder(self):
        self.musica_perder = QSound(p.RUTA_MUSICA_PERDER)
        self.musica_perder.play()
        self.senal_pop_perder.emit(self.nombre_usuario)
