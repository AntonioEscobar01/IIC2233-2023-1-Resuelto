import parametros
from random import random, randint


class Torneo:
    def __init__(self, arena, equipo, mochila, metros_cavados, meta,
                 dias_transcurridos, dias_totales,
                 arenas_disponibles, excavadores_disponibles):

        self.arena = arena
        self.equipo = equipo
        self.mochila = mochila
        self.__metros_cavados = metros_cavados
        self.meta = meta
        self.dias_transcurridos = dias_transcurridos
        self.dias_totales = dias_totales
        self.arenas_disponibles = arenas_disponibles
        self.excavadores_disponibles = excavadores_disponibles

    @property
    def metros_cavados(self):
        return self.__metros_cavados

    @metros_cavados.setter
    def metros_cavados(self, p):
        if p < 0:
            self.__metros_cavados = 0
        else:
            self.__metros_cavados = p

    def simular_dia(self) -> None:
        if self.arena.tipo == 'magnetica':
            self.arena.nuevo_dia()
        print('\n')
        print(f'Día {self.dias_transcurridos}'.center(60))
        print('-'*60)
        dificultad_arena_actual = self.arena.dificultad_de_la_arena()
        metros_excavados = 0
        print('Metros Cavados:')
        for excavador in self.equipo:
            if excavador.dias_descanso == 0:
                metros_excavador = excavador.cavar(dificultad_arena_actual)
                metros_excavados += metros_excavador
                print(f'{excavador.nombre} ha cavado {metros_excavador} metros.')
        metros_excavados = round(metros_excavados, 2)
        print(f'El equipo ha conseguido excavar {metros_excavados} metros.\n')
        self.metros_cavados += metros_excavados

        print('Items Encontrados:')
        consumibles_encontrados = 0
        tesoros_encontrados = 0
        for excavador in self.equipo:
            if excavador.dias_descanso == 0:
                item = excavador.encontrar_item(self.arena.items, self.arena.tipo)
                if item is not None:
                    self.mochila.append(item)
                    print(f'{excavador.nombre} consiguió {item.nombre} del tipo {item.tipo}.')
                    if item.tipo == 'consumible':
                        consumibles_encontrados += 1
                    else:
                        tesoros_encontrados += 1
                else:
                    print(f'{excavador.nombre} no consiguió nada.')
            else:
                print(f'{excavador.nombre} no consiguió nada.')

        print(f'''Se han encontrado {consumibles_encontrados + tesoros_encontrados} ítems:
- {consumibles_encontrados} consumibles.
- {tesoros_encontrados} tesoros.
                  \n''')

        if random() <= parametros.PROB_INICIAR_EVENTO:
            self.iniciar_evento()

        else:
            print('Hoy no ocurrió un evento')
        for excavadores in self.equipo:
            if excavadores.dias_descanso != 0:
                excavadores.dias_descanso -= 1
                if excavadores.dias_descanso == 0:
                    excavadores.energia = 100
                print(f'{excavadores.nombre} decidió descansar...')
            else:
                excavadores.gastar_energia()
                if excavadores.energia == 0:
                    dias = excavadores.descansar()
                    print(f'{excavadores.nombre} gasto \
toda su energia y descansara por {dias} dias')

        self.dias_transcurridos += 1
        print('\n')

    def mostrar_estado(self) -> None:
        print('\n')
        print(f'''{'*** Estado Torneo ***'.center(60)}
{'-'*60}
Día actual: {self.dias_transcurridos}
Tipo de arena: {self.arena.tipo.title()}
Metros excavados: {int(self.metros_cavados)} / {int(self.meta)}
{'-'*60}
{'Excavadores'.center(60)}
{'-'*60}
{'  Nombre  |   Tipo   | Energía | Fuerza | Suerte | Felicidad '.center(60)}
{('-'*60)}''')

        for excavador in self.equipo:
            texto_nombre = excavador.nombre
            texto_tipo = (excavador.tipo).title().center(10)
            print(f'{texto_nombre:10.10s}|{texto_tipo:10.10s}|\
{int(excavador.energia):9d}|{int(excavador.fuerza):8d}|\
{int(excavador.suerte):8d}|{int(excavador.felicidad):10d}')
        print('-'*60)
        print()

    def ver_mochila(self) -> None:
        print('\n')
        print(f'''{'*** Menú Ítems ***'.center(85)}
{'-'*85}
{'Nombre': ^22s}|{'Tipo': ^12s}|{'Descripción': ^49s}
{('-'*85)}''')
        if len(self.mochila) > 0:
            for j, item in enumerate(self.mochila):
                nombre_opcion = f'[{j+1}] {item.nombre}'
                print(f'{nombre_opcion:22.22s}|\
 {item.tipo.title():11.11s}| {item.descripcion}')
        else:
            print('Mochila Vacia'.center(85))
        print(f'''{'-'*85}
[{len(self.mochila) + 1}] Volver
[X] Salir Programa''')
        opcion_usuario = input('\nIndique su opcion: \n')
        if opcion_usuario in ['X', 'x']:
            print('\nCerrando programa...\n')
            exit()
        else:
            try:
                opcion_usuario = int(opcion_usuario)
                if opcion_usuario in range(1, len(self.mochila) + 2):
                    if len(self.mochila) != 0 and opcion_usuario < len(self.mochila) + 1:
                        item = self.mochila[opcion_usuario - 1]
                        if item.tipo == 'consumible':
                            self.usar_consumible(item)
                        elif item.tipo == 'tesoro':
                            self.abrir_tesoro(item)
                        self.mochila.remove(item)
                        self.ver_mochila()
                    elif opcion_usuario == len(self.mochila) + 1:
                        return
                else:
                    print('Opcion no valida, debe ser entre 1 y X')
                    self.ver_mochila()
            except ValueError:
                print('Opcion no valida')
                self.ver_mochila()

    def usar_consumible(self, consumible) -> None:
        for excavador in self.equipo:
            excavador.consumir(consumible)
        print(f'''\nEl equipo utilizo el consumible {consumible.nombre}\
y este {consumible.descripcion}\n''')

    def abrir_tesoro(self, tesoro) -> None:
        if tesoro.calidad == 1:
            if len(self.equipo) == len(self.excavadores_disponibles):
                print('\nNo quedan excavadores para agregar al equipo\n')
            else:
                encontro_excavador = False
                for excavador in self.excavadores_disponibles:
                    ya_esta = False
                    for excavadores_equipo in self.equipo:
                        if excavador.nombre == excavadores_equipo.nombre:
                            ya_esta = True
                            break
                    if ya_esta is False and excavador.tipo == tesoro.cambio:
                        self.equipo.append(excavador)
                        print(f'\nEl nuevo integrante del equipo es {excavador.nombre}\n')
                        encontro_excavador = True
                        break
                if encontro_excavador is False:
                    print(f'\nNo quedan excavadores del tipo {tesoro.cambio}\n')
        elif tesoro.calidad == 2:
            for arenas_posibles in self.arenas_disponibles:
                if arenas_posibles.tipo == tesoro.cambio and arenas_posibles != self.arena:
                    self.arena = arenas_posibles
                    print(f'\nLa arena cambio a arena {self.arena.tipo}\n')
                    break

    def iniciar_evento(self) -> None:
        prob_aleatoria = random()
        if prob_aleatoria <= parametros.PROB_LLUVIA:
            print('Durante el día de trabajo LLOVIÓ')
            if self.arena.tipo == 'normal':
                encontre_arena = False
                while encontre_arena is False:
                    n_arenas = len(self.arenas_disponibles) - 1
                    arenas_posibles = self.arenas_disponibles[randint(0, n_arenas)]
                    if arenas_posibles.tipo == 'mojada' and arenas_posibles != self.arena:
                        self.arena = arenas_posibles
                        encontre_arena = True
            elif self.arena.tipo == 'rocosa':
                encontre_arena = False
                while encontre_arena is False:
                    n_arenas = len(self.arenas_disponibles) - 1
                    arenas_posibles = self.arenas_disponibles[randint(0, n_arenas)]
                    if arenas_posibles.tipo == 'magnetica' and arenas_posibles != self.arena:
                        self.arena = arenas_posibles
                        encontre_arena = True
        elif prob_aleatoria < parametros.PROB_LLUVIA + parametros.PROB_TERREMOTO:
            print('Durante el día de trabajo ocurrió un TERREMOTO')
            if self.arena.tipo == 'normal':
                encontre_arena = False
                while encontre_arena is False:
                    n_arenas = len(self.arenas_disponibles) - 1
                    arenas_posibles = self.arenas_disponibles[randint(0, n_arenas)]
                    if arenas_posibles.tipo == 'rocosa' and arenas_posibles != self.arena:
                        self.arena = arenas_posibles
                        encontre_arena = True
            elif self.arena.tipo == 'mojada':
                encontre_arena = False
                while encontre_arena is False:
                    n_arenas = len(self.arenas_disponibles) - 1
                    arenas_posibles = self.arenas_disponibles[randint(0, n_arenas)]
                    if arenas_posibles.tipo == 'magnetica' and arenas_posibles != self.arena:
                        self.arena = arenas_posibles
                        encontre_arena = True
        else:
            print('Durante el día de trabajo ocurrió un DERRUMBE')
            encontre_arena = False
            while encontre_arena is False:
                n_arenas = len(self.arenas_disponibles) - 1
                arenas_posibles = self.arenas_disponibles[randint(0, n_arenas)]
                if arenas_posibles.tipo == 'normal' and arenas_posibles != self.arena:
                    self.arena = arenas_posibles
                    encontre_arena = True
            print(f'El equipo perdio {parametros.METROS_PERDIDOS_DERRUMBE} metros de progreso')
            self.metros_cavados -= parametros.METROS_PERDIDOS_DERRUMBE
        print(f'La arena final es del tipo {self.arena.tipo}')
        for excavador in self.equipo:
            excavador.felicidad -= parametros.FELICIDAD_PERDIDA
