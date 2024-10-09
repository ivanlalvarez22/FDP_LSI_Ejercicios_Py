# Dada una matriz A de N x N y un vector B de X elementos,
# mostrar el elemento del vector B que se repita el mayor número de veces en la diagonal principal.
import numpy as np
# Carga estática de la matriz A

A = np.array(([4, 3, 4, 5, 1], [4, 4, 9, 9, 3], [1, 2, 3, 1, 2],
              [5, 7, 8, 8, 1], [8, 3, 1, 2, 1]))
# Ciclo para indicar la dimensión de la matriz A
N = 0

while not 0 < N < 6:
    print("Ingresar la cantidad de filas y columnas de la matriz cuadrada A (1-5): ")
    N = int(input())

# Carga estática del vector B
B = np.array([4, 1, 2, 5, 7, 8, 3])

# Ciclo para indicar la cantidad de elementos del vector B

X = 0
while not 0 < X < 8:
    print("Ingresar la cantidad de elementos del vector B (1-7): ")
    X = int(input())
# Ciclo para mostrar la matriz A
print("La matriz A es la siguiente: ")
for i in range(0, N):
    print("[", end="")
    for j in range(0, N):
        print(A[i, j], end=" ")
    print("]", end="")
    print(" ")
# Ciclo para mostrar el vector B
print("El vector B es el siguiente: ")
print("[", end="")
for i in range(0, X):
    print(B[i], end=" ")
print("]")
# Ciclo para mostrar el elemento del vector B que se repita el mayor número de veces en la diagonal principal
# Estrategia de solución: por cada elemento del vector 'B' recorremos la diagonal principal de la matriz 'A',
# contamos la cantidad de veces que se repite cada elemento de 'B' en la misma y guardamos el dato
# a continuación usamos el algoritmo del mayor para comparar y ver cual elemento se repitió mas veces
cant_rep = 0
mayor_rep = 0
bandera = False
for k in range(0, X):  # 'X' dimensión del vector B
    cant_B = 0
    for i in range(0, N):
        if A[i, i] == B[k]:
            cant_B += 1
    if bandera:  # Algoritmo del mayor
        cant_rep = cant_B
        mayor_rep = B[k]
        bandera = True
    if cant_B > cant_rep:
        cant_rep = cant_B
        mayor_rep = B[k]
    print(f"Las veces que se repite el valor {B[k]} son {cant_B} veces")
print(f"El número que se repite mas veces es el {mayor_rep}")
print(f"El mismo se repite {cant_rep} veces")
