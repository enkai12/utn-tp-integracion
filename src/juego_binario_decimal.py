# Juego de Adivinanza en Binario:
# Muestren un número en binario y desafíen al usuario a adivinar su
# equivalente decimal, o viceversa, reforzando la conversión entre ambos sistemas.

import random

# Inicializamos las estadísticas
partidas = 0
aciertos = 0
bandera = True

print("========================================")
print("        JUEGO DE ADIVINANZAS BINARIAS")
print("========================================")

# Elegimos la cantidad de bits (solo 4, 6 u 8)
bits = 0
while bits != 4 and bits != 6 and bits != 8:
    entrada = input("Elegí la cantidad de bits (4, 6 u 8): ")
    if entrada.isdigit():
        bits = int(entrada)
        if bits != 4 and bits != 6 and bits != 8:
            print("Solo se permite 4, 6 u 8.")
    else:
        print("Entrada no válida. Ingresá un número.")

# Calculamos el valor máximo posible con esa cantidad de bits
max_valor = 2 ** bits - 1

# Bucle principal del juego
while bandera == True:
    print("\n¿En qué dirección querés jugar?")
    print("  b - Binario a Decimal")
    print("  d - Decimal a Binario")
    opcion = input("Elegí una opción (b/d): ").lower()

    if opcion == 'b':
        # BINARIO A DECIMAL
        numero_decimal = random.randint(0, max_valor)
        binario = bin(numero_decimal)[2:].zfill(bits)

        print("\n----------------------------------------")
        print(" BINARIO A DECIMAL")
        print("----------------------------------------")
        print(f" Número binario: {binario}")

        opciones = [numero_decimal]
        while len(opciones) < 5:
            candidato = random.randint(0, max_valor)
            if candidato not in opciones:
                opciones.append(candidato)

        random.shuffle(opciones)

        print("\n Opciones:")
        for i in range(5):
            print(f"  {i + 1}. {opciones[i]}")

        intentos = 3
        partidas += 1
        acerto = False

        while intentos > 0 and acerto == False:
            eleccion = input(" Elegí la opción correcta (1-5): ")

            if eleccion.isdigit():
                eleccion = int(eleccion)
                if 1 <= eleccion <= 5:
                    if opciones[eleccion - 1] == numero_decimal:
                        print("\n ¡Correcto!")
                        aciertos += 1
                        acerto = True
                    else:
                        intentos -= 1
                        print(f" Incorrecto. Te quedan {intentos} intento(s).")
                else:
                    print(" Elegí un número entre 1 y 5.")
            else:
                print(" Ingresá un número válido entre 1 y 5.")

        print(f"\n La respuesta correcta era: {numero_decimal}")

        print("\n Explicación paso a paso:")
        suma = 0
        for i in range(bits):
            bit = int(binario[i])
            potencia = bits - 1 - i
            valor = bit * (2 ** potencia)
            print(f"  {bit} × 2^{potencia} = {valor}")
            suma += valor
        print(f"\n Resultado final: {suma}")

    elif opcion == 'd':
        # DECIMAL A BINARIO
        numero_decimal = random.randint(0, max_valor)
        temp = numero_decimal
        binario_correcto = ""

        for _ in range(bits):
            binario_correcto = str(temp % 2) + binario_correcto
            temp //= 2
        while len(binario_correcto) < bits:
            binario_correcto = "0" + binario_correcto

        print("\n----------------------------------------")
        print(" DECIMAL A BINARIO")
        print("----------------------------------------")
        print(f" Número decimal: {numero_decimal}")

        opciones = [binario_correcto]
        while len(opciones) < 5:
            candidato = random.randint(0, max_valor)
            bin_incorrecto = bin(candidato)[2:].zfill(bits)
            if bin_incorrecto not in opciones:
                opciones.append(bin_incorrecto)

        random.shuffle(opciones)

        print("\n Opciones:")
        for i in range(5):
            print(f"  {i + 1}. {opciones[i]}")

        intentos = 3
        partidas += 1
        acerto = False

        while intentos > 0 and acerto == False:
            eleccion = input(" Elegí la opción correcta (1-5): ")

            if eleccion.isdigit():
                eleccion = int(eleccion)
                if 1 <= eleccion <= 5:
                    if opciones[eleccion - 1] == binario_correcto:
                        print("\n ¡Correcto!")
                        aciertos += 1
                        acerto = True
                    else:
                        intentos -= 1
                        print(f" Incorrecto. Te quedan {intentos} intento(s).")
                else:
                    print(" Elegí un número entre 1 y 5.")
            else:
                print(" Ingresá un número válido entre 1 y 5.")

        print(f"\n La respuesta correcta era: {binario_correcto}")

        print("\n Explicación paso a paso:")
        pasos = []
        temp = numero_decimal
        while temp > 0:
            residuo = temp % 2
            cociente = temp // 2
            pasos.append((temp, 2, cociente, residuo))
            temp = cociente
        for paso in pasos:
            print(f"  {paso[0]} ÷ {paso[1]} = {paso[2]}, residuo = {paso[3]}")
        print(f"\n Resultado final (de abajo hacia arriba): {binario_correcto}")

    else:
        print(" Opción no válida. Por favor, escribí 'b' o 'd'.")

    print(f"\nEstadísticas: {aciertos} acierto(s) sobre {partidas} partida(s) jugada(s).")

    otra = input("\n ¿Querés jugar otra vez? (s/n): ").lower()
    if otra != 's':
        bandera = False

print("\nGracias por jugar. ¡Hasta la próxima!")