"""
AUTOR: Iván L. Alvarez

Diagnostico:


Dado los siguientes problemas, defina las estructuras de datos adecuadas para almacenar la información, diseñe el
diagrama de flujo.

1.- "AutosM" empresa dedicada a la venta de automóviles, realiza la distribución de los automóviles
a las diferentes concesionarias. Para ello se utiliza N camiones de carga que puede trasladar
solo hasta 5 automóviles.

Por cada vehículo tiene información de código de identificación formado por cinco dígitos (ejemplo: 03111),
el modelo, marca, precio y el flete. El código de identificación está formado por los cuatro primeros
dígitos son fecha de fabricación (MMAA) y el último indica código de concesionaria (1 al 9).

Se pide:
    a) Guardar la siguiente informacion de sus N camiones de carga: código de identificación, modelo,
color, precio y flete. Se pide hacer un algoritmo que permita realizar el proceso de carga de la
estructura.

    b) La concesionaria X desea obtener el monto de flete de los vehículos, de acuerdo al siguiente formato:

Concesionaria: 9

Modelo      color       Cantidad existente      Monto total del flete
xxxx        xxx         10                        200.000
xxxx        xxx         5                         500.000
xxxx        xxx         7                         700.000
                        total:                  1.400.000

    c) Mostrar un informe de la recaudación de la empresa por cada camión de carga, debiendo el mismo
cumplir con el siguiente formato:

RECAUDACION DEL CAMION
Fecha de fabricación        Precio          Flete
MMAA                        9.999.999       99.999

"""

import numpy as np

# Definición de módulos


# Nombre del Módulo: mostrar_menu
# Descripción: Menú interactivo con el usuario para ingresar distintas opciones
# Datos de Entrada:
# Datos de Salida:
def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------\n"
          "1) Cargar registro\n"
          "2) Mostrar registro\n"
          "3) Realizar ítem a)\n"
          "4) Realizar ítem b)\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


