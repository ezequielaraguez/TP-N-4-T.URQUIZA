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

#----CONTADOR DE VIDAS
VIDAS=10

#----Declaramos los parametros y hacemos la funcion que genera el numero correcto----
menor = 1
mayor = 100

def generanumero (menor, mayor):
    return randint(menor, mayor)

NumeroCorrecto = randint(menor, mayor)

#Segun la opcion elegimos
if OpcionIngresada == 1:
    #Ingresamos el numero que nosotros elegimos.
    NumeroElegido = int(input("Ingresa un numero entre 1 y 100: "))

    #Una ayuda si el numero es mayor o menor al elegido
    if NumeroElegido > NumeroCorrecto:
        print("Es un numero menor al elegido.")
        VIDAS = int(VIDAS - 1)
        print("Te quedan ", VIDAS, " vidas.")
    elif NumeroElegido == NumeroCorrecto:
        print("Correcto Felicitaciones el numero es : ", NumeroCorrecto)
    else:
        print("El numero es mayor al elegido.")
        VIDAS = int(VIDAS - 1)
        print("Te quedan ", VIDAS, " vidas.")

    #Entra en un bucle que no va a salir hasta que sea el numero correcto
    while VIDAS > 0:
        print("Incorrecto intentalo de nuevo.")
        #Pedimos un numero si no es correcto
        NumeroElegido = int(input("Ingresa un numero entre 1 y 100: "))

        #Una ayuda si el numero es mayor o menor al elegido
        if NumeroElegido > NumeroCorrecto:
            print("Es un numero menor al elegido.")
            VIDAS = int(VIDAS - 1)
            print("Te quedan ", VIDAS, " vidas.")
        elif NumeroElegido == NumeroCorrecto:
            print("")
        else:
            print("El numero es mayor al elegido.")
            VIDAS = int(VIDAS - 1)
            print("Te quedan ", VIDAS, " vidas.")

else:
    print("Gracias por jugar. Chau")

if NumeroElegido == NumeroCorrecto:
    print("Correcto Felicitaciones el numero es : ", NumeroCorrecto)
else:
    print("GAME OVER")
