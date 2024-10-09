# Dada una matriz A de M x N elementos, intercambiar los elementos de las filas pares con
# los elementos de las filas impares, considere que M puede ser par o impar. Mostrar la matriz resultante.
import numpy as np
A = np.array(([12, 52, 44, 22, 12], [32, 23, 57, 86, 13], [21, 14, 15, 98, 74],
              [11, 76, 58, 47, 52], [25, 91, 24, 35, 39]))
# Ciclo para indicar la cantidad de filas y columnas de la matriz A
FILAS = 0
while not 0 < FILAS < 6:
    print("Ingresar la cantidad de filas de la matriz A (1-5): ")
    FILAS = int(input())
# Ciclo para indicar la cantidad de columnas de la matriz A
COLUMNAS = 0
while not 0 < COLUMNAS < 6:
    print("Ingresar la cantidad de columnas de la matriz A (1-5): ")
    COLUMNAS = int(input())
# Ciclo para mostrar la matriz A
for i in range(0, FILAS):
    print("[", end="")
    for j in range(0, COLUMNAS):
        print(A[i, j], end=" ")
    print("]", end="")
    print(" ")
# Ciclo para intercambiar los elementos de las filas pares con los elementos de las filas impares
if FILAS % 2 == 0:
    for j in range(0, COLUMNAS):
        i = 0
        while i < FILAS:
            # Algoritmo para intercambiar variables
            aux = A[i, j]
            A[i, j] = A[i + 1, j]
            A[i + 1, j] = aux
            i += 2
else:
    for j in range(0, COLUMNAS):
        i = 0
        while i < FILAS - 1:
            # Algoritmo para intercambiar variables
            aux = A[i, j]
            A[i, j] = A[i + 1, j]
            A[i + 1, j] = aux
            i += 2
# Ciclo para mostrar la matriz A intercambiada
print("La matriz A intercambiada es la siguiente: ")
for i in range(0, FILAS):
    print("[", end="")
    for j in range(0, COLUMNAS):
        print(A[i, j], end=" ")
    print("]", end="")
    print(" ")
