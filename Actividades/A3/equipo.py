from collections import defaultdict, deque


class Jugador:
    def __init__(self, nombre: str, velocidad: int) -> None:
        self.nombre = nombre
        self.velocidad = velocidad

    def __repr__(self) -> None:
        return f'Jugador: {self.nombre}, Velocidad: {self.velocidad}'


class Equipo:
    def __init__(self) -> None:
        self.jugadores = dict()
        self.dict_adyacencia = defaultdict(set)

    def agregar_jugador(self, id_jugador: int, jugador: Jugador) -> bool:
        if id_jugador not in self.jugadores:
            self.jugadores[id_jugador] = jugador
            return True
        else:
            return False

    def agregar_vecinos(self, id_jugador: int, vecinos: list[int]) -> int:
        if id_jugador not in self.dict_adyacencia:
            return -1
        else:
            set_actual = self.dict_adyacencia[id_jugador]
            cantidad = 0
            for vecino in vecinos:
                if vecino not in set_actual:
                    cantidad += 1
                    set_actual.add(vecino)
            return cantidad

    def mejor_amigo(self, id_jugador: int) -> Jugador:
        diferencia_menor = 10000000000000
        objeto_mejor_amigo = None
        jugador_actual = self.jugadores[id_jugador]
        velodicad_actual = jugador_actual.velocidad
        vecinos_jugador = self.dict_adyacencia[id_jugador]
        if len(vecinos_jugador) == 0:
            return None

        else:
            for id_vecino in vecinos_jugador:
                vecino = self.jugadores[id_vecino]
                velocidad_vecino = vecino.velocidad
                diferencia = abs(velodicad_actual - velocidad_vecino)
                if diferencia < diferencia_menor:
                    diferencia_menor = diferencia
                    objeto_mejor_amigo = vecino
            return objeto_mejor_amigo

    def peor_compañero(self, id_jugador: int) -> Jugador:
        diferencia_mayor = -1
        objeto_peor_amigo = None
        jugador_actual = self.jugadores[id_jugador]
        velodicad_actual = jugador_actual.velocidad
        if len(self.jugadores) == 1:
            return None

        else:
            for id_jugadores in self.jugadores:
                if id_jugadores != id_jugador:
                    vecino = self.jugadores[id_jugadores]
                    velocidad_vecino = vecino.velocidad
                    diferencia = abs(velodicad_actual - velocidad_vecino)
                    if diferencia > diferencia_mayor:
                        diferencia_mayor = diferencia
                        objeto_peor_amigo = vecino
            return objeto_peor_amigo

    def peor_conocido(self, id_jugador: int) -> Jugador:
        diferencia_mayor = -1
        objeto_peor_conocido = None
        jugador_actual = self.jugadores[id_jugador]
        velodicad_actual = jugador_actual.velocidad
        vecinos_jugador = self.dict_adyacencia[id_jugador]
        if len(vecinos_jugador) == 0:
            return None
        else:
            visitados = []
            queue = deque([id_jugador])
            while len(queue) > 0:
                vertice = queue.popleft()
                if vertice in visitados:
                    continue

                visitados.append(vertice)

                for vecino in self.dict_adyacencia[vertice]:
                    if vecino not in visitados:
                        queue.append(vecino)

            for ids in visitados:
                if ids != id_jugador:
                    conocido = self.jugadores[ids]
                    velocidad_conocido = conocido.velocidad
                    diferencia = abs(velodicad_actual - velocidad_conocido)
                    if diferencia > diferencia_mayor:
                        diferencia_mayor = diferencia
                        objeto_peor_conocido = conocido
            return objeto_peor_conocido

    def distancia(self, id_jugador_1: int, id_jugador_2: int) -> int:
        distancia_mas_corta = 1000000000
        distancia = 0
        visitados = []
        queue = deque([id_jugador_1])
        while len(queue) > 0:
            vertice = queue.popleft()
            if vertice in visitados:
                continue

            visitados.append(vertice)
            distancia += 1
            if vertice == id_jugador_2:
                if distancia_mas_corta > distancia:
                    distancia_mas_corta = distancia
                distancia = 0
            for vecino in self.dict_adyacencia[vertice]:
                if vecino not in visitados:
                    queue.append(vecino)

        if id_jugador_2 not in visitados:
            return -1

        distancia = 0
        visitados = []
        queue = deque([id_jugador_2])
        while len(queue) > 0:
            vertice = queue.popleft()
            if vertice in visitados:
                continue

            visitados.append(vertice)
            distancia += 1
            if vertice == id_jugador_1:
                if distancia_mas_corta > distancia:
                    distancia_mas_corta = distancia
                distancia = 0
            for vecino in self.dict_adyacencia[vertice]:
                if vecino not in visitados:
                    queue.append(vecino)

        return distancia_mas_corta - 1


if __name__ == '__main__':
    equipo = Equipo()
    jugadores = {
        0: Jugador('Alonso', 1),
        1: Jugador('Alba', 3),
        2: Jugador('Alicia', 6),
        3: Jugador('Alex', 10)
    }
    adyacencia = {
        0: [1],
        1: [0, 2],
        2: [1],
    }
    for idj, jugador in jugadores.items():
        equipo.agregar_jugador(id_jugador=idj, jugador=jugador)
    for idj, vecinos in adyacencia.items():
        equipo.agregar_vecinos(id_jugador=idj, vecinos=vecinos)

    print(f'El mejor amigo de Alba es {equipo.mejor_amigo(1)}')
    print(f'El peor compañero de Alonso es {equipo.peor_compañero(0)}')
    print(f'El peor amigo de Alicia es {equipo.peor_conocido(2)}')
    print(f'La distancia entre Alicia y Alonso es {equipo.distancia(2, 0)}')
    print(f'La distancia entre Alba y Alex es {equipo.distancia(1, 3)}')
