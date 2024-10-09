import numpy as np
import random

# Definición de módulos


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------\n"
          "1) Cargar películas\n"
          "2) Elegir película al azar\n"
          "0) para finalizar ingrese el '0'\n")
    op = int(input("Ingrese una opción para continuar: "))
    return op


def cargar_arreglo_de_registros(pelis, dim):
    for i in range(dim):
        pelis[i]["nombre"] = input(f"Ingrese el nombre de la {i + 1} película: ")
    return None


def elegir_peli_random(pelis, dim):
    j = random.randrange(0, dim)
    peli_sugerida = pelis[j]["nombre"]
    print(f"La película seleccionada es: {peli_sugerida}")
    return None


# Programa principal
# Estructura del registro

t_peliculas = np.dtype(
    [
        ("nombre", "U25")
    ]
)

# Arreglo de registros
dimension = int(input("Cuántas películas desea ingresar? "))
mis_peliculas = np.empty(dimension, dtype=t_peliculas)
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        salir = True
    elif opc == 1:
        cargar_arreglo_de_registros(mis_peliculas, dimension)
    elif opc == 2:
        elegir_peli_random(mis_peliculas, dimension)
