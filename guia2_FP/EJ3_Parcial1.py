# Dada una matriz C (MxM) de números enteros, se pide:
# Determinar el porcentaje de números pares de la diagonal principal.
# Generar el vector K, con aquellos elementos de C que sean de dos cifras y menores a un número dado.
import numpy as np
M = 0
while not 0 < M < 6:
    M = int(input("Ingresar la dimensión de la matriz cuadrada C de MxM: "))
# Carga estática de la matriz C
C = np.array(([10, 23, 43, 74, 35], [99, 69, 74, 72, 30], [11, 72, 38, 14, 65],
              [12, 42, 63, 34, 88], [12, 20, 31, 44, 15]))
K = np.empty(M*M, dtype=int)  # Defino el vector K
# Ciclo para mostrar la matriz C
print("La matriz C generada es la siguiente: ")
for i in range(0, M):
    for j in range(0, M):
        print(C[i, j], end=" ")
    print(" ")
# Desarrollo actividad 'a': Ciclo para determinar el porcentaje de números pares de la diagonal principal.
cantDP = 0
for i in range(0, M):
    if C[i, i] % 2 == 0:
        cantDP += 1
porc = (cantDP / M) * 100
print("El porcentaje de números pares de la diagonal principal son : %.2f" % porc, "%")
# Desarrollo de actividad 'b': Generar el vector K, con aquellos elementos de C que
# sean de dos cifras y menores a un número dado.
num = int(input("Ingresar un número: "))
aux = 0
bandera = False
for i in range(0, M):
    for j in range(0, M):
        if 9 < C[i, j] < 100:
            if C[i, j] < num:
                K[aux] = C[i, j]
                aux += 1
                bandera = True
# Ciclo para mostrar el vector 'K'
print("El vector 'K' es el siguiente: ")
for i in range(0, aux):
    print(K[i], end=" ")
if not bandera:
    print("No existen valores de dos cifras menores al número ingresado.")
