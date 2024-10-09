# Generar un vector con la Categoría de cada uno de los 20 alumnos de Lógica I.
# La misma se la establece a partir de la nota promedio obtenida por cada alumno
# luego de rendir tres parciales, y teniendo en consideración la siguiente tabla:
# Nota promedio           Categoría
#     0 a 5                   D
#     6 a 8                   A
#     9 a 10                  P
# Datos de entrada: 3 notas por cada uno de los 20 alumnos de Lógica I
# Datos de salida: crear un vector con la categoría a la que pertenece cada alumno
# dependiendo su promedio

import numpy as np
vector = np.empty(20, dtype=float)
i = 0
prom = 0
# Ciclo para generar el vector
while i < 5:  # Modificar este valor para aumentar la cantidad de alumnos
    c = 0
    suma = 0
    print(f"{i + 1} alumno: ")
    while c < 3:  # Ciclo para ingresar las 3 notas de cada alumno
        print(f"Ingresar la nota del {c + 1}° parcial: ")
        nota = int(input())
        suma += nota
        c += 1
    if c > 0:
        prom = suma / c
    vector[i] = prom
    i += 1
# Ciclo para mostrar el vector generado
i = 0
print("El vector generado es el siguiente: ")
while i < 5:  # Modificar este valor para aumentar la cantidad de alumnos a mostrar
    print(vector[i], end=" ")
    i += 1
