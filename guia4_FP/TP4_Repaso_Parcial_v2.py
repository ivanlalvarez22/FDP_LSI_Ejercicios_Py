# Un almacén almacena la siguiente información acerca de los productos que comercializa:
# código, descripción, rubro {1-Comestibles, 2-Limpieza, 3-Lácteos, 4-Bebidas}, cantidad disponible,
# precio de venta, si tiene vencimiento {True - Si, False -No} y la fecha de vencimiento. Como programador se le pide:

# 1.- Colocar los parámetros en la descripción de todos los módulos provistos y convocar al
# módulo CargarProductos. (5 Puntos).

# 2.- Información de un Producto: mostrar la información de un determinado producto a partir de su código a ser
# ingresado, siempre y cuando exista, y de acuerdo al siguiente formato: (15 Puntos)

#                           INFORMACIÓN DEL PRODUCTO
# Código: 14                Descripción: Crema de Leche         Rubro: Lácteos
# Tiene vencimiento: Si     Fecha de vencimiento: 27/03/2021
# Cantidad disponible: 70   Precio de venta: 120,00             Valuación: 8400,00

# En caso de que el código de producto ingresado no existiera, se deberá mostrar "Código inexistente".
# NOTA: debe en su interior convocar obligatoriamente al menos al módulo ExisteProducto.

# 3.- Actualizar precios de un rubro: actualizar el precio de todos aquellos productos que pertenezcan a un rubro a ser
# ingresado. Para ello deberá realizar un procedimiento que, dado un rubro y un porcentaje, aumente el precio de todos
# los productos de ese rubro en el porcentaje indicado, debiendo además retornar la cantidad de productos
# actualizados (15 Puntos)

# 4.- Productos a vencer: Generar una estructura de datos con aquellos códigos de productos que se vencen en un
# mes y año a ser ingresados. Mostrar la estructura resultante (20 PUNTOS).

import numpy as np

# Definición de módulos


