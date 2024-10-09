# Codificar en lenguaje Python los módulos que se detallan a continuación, debiendo respetar con lo
# especificado en los mismos. Verificar si se obtienen el/los resultado/s esperado/s.

# ********************************************************************************************************************

# Nombre: PorcentajeColumna
# Descripción: retorna el porcentaje de valores de las columnas impares
# cuyo dígito de las unidades sea divisor de un determinado número.
# Datos de Entrada: W, dimW, num
# Datos de Salida: PorcentajeColumna
# 25 Ptos.

# ********************************************************************************************************************

# Nombre: DatosTriangular
# Descripción: retorna el promedio de los valores de la triangular
# inferior que sean capicúas, tomando en cuenta solamente
# aquellos valores de tres dígitos; y el mayor valor de los que no son
# capicúas independientemente de la cantidad de dígitos.
# Datos de Entrada: W, dimW
# Datos de Salida: promedio, mayor
# 25 Ptos.

import numpy as np

# Definición de módulos


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------\n"
          "1) Cargar matriz w\n"
          "2) Mostrar matriz w\n"
          "3) Realizar actividad a)\n"
          "4) Realizar actividad b)")
    op = int(input("Ingrese una opción para continuar: "))
    return op


def mostrar_matriz(w, dimw):
    for i in range(dimw):
        for j in range(dimw):
            print(w[i, j], end=" ")
        print("")
    return None


# Nombre: porcentaje_columna
# Descripción: retorna el porcentaje de valores de las columnas impares
# cuyo dígito de las unidades sea divisor de un determinado número.
# Datos de Entrada: W, dimW, num
# Datos de Salida: PorcentajeColumna
def porcentaje_columna(w, dimw, num):
    total = 0
    cant = 0
    j = 0
    while j < dimw:
        for i in range(dimw):
            total += 1
            digito_unidad = w[i, j] % 10
            if digito_unidad != 0 and num % digito_unidad == 0:
                cant += 1
        j += 2
    porc_columna = (cant * 100) / total
    return porc_columna


# Nombre: DatosTriangular
# Descripción: retorna el promedio de los valores de la triangular
# inferior que sean capicúas, tomando en cuenta solamente
# aquellos valores de tres dígitos; y el mayor valor de los que no son
# capicúas independientemente de la cantidad de dígitos.
# Datos de Entrada: W, dimW
# Datos de Salida: promedio, mayor
def datos_triangular(w, dimw):
    mayor = 0
    suma = 0
    cant = 0
    for i in range(dimw):
        for j in range(dimw):
            if i > j:
                if es_capicua(w[i, j]) and 100 <= w[i, j] <= 999:
                    suma += w[i, j]
                    cant += 1
            if w[i, j] >= mayor and not es_capicua(w[i, j]):
                mayor = w[i, j]
    promedio = suma / cant
    return promedio, mayor


def es_capicua(num):
    es_cap = False
    if num % 10 == num // 100:
        es_cap = True
    return es_cap


# Programa Principal

matriz_w = np.empty([5, 5], dtype=int)
dimension_w = 5
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado")
        salir = True
    elif opc == 1:
        matriz_w = np.array([[586, 8, 64, 271, 121],
                            [656, 6, 122, 97, 207],
                            [95, 156, 384, 11, 9],
                            [535, 4, 75, 52, 40],
                            [8, 757, 29, 515, 739]])
        print("Matriz cargada correctamente")
    elif opc == 2:
        mostrar_matriz(matriz_w, dimension_w)
    elif opc == 3:
        n = int(input("Ingrese un número para continuar: "))
        porcentaje = porcentaje_columna(matriz_w, dimension_w, n)
        print(porcentaje)
    elif opc == 4:
        prom, may = datos_triangular(matriz_w, dimension_w)
        print(f"El promedio es: {prom}\n"
              f"El mayor valor de la triangular inferior que no es capicúa es: {may}")
