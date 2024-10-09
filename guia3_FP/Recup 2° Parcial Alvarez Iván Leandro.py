"""Apellido: Alvarez               DNI:    38484357           CARRERA: LSI
   Nombre:   Iván Leandro          LEGAJO: 458/2021"""

# B. Codificar en lenguaje Python los módulos que se detallan a continuación, debiendo respetar con lo especificado en
# los mismos. Verificar si se obtienen el/los resultado/s esperado/s.

# Nombre: CantidadSucursales
# Descripción: retorna la cantidad de sucursales que tuvieron ventas en el primer cuatrimestre del año mayores a un
# determinado valor y mùltiplos de 8.
# Datos de entrada: B, dimB, num
# Datos de salida: CantidadSucursales                                        (25 ptos.)


# Nombre: DatosMes
# Descripción: retorna el mes que mayor venta tuvo la empresa y la menor venta registrada en todo el semestre.
# Datos de entrada: B, dimB
# Datos de salida: nombre del mes, menor                                     (25 ptos.)

import numpy as np


# Definición de módulos


# Nombre: mostrar_menu
# Descripción: menú interactivo con el usuario
# Datos de entrada:
# Datos de salida: un número de opción tipeada por el usuario
def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------\n"
          "1) Cargar matriz B\n"
          "2) Mostrar matriz B\n"
          "3) Realizar actividad 1a)\n"
          "4) Realizar actividad 1b)\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


# Nombre: mostrar_matriz
# Descripción: nos muestra la matriz previamente cargada
# Datos de entrada: la matriz b y su dimensión
# Datos de salida:
def mostrar_matriz(b, dimb_fil, dimb_col):
    for i in range(dimb_fil):
        for j in range(dimb_col):
            print(b[i, j], end=" ")
        print("")
    return None


# Nombre: cantidad_sucursales
# Descripción: retorna la cantidad de sucursales que tuvieron ventas en el primer cuatrimestre del año mayores a un
# determinado valor y mùltiplos de 8.
# Datos de entrada: B, dimB, num
# Datos de salida: CantidadSucursales
def cantidad_sucursales(b, dimb_fil, dimb_col, num):
    cant_sucursales = 0
    for i in range(dimb_fil - 2):
        for j in range(dimb_col):
            if b[i, j] > num and b[i, j] % 8 == 0:
                cant_sucursales += 1
    return cant_sucursales


# Nombre: datos_mes
# Descripción: retorna el mes que mayor venta tuvo la empresa y la menor venta registrada en todo el semestre.
# Datos de entrada: B, dimB
# Datos de salida: nombre del mes, menor
def datos_mes(b, dimb_fil, dimb_col):
    mes_con_mayor_ventas = 0
    cant_ventas_mes = 0
    menor = 1000
    for i in range(dimb_fil):
        total_mes_may_venta = 0
        for j in range(dimb_col):
            total_mes_may_venta += b[i, j]
            if b[i, j] <= menor:
                menor = b[i, j]
        if total_mes_may_venta >= cant_ventas_mes:
            cant_ventas_mes = total_mes_may_venta
            mes_con_mayor_ventas = i
    nombre_del_mes = convertir_num_a_string(mes_con_mayor_ventas + 1)
    return nombre_del_mes, menor


# Nombre del módulo: convertir_num_a_string
# Descripción: convierte los números de los meses a sus respectivos nombres
# Datos de entrada: num (número de mes)
# Datos de salida: string (nombre del mes)
def convertir_num_a_string(num):
    string = ""
    if num == 1:
        string = "enero"
    elif num == 2:
        string = "febrero"
    elif num == 3:
        string = "marzo"
    elif num == 4:
        string = "abril"
    elif num == 5:
        string = "mayo"
    elif num == 6:
        string = "junio"
    return string


# ************ Programa Principal ************

matriz_b = np.empty([6, 5], dtype=int)
dimension_b_filas = 6
dimension_b_columnas = 5
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("¡Programa finalizado!")
        salir = True
    elif opc == 1:
        matriz_b = np.array([[170, 652, 278, 670, 587],
                            [389, 167, 174, 352, 391],
                            [178, 955, 664, 188, 192],
                            [565, 369, 581, 850, 793],
                            [177, 157, 165, 198, 195],
                            [678, 398, 815, 545, 638]])
        print("\nMatriz B cargada correctamente\n")
    elif opc == 2:
        print("La matriz B es la siguiente: \n")
        mostrar_matriz(matriz_b, dimension_b_filas, dimension_b_columnas)
        print("")
    elif opc == 3:
        n = int(input("Por favor ingrese un número para continuar: "))
        cantidad_de_sucursales = cantidad_sucursales(matriz_b, dimension_b_filas, dimension_b_columnas, n)
        print(f"\nLa cantidad de sucursales con ventas en el 1° cuatrimestre mayores a"
              f" {n} y múltiplos de 8 son: {cantidad_de_sucursales}\n")
    elif opc == 4:
        nombre_mes, menor_venta_registrada = datos_mes(matriz_b, dimension_b_filas, dimension_b_columnas)
        print(f"\nEl mes en el cual la empresa tuvo la mayor venta fue el mes de: {nombre_mes}\n"
              f"La menor venta registrada en todo el semestre fue de : ${menor_venta_registrada}\n")
