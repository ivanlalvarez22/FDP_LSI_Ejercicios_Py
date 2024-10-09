# Mostrar los números pares del vector K. Si no hubiera números pares
# mostrar el mensaje "Vector sin números pares".

import numpy as np
dim = 0  # Igualamos a 0 para que entre en el ciclo siguiente
while not 0 < dim <= 100:
    dim = int(input("Ingresar la cantidad de elementos del vector K(1-100): "))
k = np.empty(dim, dtype=int)
# Ciclo para cargar el vector
for i in range(0, dim):
    k[i] = int(input(f"Ingrese el {i + 1}° elemento: "))
# Ciclo para mostrar el vector
for i in range(0, dim):
    print(k[i], end=" ")
print(" ")
# Calculamos los elementos pares e impares
par = False
for i in range(0, dim):
    if k[i] % 2 == 0:
        print(k[i], end=" ")
        par = True
if not par:
    print("Vector sin números pares.")
