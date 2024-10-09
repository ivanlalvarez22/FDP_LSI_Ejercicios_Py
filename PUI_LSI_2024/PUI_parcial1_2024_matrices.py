"""

Se pide realizar el algoritmo de solución del siguiente problema expresado en Diagrama de Flujo, además definir las
estructuras de datos que se van a utilizar para solución del mismo.

Una tarjeta de crédito que tiene N clientes, almacena la información de los mismos: Nro de Cliente y los consumos de
cada uno de los meses del año 2022, en una matriz CLI.
Se pide lo siguiente:
a) Cargar en una nueva columna el promedio de consumo realizado por cada cliente
b) Generar una matriz F que contenga los Nro de Cliente y el promedio de consumo del cliente de ✓ aquellos que obtuvieron
un Promedio superior a 55.000.
c) Mostrar la información de la matriz F ordenada en forma descendente por Nro. de Cliente.
d) Agregar un nuevo cliente en la matriz F mediante el método de inserción ordenada.

"""

import numpy as np

# Datos de entrada
CLI = [
    [1, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 0],
    [2, 15000, 25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000, 115000, 125000, 0],
    [3, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 0],
    [4, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 0],
]

# Convertir la lista a una matriz numpy
CLI = np.array(CLI)

FILAS = len(CLI)
COLUMNAS = len(CLI[0])

# a) Cargar en una nueva columna el promedio de consumo realizado por cada cliente
for i in range(FILAS):
    sum = 0
    for j in range(1, COLUMNAS - 1):
        sum += CLI[i, j]
    prom = sum / 12
    CLI[i, COLUMNAS - 1] = prom

# Mostrar la matriz CLI con los promedios
print("Matriz CLI con los promedios:")
for i in range(FILAS):
    for j in range(COLUMNAS):
        print(CLI[i, j], end=" ")
    print(" ")

# b) Generar una matriz F que contenga los Nro de Cliente y el promedio de consumo del cliente
#    de aquellos que obtuvieron un Promedio superior a 55.000.
filas_matriz_F = 4
columnas_matriz_F = 2
F = np.empty((filas_matriz_F, columnas_matriz_F), dtype=int)
# Convertir la lista a una matriz numpy
F = np.array(F)

for i in range(filas_matriz_F):
    for j in range(columnas_matriz_F):
        F[i, j] = 0

for i in range(filas_matriz_F):
    for j in range(1, columnas_matriz_F):
        if CLI[i, COLUMNAS - 1] > 55000:
            F[i, 0] = CLI[i, 0]
            F[i, j] = CLI[i, COLUMNAS - 1]

# Mostrar la matriz F
print("Matriz F:")
for i in range(len(F)):
    for j in range(len(F[0])):
        print(F[i, j], end=" ")
    print(" ")

# c) Ordenar la matriz F por Nro. de Cliente en forma descendente usando el algoritmo de burbuja
# Implementar el algoritmo de ordenamiento con variables auxiliares
N = len(F)
b = 0
while b != 1:
    b = 1
    for i in range(N - 1):
        if F[i][0] < F[i + 1][0]:  # Condición SI F[i, 0] < F[i + 1, 0]
            # Intercambiar filas utilizando variables auxiliares
            temp1 = F[i][0]
            temp2 = F[i][1]
            F[i][0] = F[i + 1][0]
            F[i][1] = F[i + 1][1]
            F[i + 1][0] = temp1
            F[i + 1][1] = temp2
            b = 0

print("Matriz F ordenada en forma descendente por Nro. de Cliente:")
for i in range(len(F)):
    for j in range(len(F[0])):
        print(F[i, j], end=" ")
    print(" ")

# d) Agregar un nuevo cliente en la matriz F mediante el método de inserción ordenada.
nuevo_cliente = np.array([5, 80000])

N = len(F) - 1
B = 0
I = 0
# Buscar la posición de inserción y desplazar elementos si es necesario
while I < N and B == 0:
    if nuevo_cliente[0] > F[I, 0]:
        # Desplazar elementos hacia la derecha para hacer espacio para el nuevo cliente
        for J in range(N, I, -1):
            F[J, 0] = F[J - 1, 0]
            F[J, 1] = F[J - 1, 1]
        # Insertar el nuevo cliente en la posición I
        F[I, 0] = nuevo_cliente[0]
        F[I, 1] = nuevo_cliente[1]
        B = 1
    I += 1
# Si el nuevo cliente es mayor que todos los elementos en F, se inserta al final
if B == 0:
    F[N, 0] = nuevo_cliente[0]
    F[N, 1] = nuevo_cliente[1]

# Mostrar la matriz F después de la inserción
print("\nMatriz F después de la inserción:")
for i in range(len(F)):
    for j in range(len(F[0])):
        print(F[i, j], end=" ")
    print(" ")
