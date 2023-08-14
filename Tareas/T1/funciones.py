import os
import parametros
from random import randint
from Arena import ArenaMagnetica, ArenaMojada, ArenaNormal, ArenaRocosa
from Excavador import ExcavadorDocencio, ExcavadorHibrido, ExcavadorTareo
from torneo import Torneo
from Items import Consumible, Tesoro


def leer_archivo(nombre_archivo) -> list:
    try:
        ruta = os.path.join(nombre_archivo)
        with open(ruta, 'r', encoding="utf-8") as archivo_cargar:
            lineas = archivo_cargar.readlines()
        return [(linea.strip('\n')).split(",") for linea in lineas[1:]]

    except FileNotFoundError:
        print("No existen los archivos necesarios para jugar")
        print("\nCerrando programa\n")
        exit()


def crear_arenas(info_archivo, lista_items) -> list:
    arenas = []
    for linea in info_archivo:
        if linea[1] == 'magnetica':
            arenas.append(ArenaMagnetica(nombre=linea[0], tipo=linea[1],
                                         rareza=int(linea[2]), humedad=int(linea[3]),
                                         dureza=int(linea[4]), estatica=int(linea[5]),
                                         items=lista_items))
        elif linea[1] == 'normal':
            arenas.append(ArenaNormal(nombre=linea[0], tipo=linea[1],
                                      rareza=int(linea[2]), humedad=int(linea[3]),
                                      dureza=int(linea[4]), estatica=int(linea[5]),
                                      items=lista_items))

        elif linea[1] == 'mojada':
            arenas.append(ArenaMojada(nombre=linea[0], tipo=linea[1],
                                      rareza=int(linea[2]), humedad=int(linea[3]),
                                      dureza=int(linea[4]), estatica=int(linea[5]),
                                      items=lista_items))

        elif linea[1] == 'rocosa':
            arenas.append(ArenaRocosa(nombre=linea[0], tipo=linea[1],
                                      rareza=int(linea[2]), humedad=int(linea[3]),
                                      dureza=int(linea[4]), estatica=int(linea[5]),
                                      items=lista_items))
    return arenas


def crear_excavadores(info_archivo) -> list:
    excavadores = []
    for linea in info_archivo:
        if linea[1] == 'docencio':
            excavadores.append(ExcavadorDocencio(nombre=linea[0], tipo=linea[1],
                                                 edad=int(linea[2]), energia=int(linea[3]),
                                                 fuerza=int(linea[4]), suerte=int(linea[5]),
                                                 felicidad=int(linea[6])))

        elif linea[1] == 'hibrido':
            excavadores.append(ExcavadorHibrido(nombre=linea[0], tipo=linea[1],
                                                edad=int(linea[2]), energia=int(linea[3]),
                                                fuerza=int(linea[4]), suerte=int(linea[5]),
                                                felicidad=int(linea[6])))

        elif linea[1] == 'tareo':
            excavadores.append(ExcavadorTareo(nombre=linea[0], tipo=linea[1], edad=int(linea[2]),
                                              energia=int(linea[3]), fuerza=int(linea[4]),
                                              suerte=int(linea[5]), felicidad=int(linea[6])))
    return excavadores


def crear_consumibles(info_archivo) -> list:
    consumibles = []
    for linea in info_archivo:
        consumibles.append(Consumible(nombre=linea[0], tipo='consumible', descripcion=linea[1],
                                      energia=int(linea[2]), fuerza=int(linea[3]),
                                      suerte=int(linea[4]), felicidad=int(linea[5])))
    return consumibles


def crear_tesoro(info_archivo) -> list:
    tesoros = []
    for linea in info_archivo:
        tesoros.append(Tesoro(nombre=linea[0], tipo='tesoro',
                              descripcion=linea[1], calidad=int(linea[2]),
                              cambio=linea[3]))
    return tesoros


def imprimir_menu_inicio() -> str:
    print('''
        ***Menú de Inicio***
    ----------------------------
    [1] Nueva partida
    [2] Cargar partida
    [X] Salir
    ''')
    input_usuario = input('\nIndique su opción (1, 2 o X): ')
    return input_usuario


def imprimir_menu_principal(dia, tipo, dias_totales) -> str:
    print(f'''
            ***Menú Principal***
    -------------------------------------
    Día torneo DCCavaCava: {dia}/{dias_totales}
    Tipo de arena: {tipo.title()}

    [1] Simular día torneo
    [2] Ver estado torneo
    [3] Ver ítems
    [4] Guardar partida
    [5] Volver
    [X] Salir del programa
    ''')
    input_usuario = input('\nIndique su opción (1, 2, 3, 4, 5 o X): ')
    return input_usuario


