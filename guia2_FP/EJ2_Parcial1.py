# Dada una matriz B (NxN) de números enteros de tres cifras, se pide:
# Mostrar el mayor elemento de la triangular inferior.
# Generar el vector H, con aquellos elementos de la matriz cuyo dígito de la decena sea múltiplo de 3.
import numpy as np
N = 0
while not 0 < N < 6:
    N = int(input("Ingresar la dimensión de la matriz cuadrada 'B' de NxN: "))
# Carga estática de la matriz B
B = np.array(([132, 241, 341, 431, 521], [123, 234, 345, 456, 567], [123, 234, 345, 456, 567],
              [123, 234, 345, 456, 567], [123, 234, 345, 456, 567]))
H = np.empty(N*N, dtype=int)
# Ciclo para mostrar la matriz B
for i in range(0, N):
    for j in range(0, N):
        print(B[i, j], end=" ")
    print(" ")
# Ciclo para mostrar la triangular inferior de la matriz B
print("La matriz B triangular inferior es la siguiente: ")
for i in range(0, N):
    for j in range(0, N):
        if i > j:
            print(B[i, j], end=" ")
    print(" ")
# Desarrollo de la actividad 'a': Mostrar el mayor elemento de la triangular inferior.
bandera = False
mayor = 0
for i in range(0, N):
    for j in range(0, N):
        if i > j:
            if not bandera:
                mayor = B[i, j]
                bandera = True
            if B[i, j] > mayor:
                mayor = B[i, j]
print("El número de mayor valor de la diagonal inferior es: ", mayor)
# Desarrollo de la actividad 'b': Generar el vector H, con aquellos elementos de
# la matriz cuyo dígito de la decena sea múltiplo de 3
k = 0  # k actuará como índice del vector 'H' al mismo tiempo que nos indicará su dimensión máxima
for i in range(0, N):
    for j in range(0, N):
        decena = (B[i, j] // 10) % 10
        if decena % 3 == 0:
            H[k] = B[i, j]
            k += 1
# Ciclo para mostrar el vector H
print("El vector 'H' con los elementos de la decena de la matriz 'B' múltiplos de 3 es: ")
for i in range(0, k):
    print(H[i], end=" ")
