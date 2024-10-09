import numpy as np

ALUMNOS = 20  # ALUMNOS = 20
PARCIALES = 3  # PARCIALES = 3
category = np.empty(ALUMNOS, dtype="U1")
sum = 0
i = 0
j = 0
while i < ALUMNOS:
    while j < PARCIALES:
        nota = -1
        while nota < 0 or nota > 10:
            nota = int(
                input(
                    f"Ingrese la nota del {j+1}º parcial"
                    f" del {i+1}º alumno(0-10): "
                )
            )
        sum += nota
        j += 1
    prom = int(sum / PARCIALES)
    if 0 <= prom <= 5:
        category[i] = "D"
    elif 6 <= prom <= 8:
        category[i] = "A"
    else:
        category[i] = "P"
    sum = 0
    j = 0
    i += 1
cat_ing = ""
while cat_ing != "D" and cat_ing != "A" and cat_ing != "P":
    cat_ing = input("Ingrese una categoría(D, A, P): ").upper()
cant_cat = 0
i = 0
while i < ALUMNOS:
    if category[i] == cat_ing:
        cant_cat += 1
    i += 1
cant_d = 0
cant_a = 0
cant_p = 0
i = 0
while i < ALUMNOS:
    if category[i] == "D":
        cant_d += 1
    elif category[i] == "A":
        cant_a += 1
    else:
        cant_p += 1
    i += 1
if cant_cat > 0:
    print(f"La cantidad de alumnos en la categoría {cat_ing} es: {cant_cat}")
else:
    print("No existe ningún alumno en esa categoría.")
if cant_d > cant_a and cant_d > cant_p:
    print(f"La categoría con mas alumnos es D, con {cant_d} alumnos.")
elif cant_a > cant_d and cant_a > cant_p:
    print(f"La categoría con mas alumnos es A, con {cant_a} alumnos.")
elif cant_p > cant_a and cant_p > cant_d:
    print(f"La categoría con mas alumnos es P, con {cant_p} alumnos.")
else:
    print("Hay mas de una categoría con la mayor cantidad de alumnos.")
