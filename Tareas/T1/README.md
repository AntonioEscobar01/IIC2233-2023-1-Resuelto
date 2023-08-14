# Tarea 1: DCCavaCava 🏖⛏

La tarea fue completada en su totalidad y contiene todas las funcionalidades pedidas. Para cumplir con el maximo de lineas por modulo, el programa se divido en distintos modulos (Arena.py, Excavador.py, funciones.py, Items.py, main.py, Parametros.py, torneo.py), cada uno con funcionalidades especificas. Para lograr la resolución de la tarea, esta se dividio en una estructura de diferentes clases con sus respectivos metodos los cuales permiten que la tarea se ejecute.

## Consideraciones generales:

La tarea realiza todo lo pedido a excepción del bonus el cual no fue aplicado, dentro de esta no es posible botar el programa por algun tipo de error de usuario, el programa va a saber que hacer incluso en el caso de que no existan archivos a cargar al momento de cargar una partida, tomar en cuenta que estos no se encuentran dentro del repositorio segun lo pedido por lo que deberan ser agregados dentro de la carpeta T1 para poder jugar.

### Cosas implementadas y no implementadas:

- ❌ si **NO** completé lo pedido
- ✅ si completé **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores


#### Programación Orientada a Objetos: 42 pts (35%)
##### ✅ Diagrama
##### ✅ Definición de clases, atributos, métodos y properties
##### ✅ Relaciones entre clases
##### Se realizo un diagrama que representa las clases utilizadas por el programa, donde se puede apreciar cuales son las clases abstractas, quien hereda de quien, atributos, metodos, etc. Más sobre que clase es de que tipo en el punto entidades.
#### Preparación programa: 11 pts (9%)
##### ✅ Creación de partidas
##### Al momento de jugar una nueva partida se instancian los objetos de los archivos csv y se crea un objeto de la clase torneo desde 0, es decir no toma en cuenta partidas jugadas anteriormente. Torneo es instanciado con una arena inicial al azar mientras esta cumpla con el parametro del tipo de la arena inicial, los excavadores tambien son seleccionados al azar y la cantidad de estos esta dada por el parametro cantidad de excavadores iniciales.
#### Entidades: 22 pts (18%)
##### ✅ Excavador
##### Dentro del modulo creado excavador se encuentran definidas 4 clases: Excavador, ExcavadorTareo, ExcavadorDocencio y ExcavadorHibrido. Excavador es una clase abstracta de la cual heredan los otros 3 excavadores, Excavador no fue definido con todos los atributos que tienen las otras 3 clases por la forma en la que se programaron las propertys, hay una forma de que estas hereden estas propertys directamente desde Excavador pero dejaba el modulo en más de 400 lineas y para no tener que agregar un modulo más se realizo de esta forma para no agregar más complejidad. ExcavadorHibrido podría haber heredado de ExcavadorDocencio y ExcavadorTareo pero al producirse un error de multiherencia hubiera tenido que alargar más el modulo para solucionar este problema por lo que solamente hereda de Excavador, nuevamente esto se realizo así para evitar alargar de más el programa ya que con este acercamiento tambien funciona correctamente, de todas formas cumple con lo pedido dentro del enunciado.
##### ✅ Arena
##### Dentro del modulo Arena se encuentran 5 clases, la clase abstracta Arena (de la cual heredan las otras 4 clases), ArenaNormal, ArenaRocosa y ArenaMojada, las cuales todas heredan de Arena y finalmente ArenaMagnetica, la cual presenta una multiherencia de ArenaMojada y ArenaRocosa.
##### ✅ Torneo
##### Dentro del modulo torneo se encuentra definida la clase Torneo, esta posee todos los metodos pedidos ademas de dos agregados por mi, los cuales son: arenas_disponibles y excavadores_disponibles. Estos dos atributos son listas representan todos las arenas disponibles dentro del archivo arenas.csv (estas ya instanciadas como objetos), esto para cuando sea necesario cambiar de arena busque una dentro de esta lista. Por otra parte, excavadores_disponibles son todos los excavadores que existen dentro del archivo excavadores.csv, de esta lista es cuando de ser necesario se buscara un nuevo excavador para agregar al equipo. No se agrego un atributo eventos ya que los eventos que pueden ocurrir fueron manejados directamente en el metodo iniciar_evento().
#### Flujo del programa: 31 pts (26%)
##### ✅ Menú de Inicio
##### ✅ Menú Principal
##### Ambos menus son aprueba de errores de usuario, utilizando if en los casos mas simples para no agregar complejidad inecesariamente , y en los casos necesarios se utlizaron excepciones para el manejo de estos inputs. Ambos menus funcionan de manera recursiva para simplificar el movimiento entre menus.
##### ✅ Simulación día Torneo
##### Siendo esta la opcion 1 del menu principal, esta llama al metodo Simular_dia() de la clase Torneo, este metodo se encarga de la interacción entre todas las entidades del programa. Una vez terminada la simulación se vuelve al menu principal a menos que se termine el torneo, en ese caso el programa se dirige al menu de termino que permite guardar la partida o salir del programa, en caso de guardar la partida el programa vuelve al menu de inicio.
##### ✅ Mostrar estado torneo
##### Muestra el estado actual tanto de los atributos del torneo, como los atributos de cada excavador en el equipo.
##### ✅ Menú Ítems
##### Muestra los items dentro del atributo mochila, que es una lista con todos los elementos de tipo item que se obtienen en ese momento. Ademas muestra los atributos de todos estos items. En caso de que no se tenga ningun item esto sera mostrado.
##### ✅ Guardar partida
##### Por medio de un archivo txt se puede guardar la partida en todo momento, incluso una vez terminado el torneo (si eso ocurre y luego se carga esta partida, de forma inmediata se mostrara que finalizo el torneo). Las partidas se guardan en el archivo DCCavaCava.txt, de no existir el archivo se creara uno o en el caso de que si exista se sobreescribira la partida existente.
##### ✅ Robustez
##### Por medio de uso de excepciones e if de control de usario, si se respetan todos los supuestos, el programa no tiene posibilidad de caerse.
#### Manejo de archivos: 14 pts (12%)
##### ✅ Archivos CSV 
##### Una funcion dentro del modulo funciones es encargada de leer y proporcionar de manera correcta la información dentro de los archivos csv.
##### ✅ Archivos TXT
##### El archivo DCCavaCava.txt es el unico archivo de texto utilizado, este es manipulado por dos funciones dentro del modulo funciones (guardar_partida(), cargar_partida()), con el objetivo de poder guardar partidas o cargar una partida previa.
##### ✅ parametros.py
##### Este archivo contiene todos los parametros pedidos dentro del enunciado, cada uno del tipo de dato pedido. Este archivo DEBE existir junto con todos los parametros dentro del y con esos nombres, esto para el correcto funcionamiento del programa.
#### Bonus: 3 décimas máximo
##### ❌ Guardar Partida

