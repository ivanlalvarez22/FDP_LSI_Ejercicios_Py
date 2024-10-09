# Una compañía tiene N sucursales por todo el país y registra en una matriz de Nx12 las ventas que
# tiene cada sucursal durante los 12 meses del año.
# Determinar y mostrar las sucursales y los meses pares en los cuales sus ventas no superaron un
# determinado monto, en caso de no encontrar sucursales que cumplan esta condición emitir el
# correspondiente mensaje. 25 pts.
# Generar un vector PROMEDIO de N elementos en donde guarde el promedio de ventas de cada una de
# las sucursales. Mostrar el vector resultante. 25 pts.
import numpy as np
N = 0
M = 12
while not 0 < N < 8:
    N = int(input("Ingresar la cantidad de filas de la matriz 'sucursales': "))
sucursales = np.empty((N, M), dtype=float)  # Defino la matriz 'sucursales'
# Carga estática de la matriz 'sucursales'
sucursales = np.array([[3456.63, 3231.56, 2553.24, 4211.52, 3552.52, 5234.57, 7234.87, 8852.83, 1242.23, 2355.42, 3255.66, 2352.66],
                       [3255.56, 3535.23, 2355.67, 2352.89, 4235.22, 5625.89, 7987.33, 8748.35, 2451.57, 2315.78, 2335.67, 4355.67],
                       [1335.25, 3523.37, 2231.60, 4345.48, 3455.92, 5236.02, 7523.72, 8825.72, 1235.52, 2351.62, 3673.63, 4363.62],
                       [1336.35, 3455.84, 2632.90, 4466.21, 3434.34, 2356.34, 2117.45, 8458.12, 1663.64, 5671.67, 3463.31, 3634.34],
                       [9834.45, 2354.67, 4526.92, 2342.28, 2259.09, 5674.32, 7256.25, 2532.45, 7733.74, 6235.42, 2562.21, 8256.35],
                       [1243.96, 3235.72, 2353.72, 4463.71, 3344.34, 5456.19, 7342.63, 8228.91, 1235.87, 1662.00, 3235.98, 4552.12],
                       [1453.72, 3235.61, 2235.82, 4278.90, 3004.87, 5306.61, 7045.01, 8450.72, 1234.88, 1034.91, 3203.22, 4022.91]])
# Ciclo para mostrar la matriz 'sucursales'
print("La matriz 'sucursales' es la siguiente: ")
for i in range(0, N):
    for j in range(0, M):
        print(sucursales[i, j], end=" ")
    print(" ")
# Desarrollo act 'a': # Determinar y mostrar las sucursales y los meses pares en los cuales sus ventas no superaron un
# determinado monto, en caso de no encontrar sucursales que cumplan esta condición emitir el
# correspondiente mensaje. 25 pts.
MONTO = int(input("Ingresar un monto: "))
bandera = False
i = 1
while i < N:
    j = 1
    while j < M:
        if sucursales[i, j] < MONTO:
            print("En la sucursal:", i + 1, "El mes:", j + 1, "no supera los: $", MONTO, "de ventas.")
            bandera = True
        j += 2
    i += 2
if not bandera:
    print("No existen sucursales con ventas menores a $", MONTO)
# Desarrollo act 'b': Generar un vector PROMEDIO de N elementos en donde guarde el promedio de ventas de cada una de
# las sucursales.
# Mostrar el vector resultante. 25 pts.
PROMEDIO = np.empty(N, dtype=float)
# Ciclo para generar la matriz 'PROMEDIO' de ventas de cada sucursal
aux = 0
for i in range(0, N):
    suma = 0
    prom = 0
    for j in range(0, M):
        suma += sucursales[i, j]
    prom = suma / M
    PROMEDIO[aux] = prom
    aux += 1
# Ciclo para mostrar la matriz 'PROMEDIO'
print("La matriz PROMEDIO es la siguiente: ")
for i in range(0, N):
    print("%.2f" % PROMEDIO[i], end=" ")
