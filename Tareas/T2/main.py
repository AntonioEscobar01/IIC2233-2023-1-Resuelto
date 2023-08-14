from frontend.ventana_inicio import VentanaInicio
from backend.logica_inicio import VentanaInicioBackend
from frontend.ventana_constructor import VentanaConstuctor
from backend.logica_constructor import Constructor
from frontend.ventana_juego import VentanaJuego
from backend.logica_juego import Juego
from PyQt5.QtWidgets import QApplication
import sys


app = QApplication(sys.argv)

# Creamos entidades
ventana_inicio = VentanaInicio()
ventana_inicio_backend = VentanaInicioBackend()
constructor = VentanaConstuctor()
logica_constructor = Constructor()
ventana_juego = VentanaJuego()
logica_juego = Juego()

# Conectamos señales ventana inicio
ventana_inicio_backend.senal_mensaje_error.connect(ventana_inicio.pop_up_error)
ventana_inicio_backend.senal_empezar_juego.connect(ventana_inicio.empezar)
ventana_inicio.senal_verificar_usuario.connect(ventana_inicio_backend.verificar_usuario)
ventana_inicio.senal_empezar_constructor.connect(constructor.abrir_ventana)
ventana_inicio.senal_empezar_mapa.connect(logica_juego.empezar)

# Conectamos señales ventana constructor
constructor.senal_limpiar.connect(logica_constructor.limpiar_tablero)
constructor.senal_mouse_presionado.connect(logica_constructor.calcular_posicion_label)
constructor.senal_empezar.connect(logica_constructor.empezar)
logica_constructor.senal_posicion_label.connect(constructor.anadir_label)
logica_constructor.senal_casilla_ocupada.connect(constructor.pop_up_posicion_ocupada)
logica_constructor.senal_cerrar_ventana.connect(constructor.cerrar_ventana)
logica_constructor.senal_empezar_juego.connect(logica_juego.empezar)

# conectamos senales juego
ventana_juego.senal_teclas.connect(logica_juego.revisar_colisiones_luigi)
ventana_juego.senal_ganar.connect(logica_juego.ganar)
ventana_juego.senal_boton_pausa.connect(logica_juego.pausar_juego)
ventana_juego.senal_cheatcode_inf.connect(logica_juego.cheatcode_inf)
ventana_juego.senal_cheatcode_kil.connect(logica_juego.cheatcode_kil)
logica_juego.senal_mostrar_ventana.connect(ventana_juego.mostrar_ventana)
logica_juego.senal_mostrar_luigi.connect(ventana_juego.aparecer_luigi)
logica_juego.luigi.senal_actualizar_pixmap.connect(ventana_juego.lista_pixmap)
logica_juego.luigi.senal_mover_label.connect(ventana_juego.timer_mover_luigi.start)
logica_juego.luigi.senal_mover_label.connect(ventana_juego.timer_animacion_luigi.start)
logica_juego.luigi.senal_actualizar_label.connect(ventana_juego.actualizar_label_luigi)
logica_juego.senal_colocar_bloque.connect(ventana_juego.colocar_bloques)
logica_juego.senal_actualizar_vidas.connect(ventana_juego.cambiar_vidas)
logica_juego.senal_levantar_luigi.connect(ventana_juego.levantar)
logica_juego.senal_borrar_labels.connect(ventana_juego.borrar_labels)
logica_juego.senal_colocar_roca.connect(ventana_juego.colocar_roca)
logica_juego.senal_mover_roca.connect(ventana_juego.mover_roca)
logica_juego.senal_pop_ganar.connect(ventana_juego.pop_up_ganar)
logica_juego.senal_colocar_f.connect(ventana_juego.colocar_fantasmas)
logica_juego.senal_actualizar_tiempo.connect(ventana_juego.actualizar_tiempo)
logica_juego.senal_pop_perder.connect(ventana_juego.pop_up_perder)
logica_juego.senal_habilitar_teclas.connect(ventana_juego.bloquear_teclado)
logica_juego.senal_mover_fantasma.connect(ventana_juego.mover_fantasma)
logica_juego.senal_borrar_fantasma.connect(ventana_juego.borrar_fantasma)
logica_juego.senal_enviar_tiempo.connect(ventana_juego.set_tiempo_fantasmas)

sys.exit(app.exec())
