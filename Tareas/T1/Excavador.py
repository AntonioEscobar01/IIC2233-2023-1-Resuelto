import parametros
from abc import ABC, abstractmethod
from random import randint, random


class Excavador(ABC):
    def __init__(self, nombre, tipo) -> None:
        self.nombre = nombre
        self.tipo = tipo

    @abstractmethod
    def cavar(self, dificultad_arena) -> float:
        metros_cavados = ((30 / self.edad) +
                          ((self.felicidad + (2 * self.fuerza)) / 10))
        return round(metros_cavados * (1 / (10 * dificultad_arena)), 2)

    @abstractmethod
    def descansar(self) -> int:
        self.dias_descanso = int(self.edad / 20)
        return self.dias_descanso

    @abstractmethod
    def encontrar_item(self, lista_items, tipo_arena):
        if tipo_arena not in ['mojada', 'magnetica']:
            probabilidad_item = parametros.PROB_ENCONTRAR_ITEM * (self.suerte / 10)
            if random() <= probabilidad_item:
                if random() <= parametros.PROB_ENCONTRAR_CONSUMIBLE:
                    posicion_elemento = randint(0, len(lista_items[0])-1)
                    return lista_items[0][posicion_elemento]
                else:
                    posicion_elemento = randint(0, len(lista_items[1])-1)
                    return lista_items[1][posicion_elemento]
            else:
                return None
        else:
            if random() <= 0.5:
                posicion_elemento = randint(0, len(lista_items[0])-1)
                return lista_items[0][posicion_elemento]
            else:
                posicion_elemento = randint(0, len(lista_items[1])-1)
                return lista_items[1][posicion_elemento]

    @abstractmethod
    def gastar_energia(self) -> None:
        energia_gastada = int((10 / self.fuerza) + (self.edad / 6))
        self.energia -= energia_gastada

    @abstractmethod
    def consumir(self, item) -> None:
        if item.tipo == 'consumible':
            self.energia += item.energia
            self.fuerza += item.fuerza
            self.suerte += item.suerte
            self.felicidad += item.felicidad


class ExcavadorDocencio(Excavador):
    def __init__(self, edad, energia,
                 fuerza, suerte, felicidad, **kwargs) -> None:

        super().__init__(**kwargs)
        self.__edad = edad
        self.__energia = energia
        self.__fuerza = fuerza
        self.__suerte = suerte
        self.__felicidad = felicidad
        self.__dias_descanso = 0

    @property
    def dias_descanso(self) -> int:
        return self.__dias_descanso

    @dias_descanso.setter
    def dias_descanso(self, p):
        if p < 0:
            self.__dias_descanso = 0
        else:
            self.__dias_descanso = p

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, p):
        if p < 18:
            self.__edad = 18
        elif p > 60:
            self.__edad = 60
        else:
            self.__edad = p

    @property
    def energia(self) -> int:
        return self.__energia

    @energia.setter
    def energia(self, p):
        if p < 0:
            self.__energia = 0
        elif p > 100:
            self.__energia = 100
        else:
            self.__energia = p

    @property
    def fuerza(self) -> int:
        return self.__fuerza

    @fuerza.setter
    def fuerza(self, p):
        if p < 1:
            self.__fuerza = 1
        elif p > 10:
            self.__fuerza = 10
        else:
            self.__fuerza = p

    @property
    def suerte(self) -> int:
        return self.__suerte

    @suerte.setter
    def suerte(self, p):
        if p < 1:
            self.__suerte = 1
        elif p > 10:
            self.__suerte = 10
        else:
            self.__suerte = p

    @property
    def felicidad(self) -> int:
        return self.__felicidad

    @felicidad.setter
    def felicidad(self, p):
        if p < 1:
            self.__felicidad = 1
        elif p > 10:
            self.__felicidad = 10
        else:
            self.__felicidad = p

    def cavar(self, dificultad_arena) -> float:
        metros_cavados = ((30 / self.edad) +
                          ((self.felicidad + (2 * self.fuerza)) / 10))
        self.felicidad += parametros.FELICIDAD_ADICIONAL_DOCENCIO
        self.fuerza += parametros.FUERZA_ADICIONAL_DOCENCIO
        return round((metros_cavados * (1 / (10 * dificultad_arena))), 2)

    def descansar(self) -> int:
        return super().descansar()

    def encontrar_item(self, lista, tipo):
        return super().encontrar_item(lista, tipo)

    def gastar_energia(self) -> None:
        energia_gastada = int((10 / self.fuerza) + (self.edad / 6))
        self.energia -= energia_gastada
        self.energia -= parametros.ENERGIA_PERDIDA_DOCENCIO

    def consumir(self, item):
        return super().consumir(item)


