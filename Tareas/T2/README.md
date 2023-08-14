# Tarea 2: DCCazafantasmas 👻🧱🔥



## Consideraciones generales:

La tarea fue completada en su totalidad y contiene todas las funcionalidades pedidas. Para cumplir con el maximo de lineas por modulo, la ventana de juego se dividio en 2 ventanas, ventana constructor y ventana de juegp. cada ventana de juego tiene su propio backend y todas las señales estan conectadas en el modulo ```main.py```. La tarea no presenta bugs al momento de jugar mientras se respeten todas las consideraciones mencionadas más adelante.
### Cosas implementadas y no implementadas:


- ❌ si **NO** completé lo pedido
- ✅ si completé **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores


#### Ventanas: 27 pts (27%)
##### ✅ Ventana de Inicio : La ventana de inicio muestra todos los elementos pedidos, ordenados dentro de esta. La ventana de inicio tiene su propio backend ```logica_inicio.py```, esta solo revisa que el nombre de usuario sea valido segun lo pedido en el enunciado (``` linea 13 en logica_inicio.py```), en caso de no ser asi se notifica mediante un popup (``` linea 72 en ventana_inicio.py```) y no se permite comenzar el juego hasta que el nombre cumpla con las condiciones pedidas. Los mapas se seleccionan en el ComboBox presente en la ventana de inicio (``` linea 44 en ventana_inicio.py```), una vez seleccionado un mapa e ingresado un nombre de usuario valido al presionar jugar se envia una señal para comenzar el juego (``` linea 94 en ventana_inicio.py```), si fue seleccionado el modo constructor se abre la ventana constructor, si se eligio un mapa se abre la ventana de juego. El boton cerrar envia una señal para cerrar la ventana y terminar el juego.
##### ✅ Ventana de Juego: La ventana de juego presenta todos los elementos pedidos, estos no se superponen entre si. Las estadisticas ```Vidas``` y ```Tiempo``` se actualizan mientras avanza el juego (``` linea 267 en logica_juego.py y linea 275 en logica_juego.py ```). El modo constructor fue separado a una ventana aparte a la ventan de juego por lo que esta se inicia solo cuando se elige un mapa ya creado desde la ventana de inicio o cuando se presiona jugar dentro de la ventana constructor (``` linea 40 en ventana_constructor.py```). Como no fue pedido un boton salir para la ventana de juego dentro del enunciado la unica forma de salir es cerrar la pestaña de juego o bien, ganar o perder el juego, cuando eso pase se abre un pop-up con la informacion correspondiente y un boton ```Salir``` el cual envia una señal para cerrar el juego (``` linea 305 en ventana_juego.py y linea 317 en ventana_juego.py```).
#### Mecánicas de juego: 47 pts (47%)
##### ✅ Luigi: Luigi detecta las colisiones con cualquiera de las otras entidades y responde correctamente dependiendo de con que entidad colisiono (``` linea 99 en logica_juego.py```), pierde una vida si choca con fuego o con un fantasma y para cualquiera de estos se reinicia el nivel, al colisionar con una pared o con los bordes del mapa luigi no puede seguir avanzando, si colisiona con una roca este puede arrastrarla mientras la siguiente casilla este vacia para que la ocupe la roca. El movimiento de luigi es mediante las teclas WASD (``` linea 111 en ventana_juego.py```), al momento de que una de estas sea presionada la ventana de juego envia una señal a ```logica_juego.py``` donde esta determina que hacer en cada caso. Para mejorar la jugabilidad, luigi se mueve de a una casilla a la vez, es decir, cada vez que se presione una tecla (aunque esta se mantenga apretada) luigi se movera solo una casilla, si se suelta la tecla y se presiona nuevamente luigi se movera otra casilla mas, si luigi se esta moviendo de una casilla a otra durante ese intervalo de tiempo cualquier otra tecla no sera registrada. Esta forma de interaccion con las teclas es para mejorar la jugabilidad y que el usuario tenga claridad de donde esta y donde va a estar luigi en todo momento.
##### ✅ Fantasmas: La velocidad de los fantasmas se calcula aleatoriamente al comenzar cada juego (``` linea 43 en logica_juego.py```), esta velocidad es la misma para todos los fantasmas durante ese juego, esta velocidad determina cuanto tienen que esperar para moverse a la siguiente casilla. La ```logica_juego.py``` se encarga de determinar cuando se debe mover cada fantasma (``` linea 146 en logica_juego.py```) y le avisa al frontend hacia donde se debe mover cada uno. Los fantasmas se pueden traspasar entre si, al momento de que un fantasma colisiona con luigi este pierde una vida y el nivel comienza denuevo, los fantasmas cambian de direccion cuando chocan con una pared, borde o roca. Finalmente si un fantasma llega a tocar el fuego este desaparece, vuelve a aparecer si se reinica el nivel.
##### ✅ Modo Constructor: El modo constructor se creo como una ventana aparte para disminuir la extencion de cada modulo, el panel de construccion presenta todas las entidades que se pueden colocar y tambien presenta la cantidad maxima de elementos que se pueden colocar en el mapa (``` linea 30-36 en logica_constructor.py```). Al momento de colocar elementos, no se pueden colocar de estos dentro de la misma casilla, si se intenta hacer esto se notifica por medio de un pop-up que no es posible realizar esto. Mientras esta activa la ventana de constructor, ninguno de los elementos presenta movimiento o animacion alguna. El boton limpiar borra todos los elementos colocados en el mapa y el boton jugar envia una señal para iniciar el juego si solo si luigi y la estrella estan presentes dentro del mapa (``` linea 76 en logica_constructor.py```).
##### ✅ Fin de ronda: El juego termina en dos casos, si se gana o se pierde. Se puede ganar solo si se llega a la estrella y se presiona la letra G, en caso de ocurrir esto comienza la musica de ganar y se abrira un pop-up con un mesaje de felicitaciones, el nombre de usuario, y los puntos ganados durante la ronda los cuales son calculados segun la formula pedida en el enunciado, este calculo se realiza en  (``` linea 50 de funciones.py```). Se pierde cuando luigi se queda sin vidas o cuando se acaba el tiempo, para cualquiera de estos casos termina el juego y aparece un pop-up con un mensaje. Si se gana o se pierde, el pop-up correspondiente incluye un boton para salir del juego (``` linea 311 y 322 de funciones.py```).
#### Interacción con el usuario: 14 pts (14%)
##### ✅ Clicks: Al momento de estar en la ventana del constructor, para colocar cualquier elemento se debe presionar el boton correspondiente y luego hacer click sobre la casilla que se quiera colocar este elemento.
##### ✅ Animaciones: Las animaciones de luigi y los fantasmas son fluidas entre casilla y casilla. Luigi cambia de sprites cada vez que camina, los fantasmas cambian de sprites siempre que el juego no este en pausa.
#### Funcionalidades con el teclado: 8 pts (8%)
##### ✅ Pausa: Durante cualquier punto del juego en si se puede colocar pausa presionando el boton correspondiente o presionando la letra P, esto detiene todos los elementos del juego, incluyendo movimientos y animaciones. Tambien desactiva el teclado a excepcion de la tecla P para continuar con el juego cuando sea presionada (``` linea 284 de logica_juego.py```).
##### ✅ K + I + L: Mientras el juego no este en pausa, si se presionan las teclas ```K, I, L ``` al mismo tiempo sin importar el orden, se eliminaran todos los fantasmas del mapa. Por otra parte, si el nivel se reinicia porque luigi recivio daño por otra entidad, estos vuelven a aparecer ya que se reinicio el nivel (se decidio hacer de esta manera, no es un bug.). No obstante si esto pasa se puede volver a presionar esta combinacion y los fantasmas vuelven a desaparecer (``` linea 305 de logica_juego.py```).
##### ✅ I + N + F:  Mientras el juego no este en pausa, si se presionan las teclas ```I, N, F ``` al mismo tiempo sin importar el orden, se otorgaran vidas y tiempo infinito al jugador, esta opcion no es reversible, una vez presionado este cheatcode se mantendra con tiempo infinito y vidas infinitas hasta que se gane la ronda, dado que no se puede perder con esto activado la ronda solo termina si se llega a la estrella y se gana la partida (``` linea 298 de logica_juego.py```).
#### Archivos: 4 pts (4%)
##### ✅ Sprites: todos los sprites son utilizados donde corresponde dada uno.
##### ✅ Parametros.py: el modulo incluye todos los parametros pedidos dentro del enunciado, ademas de parametros creados por mi para el desarrollo de la tarea.
#### Bonus: 8 décimas máximo
##### ❌ Volver a Jugar
##### ❌ Follower Villain
##### ❌ Drag and Drop

