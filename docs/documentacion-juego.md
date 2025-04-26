# Guía

## Objetivo del juego
El programa consiste en un juego de adivinanzas en el que el usuario debe convertir números entre representaciones binarias y decimales. El juego presenta opciones múltiples y explica paso a paso la conversión.

---

## 1. Inicialización

- Se importa el módulo `random` para generar números aleatorios.
- Se definen variables de control:
  - `partidas`: total de rondas jugadas.
  - `aciertos`: cantidad de respuestas correctas.
  - `bandera`: controla la ejecución continua del juego.

---

## 2. Elección de dificultad (cantidad de bits)

- Se solicita al usuario elegir entre 4, 6 u 8 bits.
- Se verifica que la entrada sea un número válido y permitido.
- Se calcula el valor decimal máximo representable con esa cantidad de bits 
  usando `2 ** bits - 1`.

---

## 3. Bucle principal del juego

- Mientras la `bandera` esté activa, el juego sigue ejecutándose.
- Se pregunta al usuario si desea jugar en dirección:
  - Binario a Decimal (`b`)
  - Decimal a Binario (`d`)

---

## 4. Modo Binario a Decimal

- Se genera un número decimal aleatorio y se convierte a binario con `bin()` y `zfill()`.
- Se generan 4 opciones incorrectas distintas y se añaden a la lista de opciones junto con la correcta.
- Se mezclan las opciones aleatoriamente.
- Se muestran las opciones una sola vez.

### Bucle de intentos (hasta 3)

- Se permite elegir una opción entre 1 y 5.
- Se valida la entrada:
  - Si es correcta: se suma a los aciertos y se finaliza la ronda.
  - Si es incorrecta: se informa y se reduce el contador de intentos.

### Explicación paso a paso

- Se recorre el binario y se explica la conversión de cada bit usando la potencia correspondiente de 2.
- Se muestra la suma final obtenida.

---

## 5. Modo Decimal a Binario

- Se genera un número decimal aleatorio.
- Se convierte a binario de forma manual:
  - Se divide sucesivamente por 2 guardando los residuos.
  - Se invierte el orden de los residuos para obtener el binario.
- Se agregan ceros a la izquierda si el binario resultante es menor que la cantidad de bits elegida.

- Se generan 4 opciones incorrectas con el mismo formato binario.

### Bucle de intentos (hasta 3)

- Igual que en el modo anterior, se evalúa la elección y se brinda retroalimentación.

### Explicación paso a paso

- Se muestran todas las divisiones y residuos usados en la conversión.
- Se indica que el binario se forma "de abajo hacia arriba".

---

## 6. Estadísticas y control de continuidad

- Al final de cada ronda, se muestran las estadísticas de aciertos y partidas jugadas.
- Se pregunta al usuario si desea jugar otra vez.
  - Si responde 's', el juego sigue.
  - Si no, se termina el bucle principal y se despide al usuario.

---

## Notas técnicas

- Todas las entradas del usuario se validan cuidadosamente.
- Las opciones se muestran una sola vez por ronda.
- Se explica el proceso de conversión en ambas direcciones con detalle educativo.

---

Este juego es útil para practicar y entender la relación entre los sistemas binario y decimal, con una interfaz simple y validaciones robustas.