# Nombre del Módulo: cargar_registro
# Descripción: realiza una carga estática del registro tdatos_autos con su respectivo cod_id, modelo, color, precio y
# flete
# Datos de Entrada: vector mis_autos y la cantidad_camiones
# Datos de Salida:
def cargar_registro(ma, cantidad_camiones):
    if cantidad_camiones == 1:
        ma[0, 0] = (3111, "Peugeot", "rojo", 23000, 500)
        ma[0, 1] = (7182, "Fiat", "azul", 19500, 600)
        ma[0, 2] = (11213, "Renault", "verde", 25000, 700)
        ma[0, 3] = (12194, "Volkswagen", "plateado", 22000, 400)
        ma[0, 4] = (5175, "Chevrolet", "blanco", 18000, 300)
    elif cantidad_camiones == 2:
        ma[0, 0] = (3111, "Peugeot", "rojo", 23000, 500)
        ma[0, 1] = (7182, "Fiat", "azul", 19500, 600)
        ma[0, 2] = (11213, "Renault", "verde", 25000, 700)
        ma[0, 3] = (12194, "Volkswagen", "plateado", 22000, 400)
        ma[0, 4] = (5175, "Chevrolet", "blanco", 18000, 300)
        ma[1, 0] = (4131, "Peugeot", "amarillo", 23000, 500)
        ma[1, 1] = (5182, "Fiat", "aguamarina", 27000, 600)
        ma[1, 2] = (5173, "Renault", "gris", 15000, 700)
        ma[1, 3] = (6194, "Volkswagen", "naranja", 28000, 400)
        ma[1, 4] = (7115, "Chevrolet", "azulmarino", 19000, 300)
    elif cantidad_camiones == 3:
        ma[0, 0] = (3111, "Peugeot", "rojo", 23000, 500)
        ma[0, 1] = (7182, "Fiat", "azul", 19500, 600)
        ma[0, 2] = (11213, "Renault", "verde", 25000, 700)
        ma[0, 3] = (12194, "Volkswagen", "plateado", 22000, 400)
        ma[0, 4] = (5175, "Chevrolet", "blanco", 18000, 300)
        ma[1, 0] = (4131, "Peugeot", "amarillo", 23000, 500)
        ma[1, 1] = (5182, "Fiat", "aguamarina", 27000, 600)
        ma[1, 2] = (5173, "Renault", "gris", 15000, 700)
        ma[1, 3] = (6194, "Volkswagen", "naranja", 28000, 400)
        ma[1, 4] = (7115, "Chevrolet", "azulmarino", 19000, 300)
        ma[2, 0] = (12201, "Peugeot", "violeta", 26000, 500)
        ma[2, 1] = (8142, "Fiat", "cian", 21000, 600)
        ma[2, 2] = (9163, "Renault", "rosa", 18500, 700)
        ma[2, 3] = (9134, "Volkswagen", "blanco", 20000, 400)
        ma[2, 4] = (10105, "Chevrolet", "turquesa", 15000, 300)
    elif cantidad_camiones == 4:
        ma[0, 0] = (3111, "Peugeot", "rojo", 23000, 500)
        ma[0, 1] = (7182, "Fiat", "azul", 19500, 600)
        ma[0, 2] = (11213, "Renault", "verde", 25000, 700)
        ma[0, 3] = (12194, "Volkswagen", "plateado", 22000, 400)
        ma[0, 4] = (5175, "Chevrolet", "blanco", 18000, 300)
        ma[1, 0] = (4131, "Peugeot", "amarillo", 23000, 500)
        ma[1, 1] = (5182, "Fiat", "aguamarina", 27000, 600)
        ma[1, 2] = (5173, "Renault", "gris", 15000, 700)
        ma[1, 3] = (6194, "Volkswagen", "naranja", 28000, 400)
        ma[1, 4] = (7115, "Chevrolet", "azulmarino", 19000, 300)
        ma[2, 0] = (12201, "Peugeot", "violeta", 26000, 500)
        ma[2, 1] = (8142, "Fiat", "cian", 21000, 600)
        ma[2, 2] = (9163, "Renault", "rosa", 18500, 700)
        ma[2, 3] = (9134, "Volkswagen", "blanco", 20000, 400)
        ma[2, 4] = (10105, "Chevrolet", "turquesa", 15000, 300)
        ma[3, 0] = (10141, "Peugeot", "celeste", 26000, 500)
        ma[3, 1] = (1222, "Fiat", "rojo", 19000, 600)
        ma[3, 2] = (12123, "Renault", "plateado", 25000, 700)
        ma[3, 3] = (12114, "Volkswagen", "blanco", 20000, 400)
        ma[3, 4] = (3225, "Chevrolet", "gris oscuro", 30000, 300)
    elif cantidad_camiones == 5:
        ma[0, 0] = (3111, "Peugeot", "rojo", 23000, 500)
        ma[0, 1] = (7182, "Fiat", "azul", 19500, 600)
        ma[0, 2] = (11213, "Renault", "verde", 25000, 700)
        ma[0, 3] = (12194, "Volkswagen", "plateado", 22000, 400)
        ma[0, 4] = (5175, "Chevrolet", "blanco", 18000, 300)
        ma[1, 0] = (4131, "Peugeot", "amarillo", 23000, 500)
        ma[1, 1] = (5182, "Fiat", "aguamarina", 27000, 600)
        ma[1, 2] = (5173, "Renault", "gris", 15000, 700)
        ma[1, 3] = (6194, "Volkswagen", "naranja", 28000, 400)
        ma[1, 4] = (7115, "Chevrolet", "azulmarino", 19000, 300)
        ma[2, 0] = (12201, "Peugeot", "violeta", 26000, 500)
        ma[2, 1] = (8142, "Fiat", "cian", 21000, 600)
        ma[2, 2] = (9163, "Renault", "rosa", 18500, 700)
        ma[2, 3] = (9134, "Volkswagen", "blanco", 20000, 400)
        ma[2, 4] = (10105, "Chevrolet", "turquesa", 15000, 300)
        ma[3, 0] = (10141, "Peugeot", "celeste", 26000, 500)
        ma[3, 1] = (1222, "Fiat", "rojo", 19000, 600)
        ma[3, 2] = (12123, "Renault", "plateado", 25000, 700)
        ma[3, 3] = (12114, "Volkswagen", "blanco", 20000, 400)
        ma[3, 4] = (3225, "Chevrolet", "gris oscuro", 30000, 300)
        ma[4, 0] = (11211, "Peugeot", "azul marino", 29000, 500)
        ma[4, 1] = (2202, "Fiat", "negro", 25000, 600)
        ma[4, 2] = (2193, "Renault", "negro", 24500, 700)
        ma[4, 3] = (3164, "Volkswagen", "naranja", 20000, 400)
        ma[4, 4] = (12155, "Chevrolet", "negro", 17000, 300)
    return None


