import random

binarios = ["0000", "0001", "0010", "0011",
    "0100", "0101", "0110", "0111",
    "1000", "1001", "1010", "1011",
    "1100", "1101", "1110", "1111"]

bandera = True
correctas =0 
intentos =0


while bandera == True:
    print("\nJUEGO DE ADIVINANZAS")
    # Se asigna a la variable "numero" un número aleatorio entre 0 y 15
    intentos+=1
    numero = random.randint(0, 15)
    binario = binarios[numero]

    # Se muestra el binario
    print(f"Número binario mostrado: {binario}")

    # Pedimos una respuesta
    respuesta = int(input("Cuál sería el equivalente en decimal?: "))

    if respuesta == numero:
        correctas+=1
        print("Es Correcto!\n")
        
    else:
        print(f"Incorrecto, la respuesta era: {numero}\n")

   
    if intentos % 3== 0: #Cada 3 intentos consulta si continua el juego
        continuar = input("¿Quieres seguir jugando? (s/n):").lower()
        if continuar != "s":
            bandera = False
            print("¡Gracias por jugar!")
            print(f"{correctas} respuestas correctas de {intentos} intentos")

  
