
class Mensaje:

    def __init__(self, operacion=None, data=None,
                 estado=None, numero=None):
        self.operacion = operacion
        self.data = data
        self.estado = estado
        self.numero = numero

    def __repr__(self) -> str:
        return f"*Mensaje: status {self.estado}*"


class Cliente:

    def __init__(self, numero, name) -> None:
        self.numero = numero
        self.name = name
