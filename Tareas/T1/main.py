from funciones import (imprimir_menu_inicio, imprimir_menu_principal,
                       nueva_partida, imprimir_menu_termino,
                       guardar_partida, cargar_partida)


def accion_1(torneo):
    torneo.simular_dia()


def accion_2(torneo):
    torneo.mostrar_estado()


def accion_3(torneo):
    torneo.ver_mochila()


def menu_inicio():
    input_usuario = imprimir_menu_inicio()
    if input_usuario in ['1', '2', 'X', 'x']:
        if input_usuario == '1':
            torneo = nueva_partida()
            menu_principal(torneo)
        elif input_usuario == '2':
            torneo_cargado = cargar_partida()
            if torneo_cargado is not None:
                menu_principal(torneo_cargado)
            else:
                print("\nNo hay ninguna partida guardada\n")
        else:
            print('\nCerrando programa...\n')
            exit()
    else:
        print('\nOpcion invalida\n')
        menu_inicio()
    menu_inicio()


def menu_principal(torneo):
    if torneo.dias_transcurridos == torneo.dias_totales:
        input_usuario = imprimir_menu_termino(torneo.dias_totales,
                                              torneo.metros_cavados,
                                              torneo.meta)
        if input_usuario == '1':
            guardar_partida(torneo)

        elif input_usuario == '2':
            return

        elif input_usuario in ['x', 'X']:
            print('\nCerrando programa...\n')
            exit()

    else:
        input_usuario = imprimir_menu_principal(torneo.dias_transcurridos,
                                                torneo.arena.tipo,
                                                torneo.dias_totales)
        if input_usuario in ['1', '2', '3']:
            opciones_usuario = {'1': accion_1, '2': accion_2, '3': accion_3}
            opciones_usuario[input_usuario](torneo)
        elif input_usuario == '4':
            guardar_partida(torneo)
        elif input_usuario == '5':
            return
        elif input_usuario in ['x', 'X']:
            print('\nCerrando programa...\n')
            exit()
        else:
            print('\nOpcion invalida\n')
        menu_principal(torneo)


menu_inicio()
