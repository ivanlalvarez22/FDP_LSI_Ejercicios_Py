# Generar una matriz D (NxN), con números de cuatro dígitos, luego:
# Calcular y mostrar el porcentaje de elementos cuyo dígito correspondiente a la decena sea múltiplo de 7.
# Generar el vector L con la sumatoria de los elementos de las columnas de la matriz.
import numpy as np
N = 0
while not 0 < N < 6:
    N = int(input("Ingresar la dimensión de la matriz cuadrada D: "))
# Carga estática de la matriz D
D = np.array(([1979, 1945, 1918, 2020, 2202], [7472, 4347, 1122, 3568, 4215], [1114, 8788, 9553, 3354, 5412],
              [1742, 1665, 2670, 3030, 4041], [1018, 8078, 9999, 6666, 5555]))
# Definimos el vector L
L = np.empty(N, dtype=int)
# Ciclo para mostrar la matriz D
print("La matriz D generada es la siguiente: ")
for i in range(0, N):
    for j in range(0, N):
        print(D[i, j], end=" ")
    print(" ")
# Desarrollo de act 'a': Calcular y mostrar el porcentaje de elementos cuyo dígito
# correspondiente a la decena sea múltiplo de 7.
# Cálculo de la unidad de la decena
cdMul7 = 0
for i in range(0, N):
    for j in range(0, N):
        decena = (D[i, j] // 10) % 10
        if decena % 7 == 0:
            cdMul7 += 1
porc = (cdMul7 / (N*N)) * 100
print("El porcentaje de dígitos de la decena múltiplos de 7 son: %.2f" % porc, "%")
# Desarrollo act 'b': Generar el vector L con la sumatoria de los elementos de las columnas de la matriz.
aux = 0
for j in range(0, N):
    suma = 0
    for i in range(0, N):
        suma += D[i, j]
    L[aux] = suma
    aux += 1
# Ciclo para mostrar el vector 'L'
print("El vector L es el siguiente: ")
for i in range(0, aux):
    print(L[i], end=" ")
