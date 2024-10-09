# Dada la matriz B de N x N elementos, generar en la matriz D la transpuesta de la matriz B.
# La traspuesta de una matriz consiste en la transformación de las filas en columnas y de las columnas en filas.
import numpy as np
N = 0
while not 0 < N < 6:
    N = int(input("Ingresar la cantidad de filas y columnas de la matriz B: "))
# Carga estática de la matriz B
B = np.array(([0, 2, 3, 4, 5], [1, 0, 3, 4, 5], [1, 2, 0, 4, 5],
              [1, 2, 3, 0, 5], [1, 2, 3, 4, 0]))
# Definimos la matriz D
D = np.empty((N, N), dtype=int)
# Ciclo para mostar la matrz B
for i in range(0, N):
    for j in range(0, N):
        print(B[i, j], end=" ")
    print(" ")
# Ciclo para generar en la matriz D la transpuesta de la matriz B.
for i in range(0, N):
    for j in range(0, N):
        D[i, j] = B[j, i]
# Ciclo para mostrar la matriz D traspuesta
print("La matriz D traspuesta de B es la siguiente: ")
for i in range(0, N):
    for j in range(0, N):
        print(D[i, j], end=" ")
    print(" ")
