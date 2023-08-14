import os

ANCHO_GRILLA = 11  # NO EDITAR
LARGO_GRILLA = 16  # NO EDITAR
GRILLA_X = 39      # NO EDITAR
GRILLA_Y = 36      # NO EDITAR
INICIO_X = 500     # NO EDITAR
INICIO_Y = 49      # NO EDITAR
# Complete con los demás parámetros

# Rutas
RUTA_FONDO = os.path.join(
    'frontend', 'assets', 'sprites', 'Fondos', 'fondo_inicio.png')
RUTA_MAPAS = os.path.join('frontend', 'assets', 'mapas')

RUTA_BORDES = os.path.join(
    'frontend', 'assets', 'sprites', 'Elementos', 'bordermap.png')

RUTA_LUIGI_RIGHT = [os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'luigi_rigth_1.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'luigi_rigth_2.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'luigi_rigth_3.png')]

RUTA_LUIGI_LEFT = [os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'luigi_left_1.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'luigi_left_2.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'luigi_left_3.png')]

RUTA_LUIGI_DOWN = [os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'luigi_down_1.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'luigi_down_2.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'luigi_down_3.png')]

RUTA_LUIGI_UP = [os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'luigi_up_1.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'luigi_up_2.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'luigi_up_3.png')]

RUTA_FV = [os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'red_ghost_vertical_1.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'red_ghost_vertical_2.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'red_ghost_vertical_3.png')]

RUTA_FHD = [os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'white_ghost_rigth_1.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'white_ghost_rigth_2.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'white_ghost_rigth_3.png')]

RUTA_FHL = [os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'white_ghost_left_1.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'white_ghost_left_2.png'),
    os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'white_ghost_left_3.png')]

RUTA_LOGO = os.path.join(
    'frontend', 'assets', 'sprites', 'Elementos', 'logo.png')

# Rutas modo constructor
RUTA_ICONO_LUIGI = os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'luigi_front.png')
RUTA_ICONO_LADRILLO = os.path.join(
    'frontend', 'assets', 'sprites', 'Elementos', 'wall.png')
RUTA_ICONO_ROCA = os.path.join(
    'frontend', 'assets', 'sprites', 'Elementos', 'rock.png')
RUTA_ICONO_ESTRELLA = os.path.join(
    'frontend', 'assets', 'sprites', 'Elementos', 'osstar.png')
RUTA_ICONO_FH = os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'white_ghost_rigth_1.png')
RUTA_ICONO_FV = os.path.join(
    'frontend', 'assets', 'sprites', 'Personajes', 'red_ghost_vertical_1.png')
RUTA_ICONO_FUEGO = os.path.join(
    'frontend', 'assets', 'sprites', 'Elementos', 'fire.png')

# Ruta musica
RUTA_MUSICA_GANAR = os.path.join(
    'frontend', 'assets', 'sounds', 'stageClear.wav')

RUTA_MUSICA_PERDER = os.path.join(
    'frontend', 'assets', 'sounds', 'gameOver.wav')


# Parametros numericos

# Cantidades de objetos iniciales
MAXIMO_FANTASMAS_VERTICAL = 3
MAXIMO_FANTASMAS_HORIZONTAL = 3
MAXIMO_PARED = 20
MAXIMO_ROCA = 5
MAXIMO_FUEGO = 3
CANTIDAD_ESTRELLA = 1   # NO EDITAR
CANTIDAD_LUIGI = 1      # NO EDITAR

# MIN Y MAXIMO DE CARACTERES DEL USERNAME
MIN_CARACTERES = 3
MAX_CARACTERES = 12

# Tiempo, vidas, multiplicador
CANTIDAD_VIDAS = 3
TIEMPO_CUENTA_REGRESIVA = 90   # En segundos
MULTIPLICADOR_PUNTAJE = 50

# Animaciones, mientras mas pequeño sea mas rapido cambian sus foto
FRAME_RATE_LUIGI = 30
FRAME_RATE_FANTASMAS = 100

# Velocidad fantasmas
MIN_VELOCIDAD = 1
MAX_VELOCIDAD = 2
