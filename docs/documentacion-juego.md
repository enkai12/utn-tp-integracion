# Guía detallada del juego de adivinanzas binarias

Este juego permite practicar la conversión entre binario y decimal, con distintos niveles de dificultad.

## Introducción general

El juego consiste en elegir una cantidad de bits (4, 6 u 8), seleccionar la dirección del juego (de binario a decimal o viceversa), y adivinar entre cinco opciones cuál es la correcta. El usuario tiene 3 intentos por partida y se llevan estadísticas de aciertos y partidas jugadas.

---

## Paso 1 - Elección de la cantidad de bits

Se solicita al usuario que ingrese cuántos bits quiere usar: 4, 6 u 8.

```python
bits = 0
while bits != 4 and bits != 6 and bits != 8:
    entrada = input("Elegí la cantidad de bits (4, 6 u 8): ")
    if entrada.isdigit():
        bits = int(entrada)
        if bits != 4 and bits != 6 and bits != 8:
            print("Solo se permite 4, 6 u 8.")
    else:
        print("Entrada no válida. Ingresá un número.")
```

Esto valida que la entrada sea numérica y esté dentro de las opciones permitidas. El valor máximo se calcula como `2 ** bits - 1`.

---

## Paso 2 - Menú de dirección del juego

Se le pregunta al usuario si quiere convertir:

- De binario a decimal (`b`)
- De decimal a binario (`d`)

Esto se hace dentro de un bucle principal que permite jugar varias veces.

---

## Paso 3A - Juego: Binario a Decimal

1. Se genera un número aleatorio y se lo convierte a binario con la función `bin()`.
2. Se generan 4 opciones incorrectas que no se repitan.
3. Se muestran las 5 opciones al usuario, solo una es la correcta.
4. Se dan hasta 3 intentos para adivinar.

```python
numero_decimal = random.randint(0, max_valor)
binario = bin(numero_decimal)[2:].zfill(bits)
```

La función `zfill(bits)` agrega ceros a la izquierda si el número binario tiene menos dígitos.

---

## Paso 4A - Evaluación de respuesta (Binario a Decimal)

Se muestra la lista de opciones solo una vez, y se reduce el número de intentos sin volver a mostrarlas.

Si el usuario elige una opción correcta, se actualizan las estadísticas y se da una explicación detallada:

```python
for i in range(bits):
    bit = int(binario[i])
    potencia = bits - 1 - i
    valor = bit * (2 ** potencia)
    suma += valor
```

Este bucle descompone el número binario para explicar cómo se calcula el decimal paso a paso.

---

## Paso 3B - Juego: Decimal a Binario

1. Se genera un número aleatorio entre 0 y el valor máximo.
2. Se convierte manualmente a binario dividiendo por 2.
3. Se generan 4 opciones incorrectas diferentes.
4. Se muestran las 5 opciones al usuario, solo una es la correcta.

La conversión manual a binario se hace con un bucle como este:

```python
for _ in range(bits):
    binario_correcto = str(temp % 2) + binario_correcto
    temp //= 2
```

---

## Paso 4B - Evaluación de respuesta (Decimal a Binario)

Después de responder, se muestra paso a paso cómo se llegó al número binario:

```python
while temp > 0:
    residuo = temp % 2
    cociente = temp // 2
    pasos.append((temp, 2, cociente, residuo))
    temp = cociente
```

Luego se imprimen los pasos en orden, explicando el método de divisiones sucesivas.

---

## Paso 5 - Estadísticas y Repetición

Al final de cada ronda se muestran las estadísticas de aciertos y partidas, y se pregunta si se desea jugar de nuevo.

---

## Detalles adicionales

- No se usa `try`, `except` ni `break`, por lo tanto toda la validación se hace con `isdigit()` y condiciones `while`.
- Las opciones se generan una sola vez y no se repiten entre intentos.
- El juego incluye 3 niveles de dificultad según la cantidad de bits: 4, 6 u 8.

---

## Fin del juego

Al finalizar, se agradece al usuario por jugar.

```python
print("\nGracias por jugar. ¡Hasta la próxima!")
```
