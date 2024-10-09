# Generar una matriz M de 4x3 y mostrar la matriz M
import numpy as np
# Indicamos la cantidad de filas y columnas de la matriz M
FILAS = int(input("Ingresar la cantidad de filas de la matriz M: "))
COLUMNAS = int(input("Ingresar la cantidad de columnas de la matriz M: "))
M = np.empty((FILAS, COLUMNAS), dtype=int)
# Ciclo para cargar la matriz M
for i in range(0, FILAS):
    for j in range(0, COLUMNAS):
        print(f"Ingresar el {j + 1}° elemento de la {i + 1}° fila de M: ", end="")
        M[i, j] = int(input())
# Ciclo para mostrar la matriz M
print("La matriz M es la siguiente: ")
for i in range(0, FILAS):
    for j in range(0, COLUMNAS):
        print(M[i, j], end=" ")
    print(" ")
