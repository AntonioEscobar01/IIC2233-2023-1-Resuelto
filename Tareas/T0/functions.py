import os


def cargar_tablero(nombre_archivo: str) -> list:
    ruta = os.path.join('Archivos', nombre_archivo)
    with open(ruta, 'r') as archivo_cargar:
        lineas_archivo = archivo_cargar.readline()
        largo_tablero = int(lineas_archivo[0])
        lineas_archivo = lineas_archivo.split(',')[1:]
    return [lineas_archivo[index:index + largo_tablero]
            for index in range(0, len(lineas_archivo), largo_tablero)]


def guardar_tablero(nombre_archivo: str, tablero: list) -> None:
    largo_tablero = len(tablero)
    texto_escribir = str(largo_tablero) + ','
    ruta = os.path.join('Archivos', nombre_archivo)
    for linea in tablero:
        texto_escribir += ','.join(linea) + ','
    with open(ruta, 'wt') as archivo_escribir:
        archivo_escribir.write(texto_escribir[: len(texto_escribir)-1])


def verificar_valor_bombas(tablero: list) -> int:
    tamaño_tablero = len(tablero)
    bombas = list()
    for linea in tablero:
        for elemento in linea:
            if elemento not in ['-', 'T']:
                bombas.append(int(elemento))
    bombas_invalidas = [bomba for bomba in bombas if bomba > ((2 * tamaño_tablero) - 1)]
    return len(bombas_invalidas)


def verificar_alcance_bomba(tablero: list, coordenada: tuple) -> int:
    elemento_tablero = tablero[coordenada[0]][coordenada[1]]
    if elemento_tablero in ['-', 'T']:
        return 0
    else:
        fila_elemento = tablero[coordenada[0]]
        columna_elemento = [fila[coordenada[1]] for fila in tablero]
        alcance = contar_casillas(fila_elemento, coordenada[1])
        alcance += contar_casillas(columna_elemento, coordenada[0])
    return alcance + 1


def verificar_tortugas(tablero: list) -> int:
    cantidad_tortugas_invalidas = 0
    for numero_fila, fila_elemento in enumerate(tablero):
        for numero_columna, elemento in enumerate(fila_elemento):
            if elemento == 'T':
                columna_elemento = [fila[numero_columna] for fila in tablero]
                contiguas_horizontales = revisar_celdas_vecinas(
                    fila_elemento, numero_columna)
                contiguas_verticales = revisar_celdas_vecinas(
                    columna_elemento, numero_fila)
                if contiguas_horizontales is True or contiguas_verticales is True:
                    cantidad_tortugas_invalidas += 1
    return cantidad_tortugas_invalidas


def solucionar_tablero(tablero: list) -> list:
    if verificar_solucion(tablero):
        return tablero
    for fila in range(0, len(tablero)):
        for columna in range(0, len(tablero)):
            if tablero[fila][columna] == '-':
                copia_seguridad = tablero[:]
                tablero[fila][columna] = 'T'
                if verificar_tortugas(tablero) == 0 and explosion_valida(tablero) is True:
                    tablero = solucionar_tablero(tablero)
                    if tablero is not None:
                        return tablero
                    else:
                        tablero = copia_seguridad
                        tablero[fila][columna] = '-'
                else:
                    tablero[fila][columna] = '-'
    return None


# Funciones definidas por mi

'''
Verifica que un tablero cumpla con la regla 1
'''


def verificar_regla_1(tablero: list) -> bool:
    todas_bombas_validas = True
    for posicion_fila in range(0, len(tablero)):
        for posicion_columna in range(0, len(tablero)):
            elemento_actual = tablero[posicion_fila][posicion_columna]
            coordenada_actual = (posicion_fila, posicion_columna)
            if elemento_actual not in ['-', 'T']:
                alcance_real = verificar_alcance_bomba(
                    tablero, coordenada_actual)
                alcance_actual = int(elemento_actual)
                if alcance_real != alcance_actual:
                    todas_bombas_validas = False
    return todas_bombas_validas


'''
Cuenta las casillas que afecta una bomba en una fila o columna dependiendo de cual se ingrese
'''


def contar_casillas(lista_contar: list, posicion: int) -> int:
    cantidad_casillas = 0
    for posicion_atras in reversed(range(0, posicion)):
        if lista_contar[posicion_atras] != 'T':
            cantidad_casillas += 1
        else:
            break
    for posicion_adelante in range(posicion+1, len(lista_contar)):
        if lista_contar[posicion_adelante] != 'T':
            cantidad_casillas += 1
        else:
            break
    return cantidad_casillas


'''
Revisa si a los lados de una celda hay otra tortuga
'''


def revisar_celdas_vecinas(lista_revisar: list, posicion: int) -> bool:
    tortugas_contiguas = False
    if (posicion + 1) < len(lista_revisar):
        if lista_revisar[posicion + 1] == 'T':
            tortugas_contiguas = True
    if (posicion - 1) >= 0:
        if lista_revisar[posicion - 1] == 'T':
            tortugas_contiguas = True
    return tortugas_contiguas


'''
Verifica si el tablero ingresado es una solucion valida
'''


def verificar_solucion(tablero: list) -> bool:
    alcance_valido = verificar_regla_1(tablero)
    bombas_invalidas = verificar_valor_bombas(tablero)
    tortugas_invalidas = verificar_tortugas(tablero)
    if alcance_valido is True and bombas_invalidas == 0 and tortugas_invalidas == 0:
        return True
    else:
        return False


'''
Verifica que una bomba solo afecte a un numero igual o mayor a ella pero no menor
'''


def explosion_valida(tablero: list) -> bool:
    todas_bombas_validas = True
    for posicion_fila in range(0, len(tablero)):
        for posicion_columna in range(0, len(tablero)):
            elemento_actual = tablero[posicion_fila][posicion_columna]
            coordenada_actual = (posicion_fila, posicion_columna)
            if elemento_actual not in ['-', 'T']:
                alcance_real = verificar_alcance_bomba(
                    tablero, coordenada_actual)
                alcance_actual = int(elemento_actual)
                if alcance_real < alcance_actual:
                    todas_bombas_validas = False
    return todas_bombas_validas


if __name__ == "__main__":
    tablero_2x2 = [
        ['-', 2],
        ['-', '-']
    ]
    resultado = verificar_valor_bombas(tablero_2x2)
    print(resultado)  # Debería ser 0

    resultado = verificar_alcance_bomba(tablero_2x2, (0, 1))
    print(resultado)  # Debería ser 3

    tablero_resuelto = solucionar_tablero(tablero_2x2)
    print(tablero_resuelto)

    tablero_2x2_sol = [
        ['T', 2],
        ['-', '-']
    ]

    resultado = verificar_alcance_bomba(tablero_2x2_sol, (0, 1))
    print(resultado)  # Debería ser 2

    resultado = verificar_tortugas(tablero_2x2_sol)
    print(resultado)  # Debería ser 0
