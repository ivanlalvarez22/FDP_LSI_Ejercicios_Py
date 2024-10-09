# Una empresa desea almacenar la edad de sus 20 empleados. Indicar la cantidad de empleados que
# se encuentran en cada una de las siguientes categorías:
# * Mayores de 45 años
# * Entre 30 y 40 años inclusive
# * De 18 años
# Datos de entrada: la edad de 20 empleados
# Datos de salida: Mostrar la cantidad de mayores de 45 años
# Mostrar la cantidad de empleados entre 30 y 40 años
# Mostrar la cantidad de empleados con 18 años

import numpy as np
vector = np.empty(20, dtype=int)  # Definimos le vector para 20 empleados
cant_45 = 0
cant_30_40 = 0
cant_18 = 0
i = 0
while i < 20:  # Ciclo para recorrer y cargar el vector de forma dinámica del elemento 1 al 20
    print(f"Ingresar la edad del {i + 1} empleado: ", end=" ")
    edad = int(input())
    vector[i] = edad
    if vector[i] > 45:
        cant_45 += 1
    if 30 < vector[i] < 40:
        cant_30_40 += 1
    if vector[i] == 18:
        cant_18 += 1
    i += 1
print(" ")
# Ciclo para mostrar el vector cargado
i = 0
print("La edad de los empleados cargadas en forma de vector es: ")
while i < 20:
    print(vector[i], end=" ")
    i += 1
print(" ")

print(f"La cantidad de empleados de edad mayor a 45 son: {cant_45}")
print(f"La cantidad de empleados de edad entre 30 y 40 son: {cant_30_40}")
print(f"La cantidad de empleados con edad de 18 años son : {cant_18}")
