# Tarea 3: DCCACHOS


Por motivos de tiempo la tarea no fue completada en su totalidad, si se logro montar el servidor y que se logren conectar clientes a este, ademas se realizo de forma completa el sistema de manejo de bytes con la serializacion, codificiacion y encriptacion correspondiente. Finalmente se crearon las ventanas de inicio y de juego pero mostrando todos los elementos pedidos. En la ventana de inicio estos elementos en parte si funcionan a diferencia de la ventana de juego donde solo se lograron crear pero no se llegaron a utilizar.


## Consideraciones generales:


- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores


#### Networking: 18 pts (16%)
##### ✅ Protocolo, se utiliza TCP/IP
##### ✅Correcto uso de sockets, se instancian y conectan los sockets de manera correcta, tanto en el servidor como en el cliente. El servidor puede escuchar simultaneamente a los clientes dado que se utilizan threads.
##### ✅ Conexión, la conexion se sostiene durante el tiempo logrando intercambiar diversos mensajes
##### 🟠 Manejo de Clientes, se pueden conectar hasta 4 clientes, luego de eso se logran conectar los clientes pero puede generar un error.
##### ✅ Desconexión Repentina, las desconecciones repentinas son atrapadas y manejadas con exepciones
#### Arquitectura Cliente - Servidor: 18 pts (16%)
##### ✅ Roles, el servidor y el cliente estan correctamente divididos, el cliente solo le corresponde actualizar la Ui mientras que el servidor se encarga de todo lo demas.
##### 🟠 Consistencia, se mantiene coordinada la informacion durante el transcurso del programa pero no se utilizan locks ya que para lo que se logro realizar de la tarea no fue necesario.
##### ✅ Logs, dentro de la terminal del servidor se presentan logs que explican que esta pasando con este en cada accion que se realiza.
#### Manejo de Bytes: 26 pts (22%)
##### ✅ Codificación
##### ✅ Decodificación
Tanto para codificar como para decodificar existe una funcion dentro de el archivo cripto.py que realiza esta accion cumpliendo lo pedido segun el enunciado.
##### ✅ Encriptación
##### ✅ Desencriptación
Tanto para encriptar como para desencriptar existe una funcion dentro de el archivo cripto.py que realiza esta accion cumpliendo lo pedido segun el enunciado.
##### ✅ Integración
Todas las funciones dentro del archivo cripto.py son utilizadas para el intercambio de bytes entre el cliente y el servidor.
#### Interfaz Gráfica: 22 pts (19%)
##### ✅ Ventana de Inicio, se creo la ventana de inicio con todos sus elementos pedidos, el boton de salir y comenzar funcionan correctamente
##### 🟠 Ventana de juego, se creo la ventana de juego con todos los elementos pedidos, pero estos no realizan ningun tipo de accion.
#### Reglas de DCCachos: 22 pts (19%)
##### ❌ Inicio del juego
##### ❌ Bots
##### ❌ Ronda
##### ❌ Termino del juego
No se implemento ninguna de estas funcionalidades
#### Archivos: 10 pts (9%)
##### ✅ Parámetros (JSON), existe y se utiliza correctamente un archivo de parametros en formato json
##### ✅ main.py, ambas entidades, el cliente y el servidor, poseen un archivo main.py, estos aceptan por la terminal tanto el puerto que se quiere utilizar, como el host, si no se coloca host se asume que se utiliza localhost, y para el puerto si no se entrega ninguno se utiliza uno predefinido.
##### ✅ Cripto.py, el archivo cripto contiene todas las funciones necesarias para el manejo de bytes, se crearon dos de estos archivos identicos uno para el servidor y otro para el cliente.
#### Bonus: 4 décimas máximo
##### ❌ Cheatcodes
##### ❌ Turno con tiempo

## Ejecución :computer:
Para ejecutar la tarea esta, el servidor debe ser ejecutado en:
1. ```main.py``` en ```servidor\```

Por otra parte los clientes deben ser ejecutados desde:

1. ```main.py``` en ```cliente\```



## Librerías:
La lista de librerías externas que utilicé fue la siguiente:

1. ```sockets```
2. ```pyqt5```
3. ```random```
4. ```json```
5. ```sys```
6. ```os```
7. ```threading```


## Supuestos y consideraciones adicionales:
Los supuestos que realicé durante la tarea son los siguientes:

1. Para la correción del archivo cripto, el test que viene colocado abajo no necesariamente funciona, esto porque la ruta del archivo de parametros es relativa a si este se corre desde el main y no directamente desde el archivo cripto por lo que este va a marcar un error.
2. Dentro de la carpeta ```frontend\``` se debe agregar la carpeta ```Sprites\```, con todos los sprites mencionados en el enunciado
-------


## Referencias de código externo:

La arquitectura del servidor y del cliente esta basada en la ayudantia de networking, por lo que la estructura es muy similar a la de esa ayudantia.

