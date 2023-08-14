import sys
from PyQt5.QtWidgets import QApplication

from backend.logica import ControladorLogico
from frontend.control_remoto import VentanaControlRemoto
from frontend.pantalla import VentanaPantalla


if __name__ == '__main__':
    app = QApplication([])

    # Instanciamos las clases
    procesador = ControladorLogico()
    control_remoto = VentanaControlRemoto()
    pantalla = VentanaPantalla()

    # Conectamos las señales
    control_remoto.senal_volumen.connect(procesador.cambiar_volumen)
    control_remoto.senal_canal.connect(procesador.cambiar_canal)
    control_remoto.senal_encendido.connect(procesador.prender_apagar)


    # Empezamos la ejecución del programa
    procesador.senal_volumen.connect(pantalla.actualizar_volumen)
    procesador.senal_canal.connect(pantalla.actualizar_canal)
    procesador.senal_encendido.connect(pantalla.prender_apagar)
    procesador.senal_encendido.connect(control_remoto.prender_apagar)
    procesador.senal_empezar.connect(pantalla.show)
    procesador.senal_empezar.connect(control_remoto.show)


    procesador.empezar()

    sys.exit(app.exec())
