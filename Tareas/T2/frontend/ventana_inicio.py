from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QComboBox, QPushButton,
                             QMessageBox)
from PyQt5.QtGui import QFont, QPixmap, QIcon
import os
import parametros as p


class VentanaInicio(QWidget):
    senal_verificar_usuario = pyqtSignal(str)
    senal_empezar_constructor = pyqtSignal(str)  # entrega el nombre de usuario
    senal_empezar_mapa = pyqtSignal(str, str)  # entrega el usuario y el mapa

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init__gui()

    def init__gui(self):

        self.setGeometry(600, 250, 600, 680)
        self.setWindowTitle('Ventana de Inicio')
        self.setFixedSize(600, 680)
        self.setWindowIcon(QIcon(p.RUTA_ICONO_LUIGI))

        self.layout_general = QVBoxLayout()
        self.layout_abajo = QVBoxLayout()

        self.fondo = QLabel(self)
        self.fondo.setPixmap(QPixmap(p.RUTA_FONDO).scaled(600, 500))
        self.fondo.setScaledContents(True)
        self.layout_general.addWidget(self.fondo)

        self.layout_input = QHBoxLayout()
        self.texto_usuario = QLabel('Username', self)
        self.texto_usuario.setFont(QFont("Arial", 10))
        self.layout_input.addWidget(self.texto_usuario)

        self.username = QLineEdit('', self)
        self.username.setStyleSheet("background-color: transparent;")
        self.layout_input.addWidget(self.username)
        self.layout_abajo.addLayout(self.layout_input)

        self.selector_mapa = QComboBox(self)
        self.selector_mapa.addItem('Constructor')
        self.lista_mapas = os.listdir(p.RUTA_MAPAS)
        self.selector_mapa.addItems(self.lista_mapas)
        self.layout_abajo.addWidget(self.selector_mapa)

        self.layout_botones = QHBoxLayout()
        self.boton_empezar = QPushButton("Empezar juego", self)
        self.boton_empezar.clicked.connect(self.verificar_usuario)
        self.boton_salir = QPushButton('Salir Juego', self)
        self.boton_salir.clicked.connect(self.salir)
        self.layout_botones.addWidget(self.boton_empezar)
        self.layout_botones.addWidget(self.boton_salir)
        self.layout_abajo.addLayout(self.layout_botones)
        self.layout_general.addLayout(self.layout_abajo)

        self.setLayout(self.layout_general)

        self.logo = QLabel(self)
        self.logo.setGeometry(40, 60, 518, 95)
        self.logo.setPixmap(QPixmap(p.RUTA_LOGO))
        self.logo.setScaledContents(True)

        self.show()

    def verificar_usuario(self):
        self.senal_verificar_usuario.emit(self.username.text())

    def pop_up_error(self):
        pop_up = QMessageBox()
        pop_up.setWindowIcon(QIcon(p.RUTA_ICONO_LUIGI))
        pop_up.setWindowTitle('Error nombre de usuario')
        pop_up.setText(f'''Nombre de Usuario invalido
Ingrese un nombre solo con caracteres alfanumericos
con un largo entre {p.MIN_CARACTERES} y {p.MAX_CARACTERES} caracteres''')
        pop_up.exec_()
        self.username.clear()

    def salir(self):
        self.close()

    def mostrar_ventana(self):
        self.campo_nombre.setText("")
        self.show()

    def empezar(self, nombre_usuario):
        opcion_seleccionada = self.selector_mapa.currentText()
        if opcion_seleccionada == 'Constructor':
            self.senal_empezar_constructor.emit(nombre_usuario)
        else:
            self.senal_empezar_mapa.emit(opcion_seleccionada, nombre_usuario)
        self.close()
