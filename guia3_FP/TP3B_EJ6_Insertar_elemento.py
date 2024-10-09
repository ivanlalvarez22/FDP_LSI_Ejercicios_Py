# A partir de un arreglo A ordenado ascendentemente, agregar un
# elemento X a ser ingresado conservando el orden. Mostrar el vector resultante

import numpy as np
import random

# Definición de módulos


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Cargar vector manualmente")
    print("2) Cargar vector random")
    print("3) Mostrar vector")
    print("4) Ordenar ascendentemente el vector")
    print("5) Insertar elemento al vector")
    print("Ingrese el '0' para finalizar.")
    return None


def cargar_vector(v, dim):
    print("Se realizará la carga manual del vector..")
    for i in range(dim):
        v[i] = int(input(f"Ingrese el {i + 1}° elemento del vector: "))
    print("Vector cargado exitosamente")
    return None


def cargar_random(v, dim):
    print("Se cargará un vector de manera aleatoria..")
    for i in range(dim):
        v[i] = random.randrange(0, 100)
    print("Se asignaron valores aleatorios al vector")
    return None


def mostrar_vector(v, dim):
    print("El vector ingresado es el siguiente: ")
    print("[ ", end="")
    for i in range(dim):
        print(v[i], end=" ")
    print("]")
    return None


def ordenar_vector(v, dim):
    print("Se ordenará el vector de forma ascendente..")
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


def insertar_elemento(v, dim):
    num = int(input("Ingrese el elemento a insertar: "))
    b = 0
    i = 0
    while i < dim and b == 0:
        if num < v[i]:
            j = dim - 1
            while j >= i:
                v[j + 1] = v[j]
                j -= 1
            v[i] = num
            dim += 1
            b = 1
        else:
            i += 1
    if b == 0:
        v[i] = num
        dim += 1
    return dim, num


# Programa principal
bandera = False
salir = False
ordenado = False
vector = ""
dimension = 0
while not salir:
    mostrar_menu()
    opc = int(input("Por favor ingrese una opción para continuar: "))
    if opc == 0:
        salir = True
    elif opc == 1:
        dimension = int(input("Ingrese la dimensión del vector: "))
        vector = np.empty(100, dtype=int)
        cargar_vector(vector, dimension)
        bandera = True
    elif opc == 2:
        dimension = int(input("Ingrese la dimensión del vector: "))
        vector = np.empty(100, dtype=int)
        cargar_random(vector, dimension)
        bandera = True
    elif opc == 3:
        if bandera:
            mostrar_vector(vector, dimension)
        else:
            print("Debe ingresar la opción 1")
    elif opc == 4:
        if bandera:
            ordenar_vector(vector, dimension)
            ordenado = True
        else:
            print("Debería seleccionar la opción 1")
    elif opc == 5:
        if bandera and ordenado:
            dimension, num_x = insertar_elemento(vector, dimension)
            print(f"El número {num_x} se ha insertado en el vector A.\n")
        else:
            print("Vector sin cargar o sin ordenar")
    else:
        print("Opción inválida!")
