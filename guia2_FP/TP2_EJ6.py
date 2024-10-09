# Dado un vector B que contiene las ganancias mensuales de los años 2018 y 2019,
# mostrar la mayor ganancia de cada uno de los trimestres pares de cada año.

import numpy as np
B = np.empty(24, dtype=int)
TRIM = np.empty(8, dtype=int)
suma = 0
i = 0
j = 1
k = 0
# Ciclo para cargar el vector B
while i < 24:
    print(f"Ingresar las ganancias del {i + 1}° mes: ", end="")
    ganancias = int(input())
    B[i] = ganancias
    suma += ganancias
    if j == 3:  # Condición para sumar los trimestres
        TRIM[k] = suma
        suma = 0
        j = 0
        k += 1
    j += 1
    i += 1
# Ciclo para mostrar el vector B generado
i = 0
print("El vector generado es el siguiente: ")
while i < 24:
    print(B[i], end=" ")
    i += 1
print(" ")
# Ciclo para mostrar el vector trimestre
print("El vector trimestre generado es: ")
k = 0
while k < 8:
    print(TRIM[k], end=" ")
    k += 1
print(" ")
# Calculamos el trimestre con mayor ganancias
if TRIM[1] > TRIM[5]:
    mayor_ganan2 = TRIM[1]
    mayor_trim2 = 2018
else:
    mayor_ganan2 = TRIM[5]
    mayor_trim2 = 2019
if TRIM[3] > TRIM[7]:
    mayor_ganan4 = TRIM[3]
    mayor_trim4 = 2018
else:
    mayor_ganan4 = TRIM[7]
    mayor_trim4 = 2019

print("El 2do trimestre que generó mayor ganancias fue en el año: %d" % mayor_trim2)
print(f"La cantidad de ganancias del mismo fue: ${mayor_ganan2}")
print("El 4to trimestre que generó mayor ganancias fue en el año: %d" % mayor_trim4)
print(f"La cantidad de ganancias del mismo fue: ${mayor_ganan4}")
