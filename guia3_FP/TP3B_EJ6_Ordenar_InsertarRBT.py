"""
B6. A partir de un arreglo A ordenado ascendentemente, agregar un elemento X a
ser ingresado conservando el orden. Mostrar el vector resultante
"""
import numpy as np
from os import system as console


#
def print_menu():
    print(
        "\n[MENU PRINCIPAL]\n"
        "1- Cargar los datos en el vector A.\n"
        "2- Ordenar el vector A en forma ascendente.\n"
        "3- Insertar elemento X en el vector A.\n"
        "4- Mostrar el vector A.\n"
        "5- Limpiar la pantalla.\n"
        "0- Salir"
    )


#
def load_vector(vector, dim):
    for i in range(dim):
        vector[i] = int(input(f"Ingrese el {i + 1}º elemento de A: "))


#
def sort_vector(vector, dim):
    for i in range(dim - 1):
        p = i  # p = indice del menor valor
        for j in range(i + 1, dim):
            if vector[j] < vector[p]:
                p = j
        aux = vector[p]
        vector[p] = vector[i]
        vector[i] = aux


#
def insert(vector, dim):
    num = int(input("\nElemento a insertar: "))
    is_insert = False
    i = 0
    while i < dim and not is_insert:
        if num < vector[i]:
            j = dim - 1
            while j >= i:
                vector[j + 1] = vector[j]
                j -= 1
            vector[i] = num
            dim += 1
            is_insert = True
        else:
            i += 1
    if not is_insert:
        vector[i] = num
        dim += 1
    return dim, num


#
def print_vector(vector, dim):
    print("[", end="")
    for i in range(dim):
        if i < dim - 1:
            print(vector[i], end=", ")
        else:
            print(vector[i], end="]\n")


#
def main():
    console("color 01")
    print("_____PROGRAMA INICIADO_____")
    is_loaded = False
    is_sort = False
    run = True
    while run:
        print_menu()
        command = int(input("\nSeleccione una opción: "))
        if command == 0:
            run = False
            print("\n_____PROGRAMA FINALIZADO_____")
        elif command == 1:
            dim_a = int(
                input(
                    "\nIngrese la dimensión del vector A: "
                )
            )
            vector_a = np.empty(100, dtype=int)
            load_vector(vector_a, dim_a)
            is_loaded = True
            is_sort = False
            print("Vector A cargado.")
        elif command == 2:
            if is_loaded:
                sort_vector(vector_a, dim_a)
                is_sort = True
                print("El vector A se ha ordenado.")
            else:
                print("El vector no está cargado.")
        elif command == 3:
            if is_loaded and is_sort:
                dim_a, num_x = insert(vector_a, dim_a)
                print(f"El número {num_x} se ha insertado en el vector A.\n")
            else:
                print("El vector no está cargado o no está ordenado.")
        elif command == 4:
            if is_loaded:
                print("\nVector A:")
                print_vector(vector_a, dim_a)
            else:
                print("El vector no está cargado.")
        elif command == 5:
            console("cls")
        else:
            print("Comando inválido")


# Programa principal.
main()
