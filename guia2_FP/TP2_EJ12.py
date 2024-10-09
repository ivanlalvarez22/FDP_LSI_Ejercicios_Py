# Mostrar la cantidad de veces que aparece un número X en un vector A de 50 elementos,
# y las posiciones del arreglo en que se encuentran.
import numpy as np
dim = int(input("Ingresar la cantidad de elementos del vector A: "))
A = np.empty(dim, dtype=int)
c = 0
# Ciclo para cargar el vector
for i in range(0, dim):
    print(f"Ingresar el {i + 1} elemento del vector: ", end="")
    A[i] = int(input())
# Ciclo para mostrar el vector A
print("El vector A generado es el siguiente: ")
for i in range(0, dim):
    print(A[i], end=" ")
print(" ")
# Ciclo para contar las veces que se repite un elemento del vector
X = int(input("Ingresar un valor del vector A para contar las veces que se repite: "))
for i in range(0, dim):
    if A[i] == X:
        c += 1
print(f"La cantidad de veces que se repite el número {X} son: {c}")
