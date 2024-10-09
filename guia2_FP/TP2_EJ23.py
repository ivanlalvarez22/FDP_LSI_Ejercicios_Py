# Para una matriz cuadrada W de 6x6 elementos, mostrar:
# a.La suma de los valores de la triangular superior.
# b.El promedio de los valores de la triangular inferior.
# c.La cantidad de valores múltiplos de 5 de la diagonal principal.
# d.El menor valor de las filas pares y en qué posición del arreglo está.
# e.Los valores de una determinada columna.
import numpy as np
# Carga estática de la matriz W
W = np.array(([1, 2, 3, 4, 5, 6], [4, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6],
              [9, 9, 7, 8, 8, 9], [1, 2, 3, 4, 5, 6], [6, 6, 6, 5, 6, 6]))
# Ciclo para mostrar la matriz W
for i in range(0, 6):
    for j in range(0, 6):
        print(W[i, j], end=" ")
    print(" ")
# Ciclo para mostrar la triangular superior
print("La matriz triangular superior es la siguiente: ")
for i in range(0, 6):
    for j in range(0, 6):
        if j > i:
            print(W[i, j], end=" ")
    print(" ")
# ACTIVIDAD A Ciclo para calcular la suma de elementos de la triangular superior
sumTS = 0
for i in range(0, 6):
    for j in range(0, 6):
        if j > i:
            sumTS += W[i, j]
print("La suma de los elementos de la triangular superior es: ", sumTS)
# Ciclo para mostrar la triangular inferior
print("La matriz triangular inferior es la siguiente: ")
for i in range(0, 6):
    for j in range(0, 6):
        if j < i:
            print(W[i, j], end=" ")
    print(" ")
# ACTIVIDAD B Ciclo paara calcular el promedio de los valores de la triagular inferior
conTI = 0
sumTI = 0
for i in range(0, 6):
    for j in range(0, 6):
        if j < i:
            sumTI += W[i, j]
            conTI += 1
promTI = sumTI / conTI
print("El promedio de los valores de la triangular inferior es: ", promTI)
# ACTIVIDAD C: Ciclo para calcular la cantidad de valores múltiplos de 5 de la diagonal principal
conMul5 = 0
for i in range(0, 6):
    if W[i, i] % 5 == 0:  # Forma optimizada de recorrer la diagonal principal
        conMul5 += 1
print("La cantidad de valores múltiplos de 5 de la diagonal principal son: ", conMul5)
# ACTIVIDAD D Ciclo para mostrar el menor valor de las filas pares y en qué posición del arreglo está
menValFP = 0
menPos = 0
i = 1
while i < 6:
    bandera = False
    for j in range(0, 6):
        if not bandera:
            menPos = j
            menValFP = W[i, j]
            bandera = True
        if W[i, j] < menValFP:
            menValFP = W[i, j]
            menPos = j
    print(f"El menor valor de la {i + 1}° fila es el: {menValFP}")
    print(f"La posición del mismo es: {menPos + 1}")
    i += 2
# ACTIVIDAD E: Ciclo para mostrar los valores de una determinada columna
print("Ingresar la columna a mostrar: ")
COLUMNA = int(input())
print(f"La columna seleccionada es la {COLUMNA}: ")
for i in range(0, 6):
    for j in range(0, 6):
        if j == COLUMNA - 1:  # Restamos 1 unidad a la columna porque Python inicia con j = 0 por defecto
            print(W[i, j], end=" ")
    print(" ")
