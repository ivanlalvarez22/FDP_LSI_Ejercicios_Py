# Dado el vector E de 13 elementos, permutarlo de la siguiente manera:
# B (1) con B (2), B (3) con B (4), B (5) con B (6) y así sucesivamente.
# Mostrar el vector permutado.

import numpy as np
E = np.empty(13, dtype=int)
# Ciclo para cargar el vector
i = 0
while i < 13:
    print(f"Ingresar el valor del {i + 1}° elemento: ", end="")
    E[i] = int(input())
    i += 1
# Ciclo para mostrar el vector
i = 0
print("El vector E generado es el siguiente: ")
while i < 13:
    print(E[i], end=" ")
    i += 1
print(" ")
# Ciclo para permutar el vector
i = 0
while i < 12:
    aux = E[i]
    E[i] = E[i + 1]
    E[i + 1] = aux
    i += 2
print(" ")
# Ciclo para mostrar el vector permutado
i = 0
print("El vector permutado es: ")
while i < 13:
    print(E[i], end=" ")
    i += 1
print(" ")