## Ejecución:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe agregar los siguientes archivos para que el programa funcione:
1. ```arenas.csv``` en ```\T1```
2. ```consumibles.csv``` en ```\T1```
3. ```excavadores.csv``` en ```\T1```
4. ```tesoros.csv``` en ```\T1```


## Librerías:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```random(), randint() / módulos: Torneo, Excavador, Arena, funciones```
2. ```abc```: ```ABC, abstractmethod / módulos: Arena, Items, Excavador``` 
3. ```os```: ```path() / módulos Funciones``` 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```torneo```: Contiene a ```Clase Torneo``` y sus respectivos metodos.
2. ```Arena```: Contiene a ```Clase Arena```, ```Clase ArenaNormal```, ```Clase ArenaMojada```, ```Clase ArenaRocosa```, ```Clase ArenaMagnetica``` y sus respectivos metodos.
3. ```Excavador```: Contiene a ```Clase Excavador ```, ```Clase ExcavadorDocencio```, ```Clase ExcavadorTareo```, ```Clase ExcavadorHibrido``` y sus respectivos metodos.
4. ```Items```: Contiene a ```Clase Item```, ```Clase Consumible```, ```Clase Tesoro``` y sus respectivos metodos.
5. ```parametros```: Contiene a todos los parametros pedidos dentro del enunciado.
6. ```funciones```: Contiene funciones utilizadas durante el progreso del programa tales como leer archivos, guardar archivos, imprimir menus, etc.

