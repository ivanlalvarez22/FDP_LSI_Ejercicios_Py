# Determinar el mayor y el menor elemento de un vector de números enteros

# Definición de módulos
import numpy as np
import random


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Cargar vector")
    print("2) Cargar vector (random)")
    print("3) Mostrar vector")
    print("4) Mostrar mayor elemento")
    print("5) Mostrar menor elemento")
    print("Ingrese el '0' para finalizar.")
    return None


def cargar_vector(v, dim):
    print("Se cargará el vector manualmente..")
    for i in range(dim):
        v[i] = int(input(f"Ingrese el {i + 1}° elemento del vector: "))
    print("Vector correctamente cargado")
    return None


def cargar_random(v, dim):
    print("Se realizará una carga aleatoria del vector")
    for i in range(dim):
        v[i] = random.randrange(0, 100)
    print("Vector cargado exitosamente")
    return None


def mostrar_vector(v, dim):
    print("[ ", end="")
    for i in range(dim):
        print(v[i], end=" ")
    print("]")
    return None


def mostrar_mayor(v, dim):
    mayor = ""
    for i in range(dim):
        if i == 0:
            mayor = v[i]
        elif v[i] >= mayor:
            mayor = v[i]
    print(f"El mayor elemento es: {mayor}")
    return None


def mostrar_menor(v, dim):
    menor = ""
    for i in range(dim):
        if i == 0:
            menor = v[i]
        elif v[i] <= menor:
            menor = v[i]
    print(f"El menor elemento es: {menor}")
    return None


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
        cargar_vector(vector, dimension)
        bandera = True
    elif opc == 2:
        dimension = int(input("Ingrese la dimensión del vector: "))
        vector = np.empty(dimension, dtype=int)
        cargar_random(vector, dimension)
        bandera = True
    elif opc == 3:
        if bandera:
            mostrar_vector(vector, dimension)
        else:
            print("Ingrese la opción 1")
    elif opc == 4:
        if bandera:
            mostrar_mayor(vector, dimension)
        else:
            print("Primero debe cargar el vector")
    elif opc == 5:
        if bandera:
            mostrar_menor(vector, dimension)
        else:
            print("Primero cargue el vector")
    else:
        print("Opción incorrecta!")