## Ejecución:
El módulo principal de la tarea a ejecutar es  ```main.py```, el cual se encuentra en la carpeta de la tarea 2. Además se debe crear los assets en una carpeta con el nombre ```assets``` dentro de la carpeta ```Frontend```, las carpetas que deben ser creadas dentro de ```assets``` son:
1. ```sprites``` en la ubicacion ```frontend\assets\```, esta debe contener todos los elementos cargados en esta carpeta dentro del syllabus, con los mismos nombres de cada archivo.
2. ```mapas``` en la ubicacion ```frontend\assets\```, esta debe existir y puede contener cualquier mapa que es quiera cargar luego en el juego, mientras este sea un archivo txt respetando el formato que debe tener un mapa.
3. ```sounds``` en la ubicacion ```frontend\assets\```, esta debe contener todos los elementos cargados en esta carpeta dentro del syllabus, con los mismos nombres de cada archivo.


## Librerías:
Todas las librerias utilizadas estan dentro de las librerias permitidas y vienen instaladas con python a excepcion de ```Pyqt5```, que debe ser installada para el funcionamiento de la tarea. La lista de librerías externas que utilicé fue la siguiente:

1. ```Pyqt5```
2. ```random```
3. ```os```
4. ```sys```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones.py```: Contiene todas las funciones auxiliares que se utilizan dentro de la tarea, se realizo de esta forma para mejorar modularización y disminuir la extención de cada módulo.
2. ```parametros.py```: Contiene todos parametros a utilizar mencionados en el enunciado, ademas de todos los parametros que se consideraron necesarios crear para el desarrollo de la tarea, entre esto se encuentran rutas, tamaños, posiciones, etc.
3. ```entidades.py```: Contiene las 4 entidades que tienen gran cantidad de propiedades, estas son ```Luigi```, ```FantasmaV```, ```FantasmaH```, ```Roca```.

