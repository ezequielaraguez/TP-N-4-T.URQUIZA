from random import *

#JUEGO "ADIVINA EL NUMERO"

#---Mostramos el Menu

print("""
Bienvenido al juego
Consta de elegir un numero correcto entre 1 y 100 elegido al azar.

Elige una opcion:

1-JUGAR

2-SALIR
    """)
OpcionIngresada=int(input("Ingrese una opcion= "))

#----Declaramos los parametros y hacemos la funcion que genera el numero correcto----
menor = 1
mayor = 100

def generanumero (menor, mayor):
    return randint(menor, mayor)

NumeroCorrecto = randint(menor, mayor)