class ExcavadorTareo(Excavador):
    def __init__(self, edad, energia,
                 fuerza, suerte, felicidad, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__edad = edad
        self.__energia = energia
        self.__fuerza = fuerza
        self.__suerte = suerte
        self.__felicidad = felicidad
        self.__dias_descanso = 0

    @property
    def dias_descanso(self) -> int:
        return self.__dias_descanso

    @dias_descanso.setter
    def dias_descanso(self, p):
        if p < 0:
            self.__dias_descanso = 0
        else:
            self.__dias_descanso = p

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, p):
        if p < 18:
            self.__edad = 18
        elif p > 60:
            self.__edad = 60
        else:
            self.__edad = p

    @property
    def energia(self) -> int:
        return self.__energia

    @energia.setter
    def energia(self, p):
        if p < 0:
            self.__energia = 0
        elif p > 100:
            self.__energia = 100
        else:
            self.__energia = p

    @property
    def fuerza(self) -> int:
        return self.__fuerza

    @fuerza.setter
    def fuerza(self, p):
        if p < 1:
            self.__fuerza = 1
        elif p > 10:
            self.__fuerza = 10
        else:
            self.__fuerza = p

    @property
    def suerte(self) -> int:
        return self.__suerte

    @suerte.setter
    def suerte(self, p):
        if p < 1:
            self.__suerte = 1
        elif p > 10:
            self.__suerte = 10
        else:
            self.__suerte = p

    @property
    def felicidad(self) -> int:
        return self.__felicidad

    @felicidad.setter
    def felicidad(self, p):
        if p < 1:
            self.__felicidad = 1
        elif p > 10:
            self.__felicidad = 10
        else:
            self.__felicidad = p

    def cavar(self, dificultad_arena) -> float:
        return super().cavar(dificultad_arena)

    def descansar(self) -> int:
        return super().descansar()

    def encontrar_item(self, lista, tipo):
        return super().encontrar_item(lista, tipo)

    def gastar_energia(self) -> None:
        return super().gastar_energia()

    def consumir(self, item) -> None:
        if item.tipo == 'consumible':
            self.energia += item.energia
            self.fuerza += item.fuerza
            self.suerte += item.suerte
            self.felicidad += item.felicidad

        self.energia += parametros.ENERGIA_ADICIONAL_TAREO
        self.suerte += parametros.SUERTE_ADICIONAL_TAREO
        self.edad += parametros.EDAD_ADICIONAL_TAREO
        self.felicidad -= parametros.FELICIDAD_PERDIDA_TAREO


class ExcavadorHibrido(Excavador):
    def __init__(self, edad, energia,
                 fuerza, suerte, felicidad, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__edad = edad
        self.__energia = energia
        self.__fuerza = fuerza
        self.__suerte = suerte
        self.__felicidad = felicidad
        self.dias_descanso = 0

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, p):
        if p < 18:
            self.__edad = 18
        elif p > 60:
            self.__edad = 60
        else:
            self.__edad = p

    @property
    def energia(self) -> int:
        return self.__energia

    @energia.setter
    def energia(self, p):
        if p < 20:
            self.__energia = 20
        elif p > 100:
            self.__energia = 100
        else:
            self.__energia = p

    @property
    def fuerza(self) -> int:
        return self.__fuerza

    @fuerza.setter
    def fuerza(self, p):
        if p < 1:
            self.__fuerza = 1
        elif p > 10:
            self.__fuerza = 10
        else:
            self.__fuerza = p

    @property
    def suerte(self) -> int:
        return self.__suerte

    @suerte.setter
    def suerte(self, p):
        if p < 1:
            self.__suerte = 1
        elif p > 10:
            self.__suerte = 10
        else:
            self.__suerte = p

    @property
    def felicidad(self) -> int:
        return self.__felicidad

    @felicidad.setter
    def felicidad(self, p):
        if p < 1:
            self.__felicidad = 1
        elif p > 10:
            self.__felicidad = 10
        else:
            self.__felicidad = p

    def cavar(self, dificultad_arena) -> float:
        metros_cavados = ((30 / self.edad) +
                          ((self.felicidad + (2 * self.fuerza)) / 10))
        self.felicidad += parametros.FELICIDAD_ADICIONAL_DOCENCIO
        self.fuerza += parametros.FUERZA_ADICIONAL_DOCENCIO
        return round((metros_cavados * (1 / (10 * dificultad_arena))), 2)

    def descansar(self) -> int:
        return 0

    def encontrar_item(self, lista, tipo):
        return super().encontrar_item(lista, tipo)

    def gastar_energia(self) -> None:
        energia_gastada = int((10 / self.fuerza) + (self.edad / 6))
        self.energia -= (energia_gastada / 2)
        self.energia -= parametros.ENERGIA_PERDIDA_DOCENCIO

    def consumir(self, item) -> None:
        if item.tipo == 'consumible':
            self.energia += item.energia
            self.fuerza += item.fuerza
            self.suerte += item.suerte
            self.felicidad += item.felicidad

        self.energia += parametros.ENERGIA_ADICIONAL_TAREO
        self.suerte += parametros.SUERTE_ADICIONAL_TAREO
        self.edad += parametros.EDAD_ADICIONAL_TAREO
        self.felicidad -= parametros.FELICIDAD_PERDIDA_TAREO