# Nombre del Módulo: mostrar_registro
# Descripción: Nos muestra el registro cargado en un arreglo
# Datos de Entrada: vector mis_autos, la dimensión de sus filas y la dimensión de sus columnas
# Datos de Salida:
def mostrar_registro(ma, fil, col):
    print("Cód id  Modelo        Color            Precio            Flete")
    for i in range(fil):
        for j in range(col):
            print(str(ma[i, j]["cod_id"]).ljust(5), end="   ")
            print(str(ma[i, j]["modelo"]).ljust(10), end="    ")
            print(str(ma[i, j]["color"]).ljust(11), end="    ")
            print("$", ma[i, j]["precio"], end="         ")
            print("$", ma[i, j]["flete"])
    return None


# Nombre del Módulo: realizar_act_b
# Descripción: Muestra por pantalla el formato especificado en la actividad b mostrando el modelo, color, cantidad
# existente y monto total del flete
# Datos de Entrada: vector mis_autos, dimensión de filas, dimensión de columnas
# Datos de Salida: monto_total_flete
def realizar_act_b(ma, fil, col):
    num_concesionaria = int(input("Ingrese el número de concesionaria: "))
    monto_total_flete = 0
    cantidad = 0
    print("Concesionaria: ", num_concesionaria)
    print("Modelo       Color         Cantidad existente      Monto total del flete")
    for i in range(fil):
        for j in range(col):
            if ma[i, j]["cod_id"] % 10 == num_concesionaria:
                monto_total_flete += ma[i, j]["flete"]
                cantidad += 1
                print(str(ma[i, j]["modelo"]).ljust(10), end="   ")
                print(str(ma[i, j]["color"]).ljust(12), end="  ")
                print(cantidad, end="                       ")
                print(ma[i, j]["flete"])
    return monto_total_flete


# c) Mostrar un informe de la recaudación de la empresa por cada camión de carga, debiendo el mismo
# cumplir con el siguiente formato:
#
# RECAUDACION DEL CAMION
# Fecha de fabricación        Precio          Flete
# MMAA                        9.999.999       99.999
def realizar_act_c(ma, fil, col):
    print("RECAUDACIÓN DEL CAMIÓN\n"
          "Fecha de fabricación         Precio          Flete")

    return None


# Programa principal

# Estructura del registro de autos


tdatos_autos = np.dtype(
    [
        ("cod_id", int),
        ("modelo", "U30"),
        ("color", "U30"),
        ("precio", float),
        ("flete", float)
    ]
)

# Arreglo de registros

autos = 5
camiones = int(input("Ingrese la cantidad de camiones (1 - 5): "))
mis_autos = np.empty([camiones, autos], dtype=tdatos_autos)

salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado!")
        salir = True
    elif opc == 1:
        cargar_registro(mis_autos, camiones)
    elif opc == 2:
        mostrar_registro(mis_autos, camiones, autos)
    elif opc == 3:
        monto_total = realizar_act_b(mis_autos, camiones, autos)
        print("TOTAL:                                            ", monto_total)
