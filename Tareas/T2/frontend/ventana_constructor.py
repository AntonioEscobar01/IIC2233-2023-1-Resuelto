from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout, QVBoxLayout,
                             QHBoxLayout, QComboBox, QPushButton,
                             QButtonGroup, QMessageBox)
from PyQt5.QtGui import QPixmap, QIcon, QMouseEvent
import parametros as p


class VentanaConstuctor(QWidget):
    senal_mouse_presionado = pyqtSignal(int, int, str)
    senal_limpiar = pyqtSignal()
    senal_empezar = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init__gui()

    def init__gui(self):
        # Ventana
        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle('Modo Constructor')
        self.setFixedSize(900, 600)
        self.setWindowIcon(QIcon(p.RUTA_ICONO_LUIGI))

        # Layout
        self.layout_general = QHBoxLayout()
        self.layout_general.addSpacing(10)
        self.layout_entidades = QVBoxLayout()
        self.selector = QComboBox(self)
        self.selector.addItems(['Todos', 'Bloques', 'Entidades'])
        self.selector.currentTextChanged.connect(self.mostrar_entidades)
        self.layout_entidades.addWidget(self.selector)

        # Botones
        self.generar_botones_entidades()

        self.layout_entidades.addSpacing(1000)
        self.layout_opciones = QHBoxLayout()
        self.boton_jugar = QPushButton('Jugar', self)
        self.boton_jugar.clicked.connect(self.empezar_juego)
        self.boton_limpiar = QPushButton('Limpiar', self)
        self.boton_limpiar.clicked.connect(self.limpiar_tablero)
        self.layout_opciones.addWidget(self.boton_limpiar)
        self.layout_opciones.addWidget(self.boton_jugar)
        self.layout_entidades.addLayout(self.layout_opciones)
        self.layout_general.addLayout(self.layout_entidades)
        self.layout_general.addSpacing(5)

        # Grilla
        self.labels_tablero = []
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

    def generar_botones_entidades(self):
        self.grupo_botones = QButtonGroup()
        self.boton_luigi = QPushButton(icon=QIcon(p.RUTA_ICONO_LUIGI),
                                       text=f'({p.CANTIDAD_LUIGI})',
                                       parent=self)
        self.boton_ladrillo = QPushButton(icon=QIcon(p.RUTA_ICONO_LADRILLO),
                                          text=f'({p.MAXIMO_PARED})',
                                          parent=self)
        self.boton_roca = QPushButton(icon=QIcon(p.RUTA_ICONO_ROCA),
                                      text=f'({p.MAXIMO_ROCA})',
                                      parent=self)
        self.boton_estrella = QPushButton(icon=QIcon(p.RUTA_ICONO_ESTRELLA),
                                          text=f'({p.CANTIDAD_ESTRELLA})',
                                          parent=self)
        self.boton_fantasmaH = QPushButton(icon=QIcon(p.RUTA_ICONO_FH),
                                           text=f'({p.MAXIMO_FANTASMAS_HORIZONTAL})',
                                           parent=self)
        self.boton_fantasmaV = QPushButton(icon=QIcon(p.RUTA_ICONO_FV),
                                           text=f'({p.MAXIMO_FANTASMAS_VERTICAL})',
                                           parent=self)
        self.boton_fuego = QPushButton(icon=QIcon(p.RUTA_ICONO_FUEGO),
                                       text=f'({p.MAXIMO_FUEGO})',
                                       parent=self)
        self.grupo_botones.addButton(self.boton_luigi)
        self.grupo_botones.addButton(self.boton_ladrillo)
        self.grupo_botones.addButton(self.boton_roca)
        self.grupo_botones.addButton(self.boton_estrella)
        self.grupo_botones.addButton(self.boton_fantasmaH)
        self.grupo_botones.addButton(self.boton_fantasmaV)
        self.grupo_botones.addButton(self.boton_fuego)

        for boton in self.grupo_botones.buttons():
            boton.setCheckable(True)
            self.layout_entidades.addWidget(boton)
        self.grupo_botones.buttonClicked.connect(self.boton_presionado)

    def boton_presionado(self, boton_presionado):
        for boton in self.grupo_botones.buttons():
            if boton is not boton_presionado:
                boton.setChecked(False)

    def mostrar_entidades(self, texto):
        if texto == 'Todos':
            for boton in self.grupo_botones.buttons():
                boton.show()
        elif texto == 'Bloques':
            self.boton_luigi.hide()
            self.boton_ladrillo.show()
            self.boton_roca.show()
            self.boton_estrella.show()
            self.boton_fantasmaH.hide()
            self.boton_fantasmaV.hide()
            self.boton_fuego.show()
        elif texto == 'Entidades':
            self.boton_luigi.show()
            self.boton_ladrillo.hide()
            self.boton_roca.hide()
            self.boton_estrella.hide()
            self.boton_fantasmaH.show()
            self.boton_fantasmaV.show()
            self.boton_fuego.hide()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        etiquetas = {self.boton_luigi: 'L', self.boton_ladrillo: 'P',
                     self.boton_roca: 'R', self.boton_estrella: 'S',
                     self.boton_fantasmaH: 'H', self.boton_fantasmaV: 'V',
                     self.boton_fuego: 'F'}
        if event.button() == Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            if x in range(500, 848) and y in range(49, 551):
                for botones in self.grupo_botones.buttons():
                    if botones.isChecked():
                        etiqueta = etiquetas[botones]
                        self.senal_mouse_presionado.emit(x, y, etiqueta)
                        break

    def anadir_label(self, posiciones, cantidad):
        for botones in self.grupo_botones.buttons():
            if botones.isChecked():
                label = QLabel(self)
                label.setFixedSize(39, 36)
                label.setScaledContents(True)
                label.move(*posiciones)
                self.labels_tablero.append(label)
                botones.setText(f'({cantidad})')
                if botones == self.boton_luigi:
                    label.setPixmap(QPixmap(p.RUTA_ICONO_LUIGI))
                elif botones == self.boton_ladrillo:
                    label.setPixmap(QPixmap(p.RUTA_ICONO_LADRILLO))
                elif botones == self.boton_roca:
                    label.setPixmap(QPixmap(p.RUTA_ICONO_ROCA))
                elif botones == self.boton_estrella:
                    label.setPixmap(QPixmap(p.RUTA_ICONO_ESTRELLA))
                elif botones == self.boton_fantasmaH:
                    label.setPixmap(QPixmap(p.RUTA_ICONO_FH))
                elif botones == self.boton_fantasmaV:
                    label.setPixmap(QPixmap(p.RUTA_ICONO_FV))
                elif botones == self.boton_fuego:
                    label.setPixmap(QPixmap(p.RUTA_ICONO_FUEGO))
                label.show()
                break

    def limpiar_tablero(self):
        for label in self.labels_tablero:
            label.deleteLater()
        self.labels_tablero = []
        self.boton_luigi.setText(f'({p.CANTIDAD_LUIGI})')
        self.boton_ladrillo.setText(f'({p.MAXIMO_PARED})')
        self.boton_roca.setText(f'({p.MAXIMO_ROCA})')
        self.boton_estrella.setText(f'({p.CANTIDAD_ESTRELLA})')
        self.boton_fantasmaH.setText(f'({p.MAXIMO_FANTASMAS_HORIZONTAL})')
        self.boton_fantasmaV.setText(f'({p.MAXIMO_FANTASMAS_VERTICAL})')
        self.boton_fuego.setText(f'({p.MAXIMO_FUEGO})')
        self.senal_limpiar.emit()

    def pop_up_posicion_ocupada(self):
        pop_up = QMessageBox()
        pop_up.setWindowIcon(QIcon(p.RUTA_ICONO_LUIGI))
        pop_up.setWindowTitle('Casilla ocupada')
        pop_up.setText('''No puedes colocar esta Entidad/Bloque
    La casilla ya esta ocupada
    Prueba en otra casilla''')
        pop_up.exec_()

    def empezar_juego(self):
        self.senal_empezar.emit(self.nombre_usuario)

    def abrir_ventana(self, nombre):
        self.nombre_usuario = nombre
        self.limpiar_tablero()
        self.show()

    def cerrar_ventana(self):
        self.close()
