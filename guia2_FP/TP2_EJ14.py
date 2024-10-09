# Dado un vector A, generar un nuevo arreglo con las posiciones de los elementos del arreglo A
# que sean iguales a un valor X dado.
import numpy as np
dim = int(input("Ingresar la dimensión del vector: "))
A = np.empty(dim, dtype=int)
B = np.empty(dim, dtype=int)
b = False
# Ciclo para cargar el vector A
i = 0
while i < dim:
    print(f"Ingresar el {i + 1}° elemento del vector A: ", end="")
    A[i] = int(input())
    i += 1
# Ciclo para mostrar el vector A generado
print("El vector A generado es el siguiente: ")
i = 0
while i < dim:
    print(A[i], end=" ")
    i += 1
print(" ")
# Ciclo para generar el vector B con valores iguales a uno X dado
print("Ingresar un número del vector A: ", end="")
X = int(input())
i = 0
k = 0
while i < dim:
    if A[i] == X:
        B[k] = i
        b = True
        k += 1
    i += 1
# Ciclo para mostrar el vector B
if b:
    print("Las posiciones donde se repite ese número son: ")
i = 0
while i < k:
    print(B[i], end=" ")
    i += 1
print(" ")
if not b:
    print("El número ingresado no se repite en el vector 'A'")
