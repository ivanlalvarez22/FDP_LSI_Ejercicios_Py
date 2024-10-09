# Cargar  los  datos  en  el  vector.  Ordenarlo  en  forma  ascendente
# un  vector  A  de  10  elementos,  y  por  ultimo mostrarlo ordenado.

# Definición de módulos
import numpy as np
import random


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Cargar vector")
    print("2) Cargar vector (random)")
    print("3) Mostrar vector")
    print("4) Ordenar ascendentemente vector")
    print("Ingrese el '0' para finalizar")


def cargar_vector(v, dim):
    for i in range(dim):
        v[i] = int(input(f"Ingrese el {i + 1}° elemento del vector: "))
    print("Vector cargado correctamente")
    return None


def cargar_vector_random(v, dim):
    for i in range(dim):
        v[i] = random.randrange(0, 100)  # Carga random del vector en un rango de 0 a 100
    print("Se cargó un vector de forma aleatoria")


def mostrar_vector(v, dim):
    print("El vector ingresado es el siguiente: ")
    print("[ ", end="")
    for i in range(dim):
        print(v[i], end=" ")
    print("]")
    return None


def ordenar_vector(v, dim):
    n = dim - 1
    b = 1
    while b != 0:
        b = 0
        i = 0
        while i < n:
            if v[i] > v[i + 1]:  # Condición para determinar el orden ascendente o descendente
                aux = v[i]
                v[i] = v[i + 1]
                v[i + 1] = aux
                b = 1
            i += 1
    print("El vector fue ordenado exitosamente!")
    return None


# Programa principal
bandera = False
salir = False
dimension = 5
vector = np.empty(dimension, dtype=int)

while not salir:
    mostrar_menu()
    opc = int(input("Por favor ingrese una opción para continuar: "))
    if opc == 0:
        salir = True
    elif opc == 1:
        cargar_vector(vector, dimension)
        bandera = True
    elif opc == 2:
        cargar_vector_random(vector, dimension)
        bandera = True
    elif opc == 3:
        if bandera:
            mostrar_vector(vector, dimension)
        else:
            print("Ingrese a la opción 1 para continuar")
    elif opc == 4:
        if bandera:
            ordenar_vector(vector, dimension)
        else:
            print("Debe ingresar la opción 1")
    else:
        print("Opción inválida!")