## Supuestos y consideraciones adicionales:
Los supuestos que realicé durante la tarea son los siguientes:

1. Un excavador que esta descansando no puede encontrar un item ya que este no participo durante el día.
2. Siempre va a existir al menos una arena de cada tipo en el archivo arenas.csv ya que al momento de querer cambiar de arena asumo que existe otra con las caracteristicas a buscar.
3. Tomar en consideración que al momento de imprimir tanto los nombres de los excavadores y los nombres de los items en sus respectivas tablas, para mejorar la apariencia de estas tablas estos se cortan si es que se pasan de un cierto largo (en el caso de los nombres de los excavadores son 10 caracteres y en el caso de los items son 19 caracteres) para que quepan dentro del formato indicado en el enunciado.
4. Los archivos csv se presentan en el formato indicado en el enunciado y no de otra forma ya que de ser asi el programa no va a funcionar correctamente.
5. Encontar un item en una arena no significa que este no pueda ser encontrado nuevamente, dado que no se especifica dentro del enunciado, al momento de encontrar un item A, los excavadores pueden volver a encontrar este mismo item A en esa arena. Ademas todas las arenas tienen los mismos items posibles a encontrar ya que cuales son los items de cada arena tampoco estaba explicitamente dentro del enunciado.
6. En caso de que un tesoro intente agregar un nuevo excavador al equipo pero no existen mas excavadores en el archivo entregado, se asume que no se pueden agregar mas al equipo y se notifica por la consola. Esto debido a que este caso no se especifica en el enunciado.
7. Para los items dentro de consumibles.csv y tesoros.csv y las arenas dentro de arenas.csv, se considera que el nombre de cada elemento es unico. Esto se asume para al momento de guardar una partida se guarda el nombre de cada elemento dentro del torneo para luego al momento de cargar la partida se busca la info de ese elemento en su respectivo archivo y se instancia para agregarlo a la mochila. Se realizo de esta forma para simplificar el guardar una partida y que esto no fue especificado dentro del enunciado.
8. Ningun nombre, descripcion, atributo de los elementos en los archivos csv inlcuyen caracteres especiales tales como (/, ;), ya que estos son utilizados para cargar partidas.
9. Se asume que el parametro de la cantidad de excavadores iniciales es mayor a 0 y menor o igual a la cantidad de excavadores presentes dentro del archivo excavadores.csv. Se asume que esto se cumple ya que de no ser así no se podría desarrollar el torneo.
10. El parametro dias totales torneo siempre va a ser un numero mayor a 0.
11. Los archivos csv nunca vendran vacios.
12. El archivo de texto DCCavaCava.txt solo sera creado por el programa en si y no se agregara uno con este nombre, esto dado que el formato de este archivo esta dado dentro del programa y de no ser ese formato el archivo sera leido erroneamente.


##### <PD: Dentro de los modulos se aprecia que ciertos strings dentro de algunos prints no cumplen con la indentación que uno creeria, esto se realizo de esa manera para cumplir con el formato pedido de PEP8>
-------

## Referencias de código externo:

Para la realización de la tarea no se utilizo codigo externo, solo fue utilizado conocimiento propio y materia pasada del curso en los notebooks de contenidos.

