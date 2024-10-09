# Para el arreglo del ejercicio 4 de los 20 alumnos de lógica, indicar:
# Dada una categoría, determine cuántos alumnos se encuentran en ella. Si ningún alumno obtuvo esa nota mostrar
# el mensaje “No existe ningún alumno en esa categoría”
# Indicar cuál es la categoría que tiene más alumnos.

import numpy as np
DIM = 10
categoria = np.array(['D', 'D', 'A', 'D', 'A', 'P', 'A', 'P', 'D', 'P'])
# Apartado A
categoriaBuscar = (input("Ingrese la categoría a buscar (P/A/D): "))
cAlumnos = 0
for i in range(0, 10):
    if categoria[i] == categoriaBuscar.upper():
        cAlumnos += 1
# Ciclo para mostrar el vector
print("El vector es el siguiente: ")
for i in range(0, 10):
    print(categoria[i], end=" ")
print(" ")
if cAlumnos == 0:
    print("No existen alumnos en esa categoría")
else:
    print(f"La cantidad de alumnos en esa categoría es: {cAlumnos}")
cCategoriaA = 0
cCategoriaP = 0
cCategoriaD = 0
for i in range(0, 10):
    if categoria[i] == "D":
        cCategoriaD += 1
    elif categoria[i] == "A":
        cCategoriaA += 1
    elif categoria[i] == "P":
        cCategoriaP += 1
if cCategoriaP > cCategoriaA:
    print(f"La categoría con más alumnos es la P con {cCategoriaP} alumnos")
elif cCategoriaA > cCategoriaD:
    print(f"La categoría con más alumnos es la A con {cCategoriaA} alumnos ")
else:
    print(f"La categoría con más alumnos es la D con {cCategoriaD} alumnos")
