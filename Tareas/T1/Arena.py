import parametros
from abc import ABC, abstractmethod
from random import randint


class Arena(ABC):
    def __init__(self, nombre, tipo, rareza, humedad, dureza,
                 estatica, items, *args, **kwargs) -> None:

        self.nombre = nombre
        self.tipo = tipo
        self.__rareza = rareza
        self.__humedad = humedad
        self.__dureza = dureza
        self.__estatica = estatica
        self.items = items

    @property
    def rareza(self) -> int:
        return self.__rareza

    @rareza.setter
    def rareza(self, p):
        if p < 0:
            self.__rareza = 0
        elif p > 10:
            self.__rareza = 10
        else:
            self.__rareza = p

    @property
    def humedad(self) -> int:
        return self.__humedad

    @humedad.setter
    def humedad(self, p):
        if p < 0:
            self.__humedad = 0
        elif p > 10:
            self.__humedad = 10
        else:
            self.__humedad = p

    @property
    def dureza(self) -> int:
        return self.__dureza

    @dureza.setter
    def dureza(self, p):
        if p < 0:
            self.__dureza = 0
        elif p > 10:
            self.__dureza = 10
        else:
            self.__dureza = p

    @property
    def estatica(self) -> int:
        return self.__estatica

    @estatica.setter
    def estatica(self, p):
        if p < 0:
            self.__estatica = 0
        elif p > 10:
            self.__estatica = 10
        else:
            self.__estatica = p

    @abstractmethod
    def dificultad_de_la_arena(self) -> float:
        suma = self.rareza + self.humedad + self.dureza + self.estatica
        dificultad_arena = round(suma / 40, 2)
        return dificultad_arena


class ArenaNormal(Arena):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def dificultad_de_la_arena(self) -> float:
        suma = self.rareza + self.humedad + self.dureza + self.estatica
        dificultad_arena = round(suma / 40, 2)
        return round(dificultad_arena * parametros.POND_ARENA_NORMAL, 2)


class ArenaMojada(Arena):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def dificultad_de_la_arena(self) -> float:
        return super().dificultad_de_la_arena()


class ArenaRocosa(Arena):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def dificultad_de_la_arena(self) -> float:
        suma = self.rareza + self.humedad + (2 * self.dureza) + self.estatica
        dificultad_arena = round(suma / 40, 2)
        return dificultad_arena


class ArenaMagnetica(ArenaRocosa, ArenaMojada):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def nuevo_dia(self):
        self.humedad = randint(1, 10)
        self.dureza = randint(1, 10)

    def dificultad_de_la_arena(self) -> float:
        return super().dificultad_de_la_arena()
