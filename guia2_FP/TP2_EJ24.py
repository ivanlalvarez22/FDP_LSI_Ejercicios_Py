# Dada una matriz A de N x N elementos:
# a.Generar un vector B con la sumatoria de cada fila de la matriz.
# b.Generar un vector C con el promedio de los elementos de cada columna de la matriz
import numpy as np
A = np.array(([3, 2, 1, 4, 5], [1, 3, 0, 4, 9], [2, 1, 4, 4, 4],
              [1, 0, 3, 4, 2], [1, 4, 7, 4, 6]))
B = np.empty(10, dtype=int)
C = np.empty(10, dtype=float)
# Ciclo para indicar la cantidad NxN de elementos de la matriz A
N = 0
while not 0 < N < 6:
    print("Ingresar la cantidad de filas y columnas de la matriz cuadrada A (1-5): ", end="")
    N = int(input())
# Ciclo para mostrar la matriz A generada
for i in range(0, N):
    for j in range(0, N):
        print(A[i, j], end=" ")
    print(" ")
# ACT 1: Ciclo para generar un vector B con la sumatoria de cada fila de la matriz.
for i in range(0, N):
    suma = 0
    for j in range(0, N):
        suma += A[i, j]
    B[i] = suma
print("El vector B con la sumatoria de cada fila de la matriz A es: ")
for i in range(0, N):
    print(B[i])
# ACT 2: generar un vector C con el promedio de los elementos de cada columna de la matriz
for j in range(0, N):
    sumaCol = 0
    promCol = 0
    k = 0
    for i in range(0, N):
        sumaCol += A[i, j]
    promCol = sumaCol / N
    C[j] = promCol
# Ciclo para mostrar el vector C
print("El vector C con el promedio de los elementos de cada columna de la matriz A es: ")
for i in range(0, N):
    print("%.2f" % C[i], end=" ")
