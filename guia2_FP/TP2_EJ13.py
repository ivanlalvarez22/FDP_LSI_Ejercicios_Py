# Dado un vector A de números enteros, generar un nuevo arreglo solamente con los números negativos de A
import numpy as np
dim = int(input("Ingresar la dimensión del vector A: "))
A = np.empty(dim, dtype=int)
NEG = np.empty(dim, dtype=int)
# Ciclo para cargar el vector A
for i in range(0, dim):
    print(f"Ingresar el {i + 1}° elemento del vector A: ", end="")
    A[i] = int(input())
# Ciclo para mostrar el vector A
print("El vector A generado es el siguiente: ")
for i in range(0, dim):
    print(A[i], end=" ")
print(" ")
# Ciclo para cargar y mostrar el vector negativos
k = 0
for i in range(0, dim):
    if A[i] < 0:
        print(k)
        NEG[k] = A[i]
        k += 1
print(" ")
# Ciclo para mostrar el vector negativos de A
print("El vector con los elementos negativos de A es: ")
for i in range(0, k):
    print(NEG[i], end=" ")
print(" ")
