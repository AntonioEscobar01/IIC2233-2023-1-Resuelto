import os
import functions
import tablero


'''
Le agrega el sufijo '__sol' a un str dado
'''


def cambiar_nombre_solucion(nombre: str) -> str:
    partes_nombre = nombre.split('.')
    nombre_retornar = partes_nombre[: len(partes_nombre)-1]
    return '.'.join(nombre_retornar) + '_sol.' + partes_nombre[-1]


'''
Imprime el menu de acciones en el formato indicado
'''


def imprimir_acciones() -> str:
    print('''
    ***Menú de Acciones***
    [1] Mostrar tablero
    [2] Validar tablero
    [3] Revisar solución
    [4] Solucionar tablero
    [5] Salir del programa
    ''')
    input_usuario = input('\nIndique su opción (1, 2, 3, 4 o 5): ')
    return input_usuario


'''
Se definio una funcion para cada accion del menu de acciones para simplificar el codigo
'''


def accion_1(info: list) -> str:
    print('\n')
    tablero.imprimir_tablero(info)


def accion_2(info: list) -> None:
    bombas_invalidas = functions.verificar_valor_bombas(info)
    tortugas_invalidas = functions.verificar_tortugas(info)
    if bombas_invalidas == 0 and tortugas_invalidas == 0:
        print('\nTablero valido\n')
    else:
        print('\nTablero invalido\n')


def accion_3(info: list) -> None:
    if functions.verificar_solucion(info) is True:
        print('\nSolucion valida\n')
    else:
        print('\nSolucion invalida\n')


def accion_4(info: list, nombre_archivo: str) -> list:
    if functions.verificar_solucion(info) is True:
        print('\nEste tablero ya esta solucionado\n')
        return info
    else:
        solucion = functions.solucionar_tablero(info[:])
        if solucion is not None:
            print('\nTablero solucionado\n \nGuardando solucion\n')
            nuevo_nombre = cambiar_nombre_solucion(nombre_archivo)
            functions.guardar_tablero(nuevo_nombre, solucion)
            accion_1(solucion)
            return solucion
        else:
            print('\nTablero no tiene solucion\n')
            return info


def accion_5(info: list) -> None:
    print('\nCerrando programa...\n')
    exit()


'''
Hace funcionar el menu de inicio y revisa si el archivo ingresado existe
'''


def menu_inicio() -> None:
    print('***Menú de Inicio***\n')
    nombre_posible_archivo = input(
        'Indique el nombre del archivo que desea abrir: ')
    ruta_archivo = os.path.join('Archivos', nombre_posible_archivo)
    if os.path.exists(ruta_archivo):
        info_archivo = functions.cargar_tablero(nombre_posible_archivo)
        menu_acciones(info_archivo, nombre_posible_archivo)
    else:
        print('\nOpción invalida. Cerrando programa\n')


'''
Hace funcionar el menu de acciones de forma recursiva para evitar errores de usuario
'''


def menu_acciones(info_archivo: list, nombre_archivo: str) -> None:
    accion_seleccionada = imprimir_acciones()
    if accion_seleccionada not in ['1', '2', '3', '4', '5']:
        print('\nOpción invalida. Ingresa un número del 1 al 5\n')
    else:
        opciones_menu = {
            '1': accion_1, '2': accion_2, '3': accion_3, '5': accion_5
        }
        if accion_seleccionada == '4':
            info_archivo = accion_4(info_archivo, nombre_archivo)
        else:
            opciones_menu[accion_seleccionada](info_archivo)
    menu_acciones(info_archivo, nombre_archivo)


menu_inicio()
