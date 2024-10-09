# TEMA A
# Dada una matriz A (NxN) de números enteros, se pide:
# Mostrar la cantidad de veces que aparece un número dado en la matriz A.
# Generar el vector C, con aquellos elementos de la triangular superior que sean
# mayores o iguales al promedio de los números de la diagonal principal.4
import numpy as np
N = 0
while not 0 < N < 6:
    N = int(input("Ingresar la dimensión de la matriz cuadrada 'A' de NxN: "))
# Carga estática de la matriz A
A = np.array(([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
# Definimos el vector C
C = np.empty(10, dtype=int)
# Ciclo para mostrar la matriz 'A'
for i in range(0, N):
    for j in range(0, N):
        print(A[i, j], end=" ")
    print(" ")
# Desarrollo de actividad 'a': Mostrar la cantidad de veces que aparece un número dado en la matriz A.
num = int(input("Ingresar un valor para contar las veces que se repite en la matriz A: "))
con_num = 0
for i in range(0, N):
    for j in range(0, N):
        if A[i, j] == num:
            con_num += 1
print("La cantidad de veces que se repite el número %d en la matriz 'A' son: %d " % (num, con_num))
# Desarrollo de actividad 'b': Generar el vector C, con aquellos elementos de la triangular superior que sean
# mayores o iguales al promedio de los números de la diagonal principal.
# Ciclo para calcular el promedio de elementos de la diagonal principal.
suma = 0
c_DP = 0
for i in range(0, N):
    for j in range(0, N):
        if j == i:
            suma += A[i, j]
            c_DP += 1
prom = suma / c_DP
print("El promedio de los números de la diagonal principal son: %.2f" % prom)
# Ciclo para mostrar los elementos de la triangular superior
print("La matriz triangular superior de 'A' es: ")
for i in range(0, N):
    for j in range(0, N):
        if j > i:
            print(A[i, j], end=" ")
    print(" ")
# Ciclo para generar el vector C con los elementos de la TS mayores al promedio de la DP
k = 0
for i in range(0, N):
    for j in range(0, N):
        if j > i and A[i, j] >= prom:
            C[k] = A[i, j]
            k += 1
            print("+")
# Ciclo para mostrar el vector C generado
print("El vector C generado es el siguiente: ")
for i in range(0, k):
    print(C[i], end=" ")
