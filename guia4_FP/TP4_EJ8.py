# Una biblioteca registra para cada uno de sus libros la siguiente información:
# Número de Inventario, Nombre del Libro, Código de Autor, Precio de Compra y
# Estado {1-Buen Estado, 2-Deteriorado, 3-Robado}. Se pide:

# a) Realizar el ingreso de los datos, cuyo final está dado por número de inventario igual a cero.

# b) Mostrar los datos de aquellos libros cuyo precio de compra sea mayor a $1075.

# c) Para un código de autor, mostrar la cantidad de libros que se tiene del mismo.

# d) Generar un arreglo con el número de inventario y el nombre de aquellos libros que estén deteriorados.

import numpy as np

# Definición de módulos


def mostrar_menu():
    print("-----------MENÚ PRINCIPAL-------------\n"
          "1) Cargar registro\n"
          "2) Mostrar registro\n"
          "3) Mostrar datos de libros mayores a un determinado precio\n"
          "4) Mostrar cantidad de libros según código de autor\n"
          "5) Generar arreglo con nro de inventario y nombre de libros deteriorados\n"
          "Ingrese el '0' para finalizar.")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


def cargar_registro(ml):
    ml[0] = (143, "Física I", 2024, 2000, 1)
    ml[1] = (164, "Física II", 2024, 3500, 1)
    ml[2] = (147, "Física III", 2024, 3000, 1)
    ml[3] = (243, "Álgebra I", 3747, 1500, 3)
    ml[4] = (262, "Álgebra II", 3747, 1000, 1)
    ml[5] = (261, "Álgebra III", 3747, 4000, 1)
    ml[6] = (364, "Informática I", 4222, 5000, 2)
    ml[7] = (354, "Informática II", 4222, 1000, 2)
    ml[8] = (387, "Informática III", 4154, 3300, 3)
    ml[9] = (447, "Redes I", 5264, 6000, 2)
    print("\n El registro fue cargado exitosamente\n")
    return None


def convertir_estado_caracter(num):
    if num == 1:
        num = "Buen estado"
    elif num == 2:
        num = "Deteriorado"
    else:
        num = "Robado"
    return num


def mostrar_registro(ml, d):
    print("NRO. INVENTARIO            NOMBRE              COD. AUTOR         PRECIO        ESTADO")
    for i in range(d):
        print(ml[i]["nro_inventario"], end="                        ")
        print(str(ml[i]["nombre"]).ljust(16), end="    ")
        print(ml[i]["codigo_autor"], end="              ")
        print("$", ml[i]["precio"], end="       ")
        print(convertir_estado_caracter(ml[i]["estado"]))
    print("-"*90)
    return None


def mostrar_datos_libros_con_determinado_precio(ml, d):
    precio = 1075
    print(f"Los datos de los libros con un precio mayor a ${precio} son: ")
    for i in range(d):
        if ml[i]["precio"] > precio:
            print(ml[i]["nro_inventario"], str(ml[i]["nombre"]).ljust(16), ml[i]["codigo_autor"],
                  ml[i]["precio"], ml[i]["estado"])
    return None


def mostrar_clibros_con_determinado_cod_autor(ml, d):
    cantidad_libros = 0
    cod = int(input("Ingrese un código de autor para continuar: "))
    for i in range(d):
        if ml[i]["codigo_autor"] == cod:
            cantidad_libros += 1
    print(f"La cantidad de libros según el código de autor ingresado es: {cantidad_libros}")
    return None


def generar_arreglo_nro_inventario_nombre(ml, d, mi):
    j = 0
    for i in range(d):
        if ml[i]["estado"] == 2:
            mi[j]["nro_inventario"] = ml[i]["nro_inventario"]
            mi[j]["nombre"] = ml[i]["nombre"]
            j += 1
    return j


def mostrar_arreglo_nro_inventario_nombre(mi, d):
    for i in range(d):
        print(mi[i]["nro_inventario"], mi[i]["nombre"])
    return None


# Programa principal
# Estructura del registro

Tdatos_libros = np.dtype(
    [
        ("nro_inventario", int),
        ("nombre", "U20"),
        ("codigo_autor", int),
        ("precio", float),
        ("estado", int)
    ]
)

Tinventario = np.dtype(
    [
        ("nro_inventario", int),
        ("nombre", "U20")
    ]
)

# Arreglo de registros
N = 10
mis_libros = np.empty(N, dtype=Tdatos_libros)
mi_inventario = np.empty(10, dtype=Tinventario)
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado!")
        salir = True
    elif opc == 1:
        cargar_registro(mis_libros)
    elif opc == 2:
        mostrar_registro(mis_libros, N)
    elif opc == 3:
        mostrar_datos_libros_con_determinado_precio(mis_libros, N)
    elif opc == 4:
        mostrar_clibros_con_determinado_cod_autor(mis_libros, N)
    elif opc == 5:
        dim_inv = generar_arreglo_nro_inventario_nombre(mis_libros, N, mi_inventario)
        mostrar_arreglo_nro_inventario_nombre(mi_inventario, dim_inv)
