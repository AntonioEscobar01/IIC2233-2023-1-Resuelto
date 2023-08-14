from backend.logica_cliente import Cliente
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from PyQt5.QtWidgets import QApplication
import sys


PORT = 3247 if len(sys.argv) < 2 else int(sys.argv[1])
HOST = 'localhost' if len(sys.argv) < 3 else sys.argv[2]
app = QApplication(sys.argv)
ventanainicio = VentanaInicio()
ventanajuego = VentanaJuego()
cliente = Cliente(PORT, HOST)
cliente.senal_empezar.connect(ventanainicio.empezar)
cliente.senal_empezar.connect(ventanajuego.empezar)
cliente.senal_agregar_nombre.connect(ventanainicio.agregar_nombre)
cliente.senal_lleno.connect(ventanainicio.pop_up_lleno)
ventanainicio.senal_salir.connect(cliente.salir)
ventanainicio.senal_comenzar.connect(cliente.comenzar)
sys.exit(app.exec())
