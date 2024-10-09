# Dado un número X, mostrar la posición en la que se encuentra dentro de un vector.

# Definición de módulos
import numpy as np


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Cargar vector")
    print("2) Mostrar vector")
    print("3) Mostrar posición")
    print("Ingrese el '0' para finalizar.")


def cargar_vector(v, dim):
    for i in range(dim):
        v[i] = int(input(f"ingrese el {i + 1} elemento del vector: "))
    return vector


def mostrar_vector(v, dim):
    print(end="[ ")
    for i in range(dim):
        print(v[i], end=" ")
    print("]")
    return None


def mostrar_posicion(v, dim, x):
    b = False
    posicion = ""
    for i in range(dim):
        if x == v[i]:
            posicion = i + 1
            b = True
    if b:
        print(f"El número {x} se encuentra en la {posicion}° posición")
    else:
        print("Elemento no encontrado")
    return None


# Programa principal
bandera = False
salir = False
dimension = ""
vector = ""
while not salir:
    mostrar_menu()
    opc = int(input("Por favor ingrese una opción para continuar: "))
    if opc == 0:
        salir = True
    elif opc == 1:
        dimension = int(input("Ingrese la dimensión del vector: "))
        vector = np.empty(dimension, dtype=int)
        cargar_vector(vector, dimension)
        bandera = True
        print("Vector cargado exitosamente")
    elif opc == 2:
        if bandera:
            mostrar_vector(vector, dimension)
        else:
            print("Debes cargar el vector primero")
    elif opc == 3:
        if bandera:
            num = int(input("Ingrese un número para mostrar su posición: "))
            mostrar_posicion(vector, dimension, num)
        else:
            print("Debes cargar el vector primero")
    else:
        print("Opción inválida")