## Supuestos y consideraciones adicionales:
Los supuestos que realicé durante la tarea son los siguientes:

1. El tablero siempre va a ser de 16x11 casillas, incluyendo los bordes 
2. Los parametros dentro del modulo ```parametros.py``` que dicen no editar, no deben ser editados. Estos son parametros agregador por mi para el desarrollo de la tarea y estos no deben cambiar.
3. En la ventana de juego no aparecen los botones ```Jugar``` y ```Limpiar``` deshabilitados, como se habia pedido dentro del enunciado, esto porque en la tarea se separo la ```VentanaConstructor``` con la ```VentanaJuego```, por lo que colocar los botones dentro de la ventana de juego no hubiese tenido sentido.
4. Si un mapa guardado tiene mayor cantidad de elementos que los maximos definidos en los parametros, estos maximos seran ignorados y se cargara el mapa con todos los elementos que este pide.
5. Dado que no fue especificado que ocurre cuando un fantasma colisiona con una estrella, se asume que esto nunca va a ocurrir.
6. Luigi solo puede empujar una roca a la vez, por lo que si hay dos rocas juntas el no va a poder mover ambas.
7. Cuando se deja de mover luigi, el sprite con el que se queda es el ultimo que obtuvo durante la animación para moverse.

PD: Las ventanas de juego no se pueden agrandar ni achicar dado que el tamaño de esta si importa para ejecución de la tarea, dado que se calculan las posiciones 


-------

## Referencias de código externo:

Para la realización de la tarea no se utilizo codigo externo, solo fue utilizado conocimiento propio y materia pasada del curso en los notebooks de contenidos, experiencias y ayudantias.