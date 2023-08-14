from abc import ABC


class Item(ABC):
    def __init__(self, nombre, tipo, descripcion, *args, **kwargs) -> None:

        self.nombre = nombre
        self.tipo = tipo
        self.descripcion = descripcion


class Consumible(Item):
    def __init__(self, energia, fuerza, suerte, felicidad,
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.energia = energia
        self.fuerza = fuerza
        self.suerte = suerte
        self.felicidad = felicidad


class Tesoro(Item):
    def __init__(self, calidad, cambio, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.calidad = calidad
        self.cambio = cambio
