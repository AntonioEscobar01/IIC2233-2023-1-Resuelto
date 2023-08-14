from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QHBoxLayout,
                             QVBoxLayout, QPushButton, QMessageBox)
from PyQt5.QtGui import QFont, QPixmap, QIcon
import os
import json
import sys


class VentanaInicio(QWidget):

    senal_salir = pyqtSignal()
    senal_comenzar = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with open(os.path.join('parametros.json')) as archivo:
            self.parametros = json.load(archivo)
        self.dic_nombres = {}
        self.init__gui()

    def init__gui(self):

        self.setGeometry(600, 250, 720, 720)
        self.setWindowTitle('Ventana de Inicio')
        self.setFixedSize(720, 720)
        self.ruta_icono = os.path.join(*self.parametros["RUTA_ICONO"])
        self.setWindowIcon(QIcon(self.ruta_icono))
        ruta_fondo = os.path.join(*self.parametros["RUTA_FONDO_INICIO"])
        self.fondo = QLabel(self)
        self.fondo.setPixmap(QPixmap(ruta_fondo))
        self.fondo.setFixedSize(720, 720)
        self.fondo.setScaledContents(True)

        self.layout_general = QVBoxLayout()
        self.layout_general.addSpacing(30)

        self.titulo = QLabel('SALA DE ESPERA', self)
        font_titulo = QFont("Arial", 35)
        font_titulo.setBold(True)
        self.titulo.setFont(font_titulo)
        self.layout_titulo = QHBoxLayout()
        self.layout_titulo.addStretch(1)
        self.layout_titulo.addWidget(self.titulo)
        self.layout_titulo.addStretch(1)
        self.layout_general.addLayout(self.layout_titulo)
        self.layout_general.addStretch()

        ruta_foto_vacia = os.path.join(*self.parametros["RUTA_USER_PROFILE"])
        self.layout_jugadores = QHBoxLayout()
        self.layout_jugadores.addSpacing(80)
        self.layout_nombres = QHBoxLayout()
        self.layout_nombres.addSpacing(70)
        for i in range(0, 4):
            foto_vacia = QLabel(self)
            foto_vacia.setPixmap(QPixmap(ruta_foto_vacia).scaled(90, 90))
            self.layout_jugadores.addWidget(foto_vacia)
            nombre_jugador = QLabel('----------------', self)
            self.dic_nombres[f'Jugador{i+1}'] = nombre_jugador
            font_nombres = QFont("Arial", 9)
            font_nombres.setBold(True)
            nombre_jugador.setFont(font_nombres)
            nombre_jugador.setFixedSize(113, 15)
            self.layout_nombres.addWidget(nombre_jugador)
            self.layout_nombres.addSpacing(45)
        self.layout_jugadores.addSpacing(10)
        self.layout_general.addLayout(self.layout_jugadores)
        self.layout_general.addLayout(self.layout_nombres)
        self.layout_general.addStretch()

        self.layout_botones_V = QVBoxLayout()
        self.layout_botones_H = QHBoxLayout()
        self.boton_comenzar = QPushButton('COMENZAR', self)
        self.boton_salir = QPushButton('SALIR', self)
        self.boton_salir.clicked.connect(self.salir)
        self.layout_botones_V.addWidget(self.boton_comenzar)
        self.layout_botones_V.addWidget(self.boton_salir)
        self.layout_botones_H.addStretch()
        self.layout_botones_H.addLayout(self.layout_botones_V)
        self.layout_botones_H.addStretch()
        self.layout_general.addLayout(self.layout_botones_H)
        self.layout_general.addSpacing(30)
        self.nombres_colocados = 0
        self.setLayout(self.layout_general)
        self.boton_comenzar.clicked.connect(self.senal_comenzar.emit)
        self.show()

    def agregar_nombre(self, info):
        if info[1] > 1 and info[1] < 5:
            for i in range(1, info[1] + 1):
                label = self.dic_nombres[f'Jugador{i}']
                nombre = self.parametros[f'id_{i}']
                label.setText(nombre)
                self.nombres_colocados += 1
        else:
            label = self.dic_nombres[f'Jugador{self.nombres_colocados + 1}']
            label.setText(info[0])
            self.nombres_colocados += 1

    def pop_up_lleno(self):
        pop_up = QMessageBox()
        pop_up.setWindowIcon(QIcon(self.ruta_icono))
        pop_up.setWindowTitle('SERVIDOR LLENO')
        pop_up.setText('''EL SERVIDOR ESTA LLENO
USTED SERA DESCONECTADO
ADIOS''')
        pop_up.exec_()
        self.salir()

    def salir(self):
        self.senal_salir.emit()
        self.close()

    def mostrar_ventana(self):
        self.show()

    def empezar(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_inicio = VentanaInicio()
    sys.exit(app.exec())
