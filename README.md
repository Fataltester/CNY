# Librería números complejos
## Librería de complejos
La librería tiene como título "lbCplx.py" el archivo incluye las 8 funciones solicitadas en la tarea, vamos a explicar el funcionamiento de cada una.
### función "sum_cplx"
Esta función recibe dos tuplas, las cuales son los números complejos,  lo único que realiza el programa es sumar las partes reales y almacenar el resultado en la variable "real", también sumamos las partes imaginarias y la almacenamos en "img".
La función retorna la tupla del real con el imaginario.
### función "prod_cplx"
La función recibe los dos números complejos, la variable "real" calcula la diferencia del producto entre las partes reales y las partes imaginarias, la variable "img" calcula la suma de los productos entre una parte real y otra imaginaria.
La función retorna una tupla con la variable "real" y "img".
### función "diff_cplx"
La función recibe las dos tuplas, realiza el mismo proceso que la función "sum_cplx" solo que resta las partes reales y las partes imaginarias entre ellas, retornando la parte real y la imaginaria como una tupla.
### función "div_cplx"
La función recibe dos tuplas, calculamos la parte real y la imaginaria, almacenando el resultado en "real" y "img" respectivamente.
La función retorna una tupla con "real" y "img".
### función "modulo"
La función recibe una tupla, calcula el modulo del número complejo y lo almacena en la variable "result" la cual también será retornada.
### función "conju"
La función recibe una tupla, retorna el conjugado cambiando el valor de la posición uno de la tupla multiplicando por -1.
### función "faseCplx"
La función recibe una tupla, calcula la fase del número complejo por medio de la función "math.atan" la cual pertenece a la librería **math** de python, el resultado se almacena a la variable "fase" y después es retornada.
### función "ctr_plr"
La función recibe una tupla, pasa de la representación cartesiana a la polar utilizando la función **modulo** y **fase** previamente definidas, hacemos uso de la función "iden_cuad" para identificar en que cuadrante se encuentra el número, después usamos un cuadro de condicionales que depende del resultado de "iden_cuad", esto para hallar el ángulo.
La función retorna una tupla que representa el mismo número complejo en coordenadas polares.
### función "iden_cuad"
La función es simplemente un soporte para **ctr_plr** con el objetivo de identificar en que cuadrante se encuentra el número complejo, es un cuadro de cuatro condicionales que verifican si las coordenadas son positivas o negativas, dependiendo de eso, retorna en que cuadrante se encuentra el número.
### función "plr_crt"
La función recibe una tupla, pasa de la representación polar y la cartesiana almacenando los resultados en las variables "real" y "img", el calculo se apoya en las funciones "math.cos" y "math.sin" provenientes de la librería **math** de python.
La función retorna el mismo número complejo en representación cartesiana
## Test de la Librería
El archivo "tstCplx.py" contiene todos los test a la librería "lbCplx.py" por medio de la librería **unittest** de Python, por cada función de la librería realizamos dos pruebas, para saber que test pertenece a las funciones, cada función de test lo hemos nombrado como "test_nombre de la función".
