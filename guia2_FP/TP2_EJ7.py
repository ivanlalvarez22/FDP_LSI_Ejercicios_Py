# Dado el vector E de X elementos - Con un valor de X no mayor a 20,
# permutarlo de la siguiente manera: A (1) con A(X), A (2) con A (X-1), A (3) con A (X-2) y
# así sucesivamente. Mostrar el vector con los elementos permutados.

import numpy as np
E = np.empty(20, dtype=int)
# Ciclo para ingresar la cantidad de elementos mayores a 0 y menores o iguales a 20
X = int(input("Ingresar la cantidad de elementos del vector: "))
aux1 = X - 1  # Guardo la última posición del vector
while not 0 < X < 20:
    X = int(input("Ingresar la cantidad de elementos del vector: "))
    aux1 = X
# Ciclo para cargar el vector
for i in range(0, X):
    print(f"Ingresar el {i + 1} elemento del vector: ")
    E[i] = int(input())
# Ciclo para mostrar el vector E generado
print("El vector E generado es el siguiente: ")
for i in range(0, X):
    print(E[i], end=" ")
print(" ")
# Ciclo para permutar el vector
for i in range(0, int(X / 2)):
    aux = E[i]
    E[i] = E[aux1]
    E[aux1] = aux
    aux1 -= 1
# Ciclo para mostrar el vector permutado
print("El vector permutado es: ")
for i in range(0, X):
    print(E[i], end=" ")
print(" ")
