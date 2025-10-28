# -----------------------------------------
# PROGRAMA: REPRESENTACIÓN DE UNA MATRIZ 3x5
# -----------------------------------------
# Autor: Alex Armando Ávila Coello
# Descripción: Este programa crea una matriz de 3 filas por 5 columnas,
# la muestra en pantalla, recorre sus elementos e identifica un valor específico
# según su posición (fila y columna).

# ---------------------------------------------------------
# Paso 1: CREAR UNA MATRIZ DE 3 FILAS POR 5 COLUMNAS
# ---------------------------------------------------------
# 🔹 En este paso no se utiliza ninguna biblioteca externa.
# 🔹 Python permite crear matrices usando listas dentro de listas (listas anidadas).
# 🔹 Cada sublista representa una FILA, y cada valor dentro de ella una COLUMNA.

matriz = [
    [5, 8, 2, 4, 3],       # Fila 1
    [7, 5, 1, 8, 7],       # Fila 2
    [2, 8, 16, 15, 14]     # Fila 3
]

# ---------------------------------------------------------
# Paso 2: MOSTRAR LA MATRIZ COMPLETA EN FORMATO VISUAL
# ---------------------------------------------------------
# 🔹 La función print() muestra información en pantalla.
# 🔹 La función enumerate() devuelve el índice y el valor de cada fila.
# 🔹 Se usa una f-string (f"...") para insertar variables dentro del texto fácilmente.

print("MATRIZ DE 3 FILAS x 5 COLUMNAS:\n")
for i, fila in enumerate(matriz):    # for = bucle que recorre elementos de una lista
    print(f"Fila {i+1}: {fila}")     # i+1 = se suma 1 para mostrar el número de fila real

# ---------------------------------------------------------
# Paso 3: EXPLICACIÓN CONCEPTUAL
# ---------------------------------------------------------
# 🔹 Se usa únicamente la función print() para mostrar texto explicativo.

print("\nExplicación:")
print("Una matriz es una estructura de datos bidimensional,")
print("formada por filas (horizontales) y columnas (verticales).")
print("El número de fila indica la posición horizontal del elemento,")
print("y el número de columna indica la posición vertical dentro de la fila.")

# ---------------------------------------------------------
# Paso 4: MOSTRAR CADA ELEMENTO CON SU POSICIÓN
# ---------------------------------------------------------
# 🔹 len() devuelve la cantidad de elementos (en este caso, filas o columnas).
# 🔹 range() genera una secuencia de números del 0 al número indicado.
# 🔹 Los dos bucles for anidados recorren toda la matriz elemento por elemento.

print("\nElementos de la matriz con su posición (fila, columna):\n")
for i in range(len(matriz)):          # len(matriz) = 3 → recorre las 3 filas
    for j in range(len(matriz[i])):   # len(matriz[i]) = 5 → recorre las 5 columnas
        # Acceso al elemento usando índices [fila][columna]
        print(f"Elemento {matriz[i][j]} está en la Fila {i+1}, Columna {j+1}")

# ---------------------------------------------------------
# Paso 5: BUSCAR UN ELEMENTO ESPECÍFICO
# ---------------------------------------------------------
# 🔹 Los índices en Python comienzan desde 0 (no desde 1).
# 🔹 Por eso: Fila 2 → índice 1, Columna 4 → índice 3.
# 🔹 El acceso se realiza con matriz[fila_buscada][columna_buscada].

fila_buscada = 1      # Representa la Fila 2
columna_buscada = 3   # Representa la Columna 4

elemento = matriz[fila_buscada][columna_buscada]  # Se obtiene el valor

print("\n---------------------------------------------")
print(f"El elemento ubicado en la Fila 2 y Columna 4 es: {elemento}")
print("---------------------------------------------")

# ---------------------------------------------------------
# Paso 6: EXPLICACIÓN FINAL
# ---------------------------------------------------------
# 🔹 Se utiliza print() nuevamente para presentar la conclusión textual.

print("\nInterpretación final:")
print("El elemento buscado se encuentra en la intersección entre la fila 2 y la columna 4.")
print("En la matriz, eso corresponde al número 8.")  # Se actualiza según el valor real de la matriz

# ---------------------------------------------------------