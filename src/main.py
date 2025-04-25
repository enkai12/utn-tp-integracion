# Juego de Adivinanza en Binario:
# Muestren un número en binario y desafíen al usuario a adivinar su
# equivalente decimal, o viceversa, reforzando la conversión entre ambos sistemas.

import random

numDecimal = random.randint(0, 255)
binario = ""

opcion = int(input("Ingresa '1' para jugar de Decimal a Binario. Ingresa '2' para jugar de Binario a Decimal: "))

if opcion == 1:

    # Conversor número decimal a número binario
    conversor = numDecimal
    while conversor > 0:
        if conversor % 2 == 0:
            binario = "0" + binario
        else:
            binario = "1" + binario
        conversor = conversor // 2

    # El usuario intentará adivinar ingresando el número binario
    numUsuario = -1
    while numUsuario != binario:
        numUsuario = str(input(f"Intenta adivinar el siguiente número decimal {numDecimal} en binario: "))
        if numUsuario == binario:
            print("¡Felicidades! Has adivinado el número en binario")
            print(f"El número decimal {numDecimal} es el número binario {binario}")
        else:
            print("Fallaste, vuelve a intentarlo")

elif opcion == 2:

#""" Explicación del código de lo que hicimos en la reunión:

#Genera un número aleatorio entre 0 y 15.

#Lo convierte en binario con una lista predefinida.

#Muestran el binario y pide al usuario adivinar el número decimal.

#Verifica si la respuesta es correcta o no. """

    binarios = ["0000", "0001", "0010", "0011",
        "0100", "0101", "0110", "0111",
        "1000", "1001", "1010", "1011",
        "1100", "1101", "1110", "1111"]

    bandera = True

    while bandera == True:
        print("JUEGO DE ADIVINANZAS")
        # Se asigna a la variable "numero" un número aleatorio entre 0 y 15
        numero = random.randint(0, 15)
        binario = binarios[numero]

        # Se muestra el binario
        print(f"Número binario mostrado: {binario}")

        # Pedimos una respuesta
        respuesta = int(input("Cuál sería el equivalente en decimal?: "))

        if respuesta == numero:
            print("Es Correcto!")
            bandera = False

        else:
            print(f"Incorrecto, la respuesta era: {numero}")
else:
    print("Error. Ingrese opción 1 o 2")