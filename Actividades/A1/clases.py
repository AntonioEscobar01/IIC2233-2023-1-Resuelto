from abc import ABC, abstractmethod


class Animal(ABC):
    identificador = 0

    def __init__(self, peso, nombre, *args, **kwargs) -> None:
        self.peso = peso
        self.nombre = nombre
        self.__energia = 100
        self.identificador = Animal.identificador
        Animal.identificador += 1

    @abstractmethod
    def desplazarse(self) -> None:
        pass

    @property
    def energia(self) -> int:
        return self.__energia

    @energia.setter
    def energia(self, p):
        if p < 0:
            self.__energia = 0
        else:
            self.__energia = p


class Terrestre(Animal):
    def __init__(self, cantidad_patas, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.cantidad_patas = cantidad_patas

    def energia_gastada_por_desplazamiento(self) -> int:
        return self.peso * 5

    def desplazarse(self) -> str:
        self.energia -= self.energia_gastada_por_desplazamiento()
        return 'caminando...'


class Acuatico(Animal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def energia_gastada_por_desplazamiento(self) -> int:
        return self.peso * 2

    def desplazarse(self) -> None:
        self.energia -= self.energia_gastada_por_desplazamiento()
        return 'nadando...'


class Perro(Terrestre):
    def __init__(self, raza, *args, **kwargs) -> None:
        super().__init__(cantidad_patas=4, *args, **kwargs)
        self.raza = raza

    def ladrar(self) -> str:
        return 'guau guau'


class Pez(Acuatico):
    def __init__(self, color, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.color = color

    def nadar(self) -> str:
        return 'moviendo aleta'


class Ornitorrinco(Acuatico, Terrestre):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def desplazarse(self) -> str:
        guardar_energia = self.energia
        str_acuatico = Acuatico.desplazarse(self)
        str_terrestre = Terrestre.desplazarse(self)
        self.energia = guardar_energia
        self.energia -= round(((Acuatico.energia_gastada_por_desplazamiento(self) + Terrestre.energia_gastada_por_desplazamiento(self)) / 2), 0)
        return str_acuatico + str_terrestre


if __name__ == '__main__':
    perro = Perro(nombre='Pongo', raza='Dalmata', peso=3)
    pez = Pez(nombre='Nemo', color='rojo', peso=1)
    ornitorrinco = Ornitorrinco(nombre='Perry', peso=2)

    perro.desplazarse()
    pez.desplazarse()
    ornitorrinco.desplazarse()
