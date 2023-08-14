import parametros as p

from PyQt5.QtCore import pyqtSignal, QObject


class VentanaInicioBackend(QObject):
    senal_mensaje_error = pyqtSignal()
    senal_empezar_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def verificar_usuario(self, usuario: str):
        # Nombre debe ser alfanumerico y entre el largo de parametros
        if len(usuario) >= p.MIN_CARACTERES and \
                len(usuario) <= p.MAX_CARACTERES and usuario.isalnum():
            self.senal_empezar_juego.emit(usuario)
        else:
            self.senal_mensaje_error.emit()
