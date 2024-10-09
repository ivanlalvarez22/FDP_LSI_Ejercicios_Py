# Mostrar el mayor elemento de un vector de números enteros.

# Definición de módulos
import numpy as np


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Cargar vector")
    print("2) Mostrar vector")
    print("3) Mostrar el mayor elemento")
    print("Ingrese el '0' para finalizar.")


def cargar_vector(v, dim):
    for i in range(dim):
        v[i] = int(input(f"Ingrese el {i + 1} elemento del vector: "))
    return vector


def mostrar_vector(v, dim):
    print(end="[ ")
    for i in range(dim):
        print(v[i], end=" ")
    print("]")
    return None


def mostrar_mayor(v, dim):
    mayor = 0
    for i in range(dim):
        if i == 0:
            mayor = v[i]
        if v[i] > mayor:
            mayor = v[i]
    return mayor


# Programa principal
bandera = False
salir = False
vector = ""
dimension = ""
while not salir:
    mostrar_menu()
    opc = int(input("Por favor ingrese una opción para continuar: "))
    if opc == 0:
        salir = True
    elif opc == 1:
        dimension = int(input("Ingrese la dimensión del vector: "))
        vector = np.empty(dimension, dtype=int)
        vector = cargar_vector(vector, dimension)
        bandera = True
        print("Vector cargado exitosamente")
    elif opc == 2 and bandera:
        mostrar_vector(vector, dimension)
    elif opc == 3 and bandera:
        print(f"El mayor elemento de la matriz es el: ", mostrar_mayor(vector, dimension))
    else:
        print("Debes cargar el vector primero")