def mostrar_menu():
    print("------------MENÚ PRINCIPAL---------------\n"
          "1) Cargar registro\n"
          "2) Mostrar registro\n"
          "3) Mostrar la información de un producto según el código ingresado\n"
          "4) Actualizar precios de un rubro\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


def cargar_productos(ma):
    ma[0] = (10, "Leche", 3, 600, 80.00, True, (19, 10, 2021))
    ma[1] = (12, "Aceite", 1, 76, 220.00, True, (23, 10, 2020))
    ma[2] = (30, "Jabon Tocador", 2, 6500, 110.00, False, (0, 0, 0))
    ma[3] = (14, "Crema Leche", 3, 70, 120.00, True, (27, 3, 2021))
    ma[4] = (50, "Cinzano", 4, 7, 280.00, False, (0, 0, 0))
    ma[5] = (16, "Soda", 4, 80, 60.50, False, (0, 0, 0))
    ma[6] = (17, "Queso Cheddar", 3, 500, 120.50, True, (3, 10, 2021))
    print("\nRegistro correctamente cargado\n")
    return None


def convertir_booleano_a_caracter(booleano):
    if booleano:
        caracter = "Si"
    else:
        caracter = "No"
    return caracter


def convertir_num_caracter(num):
    if num == 1:
        caracter = "Comestibles"
    elif num == 2:
        caracter = "Limpieza"
    elif num == 3:
        caracter = "Lácteos"
    else:
        caracter = "Bebidas"
    return caracter


def mostrar_registro(ma, d):
    print("CÓD    DESCRIPCIÓN         RUBRO          CANT. DISPONIBLE     PRECIO    VENCIMIENTO      FECHA VENCIMIENTO")
    for i in range(d):
        rubro = convertir_num_caracter(ma[i]["rubro"])
        print(ma[i]["codigo"], end="     ")
        print(str(ma[i]["descripcion"]).ljust(15), end="     ")
        print(str(rubro).ljust(12), end="   ")
        print(str(ma[i]["cant_disponible"]).ljust(5), end="               ")
        print("$", str(ma[i]["precio"]).ljust(10), end="   ")
        print(convertir_booleano_a_caracter(ma[i]["vencimiento"]), end="           ")
        print(str(ma[i]["fecha_vencimiento"]["dia"]) + "/" + str(ma[i]["fecha_vencimiento"]["mes"]) + "/" +
              str(ma[i]["fecha_vencimiento"]["año"]))
    return None


def existe_producto(cod_existente, cod_ingresado):
    existe = False
    if cod_existente == cod_ingresado:
        existe = True
    return existe


def mostrar_informacion_prod(ma, d):
    cod = int(input("Ingrese un código de producto para continuar: "))
    existe = False
    for i in range(d):
        if existe_producto(ma[i]["codigo"], cod):
            existe = existe_producto(ma[i]["codigo"], cod)
            print("\ncodigo:", ma[i]["codigo"], "Descripción:", ma[i]["descripcion"], "Rubro:",
                  convertir_num_caracter(ma[i]["rubro"]))
            print("Tiene vencimiento:", convertir_booleano_a_caracter(ma[i]["vencimiento"]), "Fecha de vencimiento:",
                  ma[i]["fecha_vencimiento"]["dia"], ma[i]["fecha_vencimiento"]["mes"],
                  ma[i]["fecha_vencimiento"]["año"])
            print("Cantidad disponible:", ma[i]["cant_disponible"], "Precio de venta:", "$", ma[i]["precio"],
                  "Valuación:", "$", ma[i]["precio"] * ma[i]["cant_disponible"])
            print("")
    if not existe:
        print("\nProducto inexistente\n")
    return None


def actualizar_precios_por_rubro(ma, d):
    rubro = int(input("Ingrese un rubro para continuar (1.- comestibles 2.- limpieza 3.- lácteos 4.- bebidas: "))
    porcentaje = int(input("Ingrese un porcentaje para actualizar el precio: "))
    cant = 0
    for i in range(d):
        if ma[i]["rubro"] == rubro:
            ma[i]["precio"] = ma[i]["precio"] + (ma[i]["precio"] * (porcentaje / 100))
            cant += 1
    print(f"\nPrecios del rubro {convertir_num_caracter(rubro)} actualizado en un {porcentaje}%")
    return cant


def generar_estructura(ma, d, cod_prod):
    mes = int(input("Ingrese el mes de vencimiento: "))
    anio = int(input("Ingrese el año de vencimiento: "))
    j = 0
    for i in range(d):
        if ma[i]["fecha_vencimiento"]["mes"] == mes and ma[i]["fecha_vencimiento"]["año"] == anio:
            cod_prod[j]["codigo"] = ma[i]["codigo"]
            j += 1
    return j


def mostrar_arreglo_cod(cod_prod, d):
    print("")
    for i in range(d):
        print(cod_prod[i]["codigo"])
    print("")
    return None


# Programa principal
# Estructura del registro

Tfecha = np.dtype(
    [
        ("dia", int),
        ("mes", int),
        ("año", int)
    ]
)

Tdatos_almacen = np.dtype(
    [
        ("codigo", int),
        ("descripcion", "U40"),
        ("rubro", int),
        ("cant_disponible", int),
        ("precio", float),
        ("vencimiento", bool),
        ("fecha_vencimiento", Tfecha)
    ]
)


# Arreglo de registros
N = 10
mi_almacen = np.empty(N, dtype=Tdatos_almacen)
dim = 7
codigo_producto = np.empty(N, dtype=Tdatos_almacen)
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado!")
        salir = True
    elif opc == 1:
        cargar_productos(mi_almacen)
    elif opc == 2:
        mostrar_registro(mi_almacen, dim)
    elif opc == 3:
        mostrar_informacion_prod(mi_almacen, dim)
    elif opc == 4:
        cantidad_productos = actualizar_precios_por_rubro(mi_almacen, dim)
        mostrar_registro(mi_almacen, dim)
        print(f"La cantidad de productos actualizados fueron: {cantidad_productos}")
    elif opc == 5:
        dim_cod = generar_estructura(mi_almacen, dim, codigo_producto)
        mostrar_arreglo_cod(codigo_producto, dim_cod)
