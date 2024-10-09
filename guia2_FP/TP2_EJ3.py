# El profesor de Fundamentos de la Programación desea guardar la cantidad de alumnos presentes en sus
# clases de teoría del primer cuatrimestre, las cuales son en total 12 clases. Para ello le pide:
# a.Realizar la carga de la cantidad de alumnos en el arreglo A.
# b.Determinar y mostrar la cantidad promedio de alumnos presentes.
# c.Mostrar el número de clase que registro la mayor asistencia.
# Datos de entrada: Ingresar la asistencia de alumnos en cada una de las 12 clases
# Datos de salida: Mostrar la cantidad de alumnos en el vector A
# Mostrar la cantidad promedio de alumnos presentes
# Indicar la clase que registró la mayor asistencia

import numpy as np
DIM = 12
vector = np.empty(DIM, dtype=int)
cant_alu = 0
b = False
prom = 0
mayor = 0
mayor_cant = 0

for i in range(0, DIM):  # Ciclo para generar el vector
    print(f"Ingrese la cantidad de alumnos presente en la {i + 1}° clase: ")
    asistencia = int(input())
    vector[i] = asistencia
    cant_alu += asistencia
    prom = cant_alu / DIM

    if not b:
        mayor_cant = vector[i]
        mayor = i + 1
        b = True
    elif asistencia > mayor_cant:
        mayor_cant = vector[i]
        mayor = i + 1
# Ciclo para mostrar el vector generado
print("El vector generado es el siguiente: ")
for i in range(0, DIM):
    print(vector[i], end=" ")
print(" ")

print(f"La cantidad promedio de alumnos presentes es: {prom}")
print(f"El número de clase que registró la mayor asistencia es la clase nro: {mayor}")
print(f"La cantidad de alumnos que asistió a la misma es: {mayor_cant}")
