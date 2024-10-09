# Dadas dos matrices cuadradas A y B de N x N elementos cada una,
# sumarlas y dejar el resultado en una matriz C.
import numpy as np
# Carga estática de la matriz A y B
A = np.array(([2, 7, 1, 0, 5], [5, 1, 1, 5, 0], [9, 7, 3, 2, 2],
              [4, 1, 2, 2, 3], [2, 4, 7, 0, 1]))
B = np.array(([3, 2, 8, 2, 0], [1, 0, 0, 4, 3], [0, 2, 5, 4, 1],
              [3, 2, 1, 1, 2], [0, 8, 7, 4, 4]))
# Ciclo para indicar la dimensión de la matriz A y B
N = 0
while not 0 < N < 6:
    print("Ingresar la cantidad de filas y columnas de las matrices cuadradas A y B: ")
    N = int(input())
C = np.empty((N, N), dtype=int)
# Ciclo para mostrar la matriz A
print("La matriz A es la siguiente: ")
for i in range(0, N):
    print("[", end="")
    for j in range(0, N):
        print(A[i, j], end=" ")
    print("]", end="")
    print("")
# Ciclo para mostrar la matriz B
print("La matriz B es la siguiente: ")
for i in range(0, N):
    print("[", end="")
    for j in range(0, N):
        print(B[i, j], end=" ")
    print("]", end="")
    print("")
# Ciclo para sumar las dos matrices A y B y dejar el resultado en una matriz C
for i in range(0, N):
    for j in range(0, N):
        C[i, j] = (A[i, j] + B[i, j])
# Ciclo para mostrar la maitrz C
print("La matriz C producto de la suma de A y B es la siguiente: ")
for i in range(0, N):
    for j in range(0, N):
        print(C[i, j], end=" ")
    print("")
