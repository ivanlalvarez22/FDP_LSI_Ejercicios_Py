# Dado un vector A de N elementos(con un valor de N no mayor a 30), generar un nuevo arreglo tal que
# sus elementos sean la suma de sus elementos opuestos en el arreglo dado.
# Ejemplo: arreglo A = [4, 6, 8, 2, 6, 9, 6]                 arreglo B = [10, 15, 14, 2]
import numpy as np
dim = int(input("Ingresar la dimensión del vector A: "))
aux = dim - 1
A = np.empty(dim, dtype=int)
B = np.empty(dim, dtype=int)
# Ciclo para cargar el vector A
for i in range(0, dim):
    print(f"Ingresar el {i + 1}° elemento del vector A: ", end="")
    A[i] = int(input())
# Ciclo para mostrar el vector cargado
print("El vector A generado es el siguiente: ")
for i in range(0, dim):
    print(A[i], end=" ")
print(" ")
# Ciclo para generar el vector suma de elementos opuestos
k = 0
i = 0
while i < dim / 2:
    B[k] = A[i] + A[aux]
    if aux == i:
        B[k] = A[i]
    i += 1
    k += 1
    aux -= 1
# Ciclo para mostrar el vector suma de elementos opuestos
print("El vector B suma es el siguiente: ")
i = 0
while i < k:
    print(B[i], end=" ")
    i += 1
print(" ")
