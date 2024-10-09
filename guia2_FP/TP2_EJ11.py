# Para el arreglo del ejercicio 4 de los 20 alumnos de lógica, indicar:
# Dada una categoría, determine cuántos alumnos se encuentran en ella. Si ningún alumno obtuvo esa nota mostrar
# el mensaje “No existe ningún alumno en esa categoría”
# Indicar cuál es la categoría que tiene más alumnos.

import numpy as np
vector = np.empty(20, dtype="U1")
cant_A = 0
cant_D = 0
cant_P = 0
may_cat = 0
mayor = 0
i = 0
prom = 0
# Ciclo para generar el vector
while i < 5:  # Modificar este valor para la cantidad de alumnos
    c = 0
    suma = 0
    print(f"{i + 1} alumno: ")
    while c < 3:  # Ciclo para ingresar las 3 notas de cada alumno
        print(f"Ingresar la nota del {c + 1}° parcial: ")
        nota = int(input())
        while not 0 <= nota <= 10:
            print(f"Ingresar la nota del {c + 1}° parcial: ")
            nota = int(input())
        suma += nota
        c += 1
    if c > 0:
        prom = suma / c
    if 0 <= prom <= 5:
        vector[i] = "D"
        cant_D += 1
    elif 6 <= prom <= 8:
        vector[i] = "A"
        cant_A += 1
    elif 9 <= prom <= 10:
        vector[i] = "P"
        cant_P += 1
    print(f"Promedio del {i + 1}° alumno: %.2f" % prom)
    print(f"Pertenece a categoría: {vector[i]}")
    if cant_P > may_cat:
        may_cat = cant_P
        mayor = "P"
    elif cant_A > may_cat:
        may_cat = cant_A
        mayor = "A"
    elif cant_D > may_cat:
        may_cat = cant_D
        mayor = "D"
    else:
        mayor = "Categorías con cantidad de alumnos iguales"
    i += 1
# Ciclo para mostrar el vector generado
i = 0
print("El vector generado es el siguiente:")
while i < 5:  # Modificar este valor para la cantidad de alumnos a mostrar
    print(vector[i], end=" ")
    i += 1
print(" ")
# Mostrar la cantidad de alumnos correspondientes a cada categoría
if cant_P > 0:
    print(f"La cantidad de alumnos en la categoría 'P' son: {cant_P}")
else:
    print("No hay alumnos en la categoría 'P'")
if cant_A > 0:
    print(f"La cantidad de alumnos en la categoría 'P' son: {cant_A}")
else:
    print("No hay alumnos en la categoría 'A'")
if cant_D > 0:
    print(f"La cantidad de alumnos en la categoría 'D' son: {cant_D}")
else:
    print("No hay alumnos en la categoría 'D'")
print(f"La categoría con mayor cantidad de alumnos es: {mayor}")
