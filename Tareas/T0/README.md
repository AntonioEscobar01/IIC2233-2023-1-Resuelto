# Tarea 0: DCCeldas 💣🐢🏰

## Consideraciones generales:

* La tarea se completó en su totalidad, sin tomar en cuenta los puntos de bonus.
* Ambos menús funcionan a prueba de errores de usuario siguiendo las instrucciones dadas de que hacer en caso de que se coloque un input inválido.
* Se completaron todas las funciones pedidas y se agregaron funciones extra para simplificar la resolucion de la tarea, que hace cada una de estas esta explicado con un comentario junto a ellas.
* Para solucionar los tableros se ocupo una solucion de estilo backtraking, esta soluciona tableros de cualquier dimensión, pero al estos ser de un tamaño mayor que 4x4 el programa tarda bastante pero lo resuelve de todas formas si se deja el tiempo suficiente para que lo resuelva.
* El programa es portable a diferentes sistemas operativos.
* Para ejecutar la tarea de manera correcta se debe estar en la carpeta T0 de mi repositorio.

-------

## Cosas implementadas y no implementadas:

- ❌  **NO** completé lo pedido
- ✅ si completé **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Menú de Inicio
##### ✅ Seleccionar Archivo
##### ✅ Validar Archivos
#### Menú de Acciones
##### ✅ Opciones
##### ✅ Mostrar tablero 
##### ✅ Validar bombas y tortugas
##### ✅ Revisar solución
##### ✅ Solucionar tablero
##### ✅ Salir
#### Funciones
##### ✅ Cargar tablero
##### ✅ Guardar tablero
##### ✅ Valor bombas
##### ✅ Alcance bomba
##### ✅ Verificar tortugas
##### ✅ Solucionar tablero
#### General: 
##### ✅ Manejo de Archivos
##### ✅ Menús
##### ✅ tablero.py
##### ✅ Módulos
##### ✅ PEP-8
#### Bonus:
##### 🟠 Funciones atómicas
##### - Todas las funciones del programa tienen entre 15 lineas o menos a exepción de la funcion solucionar tablero que tiene 17 lineas.
##### ❌ Regla 5

-------

## Ejecución:
El módulo principal de la tarea a ejecutar es  ```main.py```. No se creo ningún modulo extra ademas del modulo principla, de todas maneras este se encuentra en:
1. ```main.py``` en ```AntonioEscobar01-iic2233-2023-1\Tareas\T0\```

### Se utilizaron los modulos entregados para la tarea sin la necesidad de agregar adicionales a estos, de todas formas estos modulos son los siguientes:



1. ```functions.py```
2. ```tablero.py```

-------

## Librerías:
### Librerías externas utilizadas
Solo se utilizó una libreria para la resolución del juego, de todos modos esta fue utilizada en las siguientes funciones:

1. ```os```: [```  menu_inicio() / main.py  ``` | ``` cargar_tablero() / functions.py``` |  ``` guardar_tablero() / functions.py    ```]

-------

## Supuestos y consideraciones adicionales:
Los supuestos que realicé durante la tarea son los siguientes:

1. Todo archivo que contenga los tableros tiene como extension un '.txt', ya que no se especifica cual va a ser siempre la extension de los archivos por lo que se asume que es esta.
2. Al ingresar un archivo para abrir en el menu de inicio se debe escribir la extension correspondiente, en este caso '.txt'. Por ejemplo si se quiere abrir el archivo de 3x3 se debe escribir '3x3.txt'.
3. Se asume que todo archivo a leer tiene el formato indicado y este no presenta otra forma de escribirse ni otros caracteres dentro de el mismo.
4. Al tomar en cuenta la regla 3, como se asume que un tablero siempre se entrega con el formato explicado, es decir solo viene con los caracteres 'T' '-' 'Numero', y tomando en cuenta que mi estilo de solución nunca va a colocar una tortuga sobre un número, se asume que esta regla siempre se cumple y es por esto que no se definió ninguna función en específico para revisar esta regla a diferencia de la regla 1,2 y 4.

PD: Recordar que si bien el programa resuelve cualquier tamaño de tablero, si pasa de 4x4 comienza a tardar bastante en hacerlo (resolver un tablero de 8x8 tomo casi 2 horas), si se va a intentar resolver un tablero de mayor tamaño que 4x4 es necesario correr el programa desde una terminal ya que si se intenta correr en visualstudio o en algun editor de codigo aprecera que se exedio el limite de recursion maxima, a menos que se altere este valor lo cual no recomiendo.


-------

## Referencias de código externo :

* No se copio textualmente de ningun sitio web alguna parte del codigo, pero para la creación de la función que soluciona el tablero se utilizo un algoritmo estilo backtraking el cual lei de un libro. El link del libro y el lugar donde se utilizo este algoritmo es el siguiente:
1. \<https://www.amazon.com/-/es/Adnan-Aziz/dp/1537713949/ref=sr_1_3?keywords=python+interview+book&qid=1679688715&sprefix=python+int%2Caps%2C207&sr=8-3>:  este soluciona el tablero o bien indica que no tiene solución y está implementado en el archivo <functions.py> en las líneas <62-79> y hace funciona de tal manera que prueba todas las combinaciones posibles para posicionar tortugas dentro del tablero hasta encontrar uno valido y en caso de no encontrar ninguno es que este no posee solución alguna.
