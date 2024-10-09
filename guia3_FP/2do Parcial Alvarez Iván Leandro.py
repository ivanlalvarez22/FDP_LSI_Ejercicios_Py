# Nombre: Alvarez Iván Leandro
# DNI: 38484357

# Nombre: PromedioColumna

# Descripción: retorna el promedio de valores de las columnas pares cuyo digito de
# las unidades sea par y mayor a un determinado número.

# Datos de Entrada: W, dimW, num

# Datos de Salida: PromedioColumna

# 25 Ptos.

# Definición de módulos

import numpy as np

def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Mostrar matriz")
    print("2) Obtener promedio")
    print("Ingrese el '0' para finalizar")


def mostrar_matriz(w, dimw):
    for i in range(dimw):
        for j in range(dimw):
            print(w[i, j], end=" ")
        print(" ")



# Programa Principal
dimW = 5
matrizW = np.empty((dimW), dtype=int)
matrizW = np.array([[586, 8, 64, 271, 125],
                    [656, 6, 122, 97, 207],
                    [92, 156, 384, 11, 9],
                    [535, 4, 73, 52, 45],
                    [8, 757, 29, 518, 739]])
salir = False
while not salir:
    mostrar_menu()
    opc = int(input("Por favor ingrese una opción para continuar: "))
    if opc == 0:
        salir = True
    elif opc == 1:
        dimw = [5,5]
        matrizW = np.array([[586, 8, 64, 271, 125],
                            [656, 6, 122, 97, 207],
                            [92, 156, 384, 11, 9],
                            [535, 4, 73, 52, 45],
                            [8, 757, 29, 518, 739]])
        mostrar_matriz(matrizW, dimW)
