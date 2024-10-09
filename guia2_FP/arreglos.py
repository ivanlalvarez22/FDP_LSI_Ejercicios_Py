import numpy as np
# Declaro mi vector
vector = np.empty(5, dtype=int)
# Carga dinámica del vector con for
for i in range(0, 5):
    print(f"Ingrese un número para la posición {i + 1} del vector: ", end="")
    vector[i] = int(input())
# Mostrar vector cargado con for
print("El vector cargado de forma dinámica con for es el siguiente: ")
for i in range(0, 5):
    print(vector[i], end=" ")
print(" ")
# Carga dinámica del vector con while
i = 0
while i < 5:
    print(f"Ingrese un número para la posición {i + 1} del vector: ", end="")
    vector[i] = int(input())
    i += 1
# Mostrar el vector cargado con while
i = 0
print("El vector cargado de forma dinámica con while es el siguiente: ")
while i < 5:
    print(vector[i], end=" ")
    i += 1
print(" ")
# Carga estática del vector con for
vector = np.array([1, 5, 12, 4, 5])
print("El vector cargado de forma estática con for es el siguiente: ")
for i in range(0, 5):
    print(vector[i], end=" ")
print(" ")
# Carga estática del vector con while
vector = np.array([2, 22, 7, 12, 21])
print("El vector cargado de forma estática con while es el siguiente: ")
i = 0
while i < 5:
    print(vector[i], end=" ")
    i += 1
print(" ")
