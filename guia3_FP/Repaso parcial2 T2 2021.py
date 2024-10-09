# Codificar en lenguaje Python los módulos que se detallan a continuación, debiendo respetar con lo
# especificado en los mismos. Verificar si se obtienen el/los resultado/s esperado/s.

# ********************************************************************************************************************

# Nombre: PromedioColumna
# Descripción: retorna el promedio de valores de las columnas pares cuyo dígito de las unidades sea par y mayor a un
# determinado número.
# Datos de entrada: W, dimW, num
# Datos de Salida: PromedioColumna

# 25 Ptos.

# ********************************************************************************************************************

# Nombre: Datos Triangular
# Descripción: retorna el porcentaje de los valores de la triangular superior que sean capicúas, tomando en
# cuenta solamente aquellos valores de tres dígitos; y el menor valor de los que no son capicúas
# independientemente de la cantidad de dígitos.
# Datos de entrada: W, dimW
# Datos de salida: promedio, menor

# 25 Ptos.


import numpy as np

# Definición de módulos


# Nombre: mostrar_menu
# Descripción: menú interactivo con el usuario
# Datos de entrada:
# Datos de salida: un número de opción tipeada por el usuario
def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------\n"
          "1) Cargar matriz\n"
          "2) Mostrar matriz W\n"
          "3) Realizar actividad a)\n"
          "4) Realizar actividad b)\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


# Nombre: mostrar_matriz
# Descripción: nos muestra la matriz previamente cargada
# Datos de entrada: la matriz w y su dimensión
# Datos de salida:
def mostrar_matriz(w, dim_w):
    for i in range(dim_w):
        for j in range(dim_w):
            print(w[i, j], end=" ")
        print("")
    return None


# Nombre: promedio_columna
# Descripción: retorna el promedio de valores de las columnas pares cuyo dígito de las unidades sea par y mayor a un
# determinado número.
# Datos de entrada: W, dimW, num
# Datos de Salida: PromedioColumna
def promedio_columna(w, dimw, num):
    j = 1
    suma = 0
    cant = 0
    # Para recorrer la matriz en sentido norte-sur usaremos de ciclo externo al índice de las columnas 'j'
    # Para recorrerla en sentido oeste-este usuaríamos de ciclo externo al índice 'i'
    while j < dimw:
        for i in range(dimw):
            digito_unidad = w[i, j] % 10
            if digito_unidad % 2 == 0 and digito_unidad > num:
                suma += w[i, j]
                cant += 1
        j += 2
    prom_columna = obtener_promedio(suma, cant)
    return prom_columna


# Nombre: obtener_promedio
# Descripción: según una suma y una cantidad nos devuelve un promedio
# Datos de entrada: suma y cantidad
# Datos de salida: promedio
def obtener_promedio(suma, cant):
    promedio = suma / cant
    return promedio


# Nombre: datos_triangular
# Descripción: retorna el porcentaje de los valores de la triangular superior que sean capicúas, tomando en
# cuenta solamente aquellos valores de tres dígitos; y el menor valor de los que no son capicúas
# independientemente de la cantidad de dígitos.
# Datos de entrada: W, dimW
# Datos de salida: promedio, menor
def datos_triangular(w, dimw):
    total = 0
    cant = 0
    men = 1000
    for i in range(dimw):
        for j in range(dimw):
            if j > i:
                if 100 <= w[i, j] <= 999:
                    total += 1
                    if es_capicua(w[i, j]):
                        cant += 1
                if w[i, j] <= men:
                    men = w[i, j]
    porcentaje = (cant * 100) / total
    return porcentaje, men


# Nombre: es_capicua
# Descripción: nos devuelve V o F dependiendo si un número de 3 cifras es capicúa o no
# Datos de entrada: un número
# Datos de salida: un valor booleano V o F
def es_capicua(num):
    b = False
    # La operación '//' me devuelve la parte entera luego de haber dividido por algún número
    if num % 10 == num // 100:
        b = True
    return b


# ******** Programa Principal ********

matriz_w = np.empty([5, 5], dtype=int)
dimension_w = 5
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado")
        salir = True
    elif opc == 1:
        matriz_w = np.array(([586, 8, 64, 271, 125],
                             [656, 6, 122, 97, 207],
                             [92, 156, 384, 11, 9],
                             [535, 4, 73, 52, 45],
                             [8, 757, 29, 518, 739]))
        print("Matriz cargada exitosamente")
    elif opc == 2:
        mostrar_matriz(matriz_w, dimension_w)
    elif opc == 3:
        x = int(input("Ingrese un número para continuar: "))
        print(promedio_columna(matriz_w, dimension_w, x))
    elif opc == 4:
        porc, menor = datos_triangular(matriz_w, dimension_w)
        print(f"El menor valor de la triangular superior que no es capicúa es el: {menor}\n"
              f"El porcentaje de números capicúas de 3 cifras es: {porc}")
