# Juego de Adivinanza en Binario:
# Muestren un número en binario y desafíen al usuario a adivinar su
# equivalente decimal, o viceversa, reforzando la conversión entre ambos sistemas.

import random

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