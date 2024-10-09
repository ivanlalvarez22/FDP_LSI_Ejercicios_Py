# Para N números, indicar cuantos son de tres dígitos y múltiplos de 4.
import numpy as np

# Definición de módulos


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Ingresar números")
    print("2) Mostrar números de 3 dígitos y múltiplos de 4")
    print("3) Mostrar números ingresados")
    print("Ingrese el '0' para finalizar.")


def ingresar_numeros(v, dim):
    for i in range(dim):
        v[i] = int(input(f"Ingrese el {i + 1}° número: "))
    return vector


def mostrar_cantidad(v, dim):
    cant = 0
    for i in range(dim):
        if 100 <= v[i] <= 999 and v[i] % 4 == 0:
            cant = cant + 1
    return cant


def mostrar_numeros(v, dim):
    print("Los números ingresados son los siguientes: ")
    print(end="[ ")
    for i in range(dim):
        print(v[i], end=" ")
    print("]")


# Programa principal
salir = False
bandera = False
dimension = ""
vector = ""
while not salir:
    mostrar_menu()
    opc = int(input("Por favor ingrese una opción para continuar: "))
    if opc == 0:
        salir = True
    elif opc == 1:
        dimension = int(input("¿Cuántos números desea ingresar?: "))
        vector = np.empty(dimension, dtype=int)
        ingresar_numeros(vector, dimension)
        bandera = True
        print("Vector cargado...")
    elif opc == 2:
        if bandera:
            print(f"La cantidad de números de 3 cifras múltiplos de 4 son: {mostrar_cantidad(vector, dimension)}")
        else:
            print("Debe ingresar previamente algún número")
    elif opc == 3:
        if bandera:
            mostrar_numeros(vector, dimension)
        else:
            print("Primero debería ingresar algún número")
