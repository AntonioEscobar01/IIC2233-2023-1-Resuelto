from PyQt5.QtCore import Qt, pyqtSignal, QTimer, QRect, QPropertyAnimation
from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout, QVBoxLayout,
                             QHBoxLayout, QFormLayout, QPushButton,
                             QMessageBox)
from PyQt5.QtGui import QPixmap, QIcon, QFont
from backend.funciones import cargar_pixmaps_fantasmas
import parametros as p


class VentanaJuego(QWidget):
    senal_teclas = pyqtSignal(str)
    senal_ganar = pyqtSignal()
    senal_boton_pausa = pyqtSignal()
    senal_cheatcode_inf = pyqtSignal()
    senal_cheatcode_kil = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init__gui()

    def init__gui(self):

        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle('Ventana de Juego')
        self.setFixedSize(900, 600)
        self.setWindowIcon(QIcon(p.RUTA_ICONO_LUIGI))
        self.layout_general = QHBoxLayout()
        self.layout_general.addSpacing(10)
        self.crear_info()
        self.layout_general.addSpacing(5)
        self.grilla = QGridLayout()
        self.grilla.setSpacing(0)
        for row in range(p.ANCHO_GRILLA):
            for col in range(p.LARGO_GRILLA):
                casilla = QLabel(self)
                if col == 0 or col == 15 or row == 0 or row == 10:
                    casilla.setPixmap(QPixmap(p.RUTA_BORDES).scaled(32, 32))
                    casilla.setScaledContents(True)
                else:
                    casilla.setStyleSheet('''background-color: #222222;
                    border-style: solid; border-width: 1px;
                    border-color: #333333;''')
                self.grilla.addWidget(casilla, col, row)
        self.layout_general.addLayout(self.grilla)
        self.setLayout(self.layout_general)
        self.timer_mover_luigi = QTimer(self)
        self.timer_mover_luigi.setInterval(10)
        self.timer_mover_luigi.timeout.connect(self.mover_luigi)
        self.timer_animacion_luigi = QTimer(self)
        self.timer_animacion_luigi.setInterval(p.FRAME_RATE_LUIGI)
        self.timer_animacion_luigi.timeout.connect(self.cambiar_pixmap_luigi)
        self.timer_animacion_fantasmas = QTimer(self)
        self.timer_animacion_fantasmas.setInterval(p.FRAME_RATE_FANTASMAS)
        self.timer_animacion_fantasmas.timeout.connect(self.cambiar_pixmap_f)
        self.tiempo_movimiento_fantasmas = int()
        self.imagen_actual_f = 0
        self.imagen_actual_luigi = 0
        self.pixmaps_luigi = list()
        self.pixmaps_v = cargar_pixmaps_fantasmas(p.RUTA_FV)
        self.flag_teclado = True
        self.dic_fantasmas_h = {}
        self.dic_fantasmas_v = {}
        self.dic_animaciones_h = {}
        self.dic_animaciones_v = {}
        self.lista_bloques = []
        self.dic_rocas = {}
        self.i_presionada = False
        self.n_presionada = False
        self.f_presionada = False
        self.k_presionada = False
        self.l_presionada = False

    def crear_info(self):
        self.layout_izquierdo = QHBoxLayout()
        self.layout_izquierdo.addSpacing(30)
        self.layout_info = QVBoxLayout()
        self.layout_info.addSpacing(15)
        self.grilla_info = QFormLayout()
        self.texo_tiempo = QLabel('Tiempo:', self)
        self.texo_tiempo.setFont(QFont("Arial", 11))
        self.texto_vida = QLabel('Vidas:', self)
        self.texto_vida.setFont(QFont("Arial", 11))
        self.contador_tiempo = QLabel('00:00', self)
        self.contador_tiempo.setFont(QFont("Arial", 11))
        self.vidas = QLabel(str(p.CANTIDAD_VIDAS), self)
        self.vidas.setFont(QFont("Arial", 11))
        self.grilla_info.addRow(self.texo_tiempo, self.contador_tiempo)
        self.grilla_info.addRow(self.texto_vida, self.vidas)
        self.layout_info.addLayout(self.grilla_info)
        self.layout_info.addSpacing(30)
        self.boton_pausa = QPushButton('PAUSAR JUEGO', self)
        self.boton_pausa.clicked.connect(self.senal_boton_pausa.emit)
        self.layout_info.addWidget(self.boton_pausa)
        self.layout_info.addSpacing(1000)
        self.layout_izquierdo.addLayout(self.layout_info)
        self.layout_general.addLayout(self.layout_izquierdo)

    def cambiar_vidas(self, vidas):
        self.vidas.setText(vidas)

    def aparecer_luigi(self, x, y):
        self.luigi_x = x
        self.luigi_y = y
        self.label_luigi = QLabel(self)
        self.label_luigi.setGeometry(x, y, 39, 36)
        self.label_luigi.setPixmap(QPixmap(p.RUTA_ICONO_LUIGI))
        self.label_luigi.setScaledContents(True)
        self.label_luigi.show()
        self.label_luigi.raise_()

    def keyPressEvent(self, event):
        if self.flag_teclado is True:
            if self.timer_mover_luigi.isActive() is False:
                if event.key() == Qt.Key_A and not event.isAutoRepeat():
                    self.senal_teclas.emit('left')
                if event.key() == Qt.Key_D and not event.isAutoRepeat():
                    self.senal_teclas.emit('right')
                if event.key() == Qt.Key_W and not event.isAutoRepeat():
                    self.senal_teclas.emit('up')
                if event.key() == Qt.Key_S and not event.isAutoRepeat():
                    self.senal_teclas.emit('down')
                if event.key() == Qt.Key_G:
                    posicion_estrella = self.estrella.geometry()
                    x_estrella = posicion_estrella.x()
                    y_estrella = posicion_estrella.y()
                    posicion_luigi = self.label_luigi.geometry()
                    x_luigi = posicion_luigi.x()
                    y_luigi = posicion_luigi.y()
                    if x_estrella in range(x_luigi - 2, x_luigi + 3) and \
                            y_estrella in range(y_luigi - 2, y_luigi + 3):
                        self.senal_ganar.emit()
            if event.key() == Qt.Key_I:
                self.i_presionada = True
            if event.key() == Qt.Key_F:
                self.f_presionada = True
            if event.key() == Qt.Key_N:
                self.n_presionada = True
            if event.key() == Qt.Key_K:
                self.k_presionada = True
            if event.key() == Qt.Key_L:
                self.l_presionada = True
            if self.i_presionada and self.k_presionada and self.l_presionada:
                self.senal_cheatcode_kil.emit()
            if self.i_presionada and self.f_presionada and self.n_presionada:
                self.senal_cheatcode_inf.emit()
        if event.key() == Qt.Key_P:
            self.senal_boton_pausa.emit()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_K:
            self.k_presionada = False
        if event.key() == Qt.Key_L:
            self.l_presionada = False
        if event.key() == Qt.Key_I:
            self.i_presionada = False
        if event.key() == Qt.Key_F:
            self.f_presionada = False
        if event.key() == Qt.Key_N:
            self.n_presionada = False

    def lista_pixmap(self, lista_fotos):
        self.pixmaps_luigi = lista_fotos

    def cambiar_pixmap_luigi(self):
        pixmap_nuevo = self.pixmaps_luigi[self.imagen_actual_luigi]
        self.label_luigi.setPixmap(pixmap_nuevo)
        self.imagen_actual_luigi += 1
        if self.imagen_actual_luigi == 3:
            self.imagen_actual_luigi = 0

    def cambiar_pixmap_f(self):
        pixmap_v = self.pixmaps_v[self.imagen_actual_f]
        for fantasmav in self.dic_fantasmas_v.values():
            fantasmav.setPixmap(pixmap_v)
        for obj_fantasmah, label in self.dic_fantasmas_h.items():
            lista_pixmaps = obj_fantasmah.pix_actual
            pix_colocar = lista_pixmaps[self.imagen_actual_f]
            label.setPixmap(pix_colocar)
        self.imagen_actual_f += 1
        if self.imagen_actual_f == 3:
            self.imagen_actual_f = 0

    def mover_luigi(self):
        posicion_actual = self.label_luigi.geometry()
        label_x = posicion_actual.x()
        label_y = posicion_actual.y()
        if self.luigi_x != label_x:
            if self.luigi_x < label_x:
                self.label_luigi.move(label_x - 1, label_y)
            elif self.luigi_x > label_x:
                self.label_luigi.move(label_x + 1, label_y)
        elif self.luigi_y != label_y:
            if self.luigi_y < label_y:
                self.label_luigi.move(label_x, label_y - 1)
            elif self.luigi_y > label_y:
                self.label_luigi.move(label_x, label_y + 1)
        else:
            self.timer_mover_luigi.stop()
            self.timer_animacion_luigi.stop()

    def actualizar_label_luigi(self, x, y):
        self.luigi_x = x
        self.luigi_y = y

    def colocar_bloques(self, info):
        pixmap_bloques = {'P': p.RUTA_ICONO_LADRILLO, 'F': p.RUTA_ICONO_FUEGO,
                          'S': p.RUTA_ICONO_ESTRELLA}
        tipo_bloque = info[2]
        if tipo_bloque == 'S':
            self.estrella = QLabel(self)
            self.estrella.setGeometry(info[0], info[1], 39, 36)
            self.estrella.setPixmap(QPixmap(pixmap_bloques[tipo_bloque]))
            self.estrella.setScaledContents(True)
            self.estrella.show()
        else:
            self.bloque = QLabel(self)
            self.bloque.setGeometry(info[0], info[1], 39, 36)
            self.bloque.setPixmap(QPixmap(pixmap_bloques[tipo_bloque]))
            self.bloque.setScaledContents(True)
            self.lista_bloques.append(self.bloque)
            self.bloque.show()

    def borrar_labels(self):
        for bloque in self.lista_bloques:
            bloque.deleteLater()
        for fantasmah in self.dic_fantasmas_h.values():
            fantasmah.deleteLater()
        for roca in self.dic_rocas.values():
            roca.deleteLater()
        for fantasmav in self.dic_fantasmas_v.values():
            fantasmav.deleteLater()
        self.estrella.deleteLater()
        self.label_luigi.deleteLater()
        self.lista_bloques = []
        self.dic_fantasmas_h = {}
        self.dic_fantasmas_v = {}
        self.dic_animaciones_h = {}
        self.dic_animaciones_v = {}
        self.dic_rocas = {}

    def colocar_roca(self, info):
        obj_roca = info[0]
        self.roca = QLabel(self)
        self.roca.setGeometry(info[1], info[2], 39, 36)
        self.roca.setPixmap(QPixmap(p.RUTA_ICONO_ROCA))
        self.roca.setScaledContents(True)
        self.dic_rocas[obj_roca] = self.roca
        self.roca.show()

    def colocar_fantasmas(self, info):
        self.label_fantasma = QLabel(self)
        self.label_fantasma.setGeometry(info[2], info[3], 39, 36)
        self.label_fantasma.setScaledContents(True)
        self.animacion = QPropertyAnimation(self.label_fantasma, b"geometry")
        if info[0] == 'H':
            self.label_fantasma.setPixmap(QPixmap(p.RUTA_ICONO_FH))
            self.dic_fantasmas_h[info[1]] = self.label_fantasma
            self.dic_animaciones_h[self.label_fantasma] = self.animacion
        elif info[0] == 'V':
            self.label_fantasma.setPixmap(QPixmap(p.RUTA_ICONO_FV))
            self.dic_fantasmas_v[info[1]] = self.label_fantasma
            self.dic_animaciones_v[self.label_fantasma] = self.animacion
        self.timer_animacion_fantasmas.start()
        self.label_fantasma.show()

    def mover_fantasma(self, info):
        if info[0] == 'H':
            label = self.dic_fantasmas_h[info[1]]
            animacion = self.dic_animaciones_h.pop(label)
            posicion = label.geometry()
            animacion.setDuration(self.tiempo_movimiento_fantasmas)
            animacion.setStartValue(QRect(posicion.x(), posicion.y(), 39, 36))
            animacion.setEndValue(QRect(info[2], info[3], 39, 36))
            animacion.start()
            self.dic_fantasmas_h[info[1]] = label
            self.dic_animaciones_h[label] = animacion
        elif info[0] == 'V':
            label = self.dic_fantasmas_v[info[1]]
            animacion = self.dic_animaciones_v.pop(label)
            posicion = label.geometry()
            animacion.setDuration(self.tiempo_movimiento_fantasmas)
            animacion.setStartValue(QRect(posicion.x(), posicion.y(), 39, 36))
            animacion.setEndValue(QRect(info[2], info[3], 39, 36))
            animacion.start()
            self.dic_fantasmas_v[info[1]] = label
            self.dic_animaciones_v[label] = animacion

    def borrar_fantasma(self, info):
        if info[0] == 'H':
            self.dic_fantasmas_h[info[1]].deleteLater()
            label = self.dic_fantasmas_h.pop(info[1])
            self.dic_animaciones_h.pop(label)
        elif info[0] == 'V':
            self.dic_fantasmas_v[info[1]].deleteLater()
            label = self.dic_fantasmas_v.pop(info[1])
            self.dic_animaciones_v.pop(label)

    def levantar(self):
        self.label_luigi.raise_()

    def mover_roca(self, info):
        label_roca = self.dic_rocas[info[0]]
        label_roca.move(info[1], info[2])

    def pop_up_ganar(self, nombre: str, puntuacion: str):
        pop = QMessageBox()
        pop.setWindowIcon(QIcon(p.RUTA_ICONO_LUIGI))
        pop.setWindowTitle('Juego Completado')
        pop.setText(f'''{nombre.upper()}\nFELICIDADES POR GANAR EL JUEGO
PUNTUACION: {puntuacion}''')
        self.boton_salir = QPushButton('SALIR', self)
        pop.addButton(self.boton_salir, QMessageBox.RejectRole)
        self.boton_salir.clicked.connect(pop.close)
        pop.exec_()
        self.salir()

    def pop_up_perder(self, nombre: str):
        pop = QMessageBox()
        pop.setWindowIcon(QIcon(p.RUTA_ICONO_LUIGI))
        pop.setWindowTitle('MAS SUERTE A LA PROXIMA')
        pop.setText(f'''{nombre.upper()}\nLO SENTIMOS\nNO LOGRASTE GANAR''')
        self.boton_salir2 = QPushButton('SALIR', self)
        pop.addButton(self.boton_salir2, QMessageBox.RejectRole)
        self.boton_salir2.clicked.connect(pop.close)
        pop.exec_()
        self.salir()

    def actualizar_tiempo(self, tiempo):
        self.contador_tiempo.setText(tiempo)

    def bloquear_teclado(self, flag):
        self.flag_teclado = flag
        if flag is False:
            self.timer_animacion_fantasmas.stop()
        elif flag is True:
            self.timer_animacion_fantasmas.start()

    def set_tiempo_fantasmas(self, tiempo: int):
        self.tiempo_movimiento_fantasmas = tiempo

    def salir(self):
        self.close()

    def mostrar_ventana(self):
        self.show()