def nueva_partida() -> object:
    info_excavadores = leer_archivo('excavadores.csv')
    excavadores = crear_excavadores(info_excavadores)
    info_consumibles = leer_archivo('consumibles.csv')
    consumibles = crear_consumibles(info_consumibles)
    info_arenas = leer_archivo('arenas.csv')
    info_tesoros = leer_archivo('tesoros.csv')
    tesoros = crear_tesoro(info_tesoros)
    arenas = crear_arenas(info_arenas, [consumibles, tesoros])

    encontre_arena = False
    while encontre_arena is False:
        arena_aleatoria = arenas[randint(0, len(arenas)-1)]
        if arena_aleatoria.tipo == parametros.ARENA_INICIAL:
            arena_inicial = arena_aleatoria
            encontre_arena = True

    equipo = list()
    while len(equipo) != parametros.CANTIDAD_EXCAVADORES_INICIALES:
        excavador = excavadores[randint(0, len(excavadores)-1)]
        if excavador not in equipo:
            equipo.append(excavador)

    torneo_actual = Torneo(arena_inicial, equipo, [],
                           0, parametros.METROS_META,
                           1, parametros.DIAS_TOTALES_TORNEO,
                           arenas, excavadores)
    return torneo_actual


def imprimir_menu_termino(dia, metros, meta) -> str:
    texto_dias = f'{dia} de {dia} dias'
    print(f'''{'-'*60}
{'***** TORNEO TERMINADO *****'.center(60)}
{'-'*60}
{texto_dias.center(60)}
{'-'*60}''')
    if metros >= meta:
        print('*** FELICIDADES POR LLEGAR A LA META ***'.center(60))
    else:
        print('*** MAS SUERTE LA PROXIMA VEZ ***'.center(60))
        metros_recorridos = f'Cavaron {metros} metros de {meta} metros'
        print(metros_recorridos.center(60))
    print(f'''{'-'*60}

    [1] Guardar partida
    [2] Volver
    [X] Salir del programa
    ''')
    input_usuario = input('\nIndique su opción (1, X): ')
    if input_usuario not in ['1', '2', 'x', 'X']:
        print('\nOpción no valida')
        return imprimir_menu_termino(dia, metros, meta)
    else:
        return input_usuario


def guardar_partida(torneo) -> None:
    texto_guardar = ''
    metros = torneo.metros_cavados
    meta = torneo.meta
    dia = torneo.dias_transcurridos
    total_dias = torneo.dias_totales
    texto_guardar += f'{metros},{meta},{dia},{total_dias};'

    items = ''
    for item in torneo.mochila:
        items += f'{item.nombre},'
    items = items[:-1]
    items += ';'
    texto_guardar += items

    nombre = torneo.arena.nombre
    tipo = torneo.arena.tipo
    rareza = int(torneo.arena.rareza)
    humedad = int(torneo.arena.humedad)
    dureza = int(torneo.arena.dureza)
    estatica = int(torneo.arena.estatica)
    texto_guardar += f'{nombre},{tipo},{rareza},{humedad},{dureza},{estatica};'

    texto_equipo = ''
    for excavador in torneo.equipo:
        nombre_e = excavador.nombre
        tipo_e = excavador.tipo
        edad = int(excavador.edad)
        energia = int(excavador.energia)
        fuerza = int(excavador.fuerza)
        suerte = int(excavador.suerte)
        felicidad = int(excavador.felicidad)
        texto_equipo += f'{nombre_e},{tipo_e},{edad},{energia},{fuerza},{suerte},{felicidad}/'
    texto_equipo = texto_equipo[:-1]
    texto_guardar += texto_equipo

    ruta = os.path.join('DCCavaCava.txt')
    with open(ruta, 'wt') as archivo_escribir:
        archivo_escribir.write(texto_guardar)

    print('\n***Partida Guardada***\n'.center(60))


def cargar_partida() -> object:
    try:
        ruta = os.path.join('DCCavaCava.txt')
        with open(ruta, 'r') as archivo_cargar:
            lineas_archivo = archivo_cargar.readline()
        lineas_archivo = lineas_archivo.split(';')
        info_excavadores = leer_archivo('excavadores.csv')
        excavadores = crear_excavadores(info_excavadores)
        info_consumibles = leer_archivo('consumibles.csv')
        consumibles = crear_consumibles(info_consumibles)
        info_arenas = leer_archivo('arenas.csv')
        info_tesoros = leer_archivo('tesoros.csv')
        tesoros = crear_tesoro(info_tesoros)
        arenas = crear_arenas(info_arenas, [consumibles, tesoros])
        info_torneo = lineas_archivo[0].split(',')
        info_items = lineas_archivo[1].split(',')
        info_arena = lineas_archivo[2].split(',')
        info_equipo = lineas_archivo[3]

        metros = float(info_torneo[0])
        meta = float(info_torneo[1])
        dia = int(info_torneo[2])
        total_dias = int(info_torneo[3])

        mochila = []
        for nombre_item in info_items:
            ya_encontre = False
            for tesoro in tesoros:
                if nombre_item == tesoro.nombre:
                    mochila.append(tesoro)
                    ya_encontre = True
                    break
            if ya_encontre is False:
                for consumible in consumibles:
                    if nombre_item == consumible.nombre:
                        mochila.append(consumible)
                        break

        arena_actual = (crear_arenas([info_arena], [consumibles, tesoros]))[0]
        info_excavadores_existentes = []
        for linea in info_equipo.split('/'):
            info_excavadores_existentes.append(linea.split(','))

        excavadores_existentes = crear_excavadores(info_excavadores_existentes)

        torneo_cargado = Torneo(arena_actual, excavadores_existentes, mochila,
                                metros, meta, dia, total_dias, arenas, excavadores)

        return torneo_cargado

    except FileNotFoundError:
        return None
