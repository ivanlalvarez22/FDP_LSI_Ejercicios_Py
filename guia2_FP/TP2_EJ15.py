# Dado un vector A de N elementos(con un valor de N no mayor a 20), generar un nuevo arreglo tal que
# sus elementos sean la diferencia de los elementos sucesivos del arreglo dado.
# Ejemplo: arreglo A = [4, 6, 8, 2, 6, 9, 6, 1]            arreglo B = [-2, -2, 6, -4, -3, 3, 5]
import numpy as np
dim = int(input("Ingrese la dimensión del vector A: "))
A = np.empty(dim, dtype=int)
B = np.empty(dim, dtype=int)
# Ciclo para cargar el vector A
for i in range(0, dim):
    print(f"Ingresar el {i + 1}° elemento del vector A: ", end="")
    A[i] = int(input())
# Ciclo para mostrar el vector A
print("El vector A generado es el siguiente: ")
for i in range(0, dim):
    print(A[i], end=" ")
print(" ")
# Ciclo para calcular la diferencia de elementos sucesivos del arreglo A
k = 0
for i in range(0, dim - 1):
    B[k] = A[i] - A[i + 1]
    k += 1
# Ciclo para mostrar el vector diferencia
print("El vector diferencia es el siguiente: ")
for i in range(0, k):
    print(B[i], end=" ")
