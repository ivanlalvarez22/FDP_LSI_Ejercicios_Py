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
def cargar_registro(mc, cantidad_camiones):
    if cantidad_camiones == 1:
        mc[0]["auto1"] = (3111, "206", "azul", 20000, 500)
        mc[0]["auto2"] = (2121, "308", "rojo", 21000, 500)
        mc[0]["auto3"] = (4151, "207", "negro", 19000, 500)
        mc[0]["auto4"] = (9171, "408", "rojo", 25000, 500)
        mc[0]["auto5"] = (1192, "Gol", "amarillo", 18000, 700)
    elif cantidad_camiones == 2:
        mc[0]["auto1"] = (3111, "206", "azul", 20000, 500)
        mc[0]["auto2"] = (2121, "308", "rojo", 21000, 500)
        mc[0]["auto3"] = (4151, "207", "negro", 19000, 500)
        mc[0]["auto4"] = (9171, "408", "rojo", 25000, 500)
        mc[0]["auto5"] = (1192, "gol", "amarillo", 18000, 700)
        mc[1]["auto1"] = (12212, "Nivus", "plateado", 26000, 600)
        mc[1]["auto2"] = (11212, "Tiguan", "blanco", 30000, 600)
        mc[1]["auto3"] = (10202, "Amarok", "negro", 35000, 600)
        mc[1]["auto4"] = (1153, "Logan", "verde", 15000, 400)
        mc[1]["auto5"] = (3123, "Fluence", "gris", 21000, 400)
    elif cantidad_camiones == 3:
        mc[0]["auto1"] = (3111, "206", "azul", 20000, 500)
        mc[0]["auto2"] = (2121, "308", "rojo", 21000, 500)
        mc[0]["auto3"] = (4151, "207", "negro", 19000, 500)
        mc[0]["auto4"] = (9171, "408", "rojo", 25000, 500)
        mc[0]["auto5"] = (1192, "gol", "amarillo", 18000, 700)
        mc[1]["auto1"] = (12212, "Nivus", "plateado", 26000, 600)
        mc[1]["auto2"] = (11212, "Tiguan", "blanco", 30000, 600)
        mc[1]["auto3"] = (10202, "Amarok", "negro", 35000, 600)
        mc[1]["auto4"] = (1153, "Logan", "verde", 15000, 400)
        mc[1]["auto5"] = (3123, "Fluence", "gris", 21000, 400)
        mc[2]["auto1"] = (4124, "Prisma", "azul marino", 20000, 1000)
        mc[2]["auto2"] = (6144, "Corsa", "gris", 12000, 1000)
        mc[2]["auto3"] = (7174, "S10", "negro", 34000, 1000)
        mc[2]["auto4"] = (6215, "Palio", "blanco", 19000, 200)
        mc[2]["auto5"] = (5155, "Cronos", "gris perla", 22000, 200)
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
def mostrar_registro(mc, fil):
    print("Cód id  Modelo        Color            Precio            Flete")
    for i in range(fil):
        print(str(mc[i]["auto1"]["cod_id"]).ljust(5), end="   ")
        print(str(mc[i]["auto1"]["modelo"]).ljust(10), end="    ")
        print(str(mc[i]["auto1"]["color"]).ljust(11), end="    ")
        print("$", mc[i]["auto1"]["precio"], end="         ")
        print("$", mc[i]["auto1"]["flete"])
        print(str(mc[i]["auto2"]["cod_id"]).ljust(5), end="   ")
        print(str(mc[i]["auto2"]["modelo"]).ljust(10), end="    ")
        print(str(mc[i]["auto2"]["color"]).ljust(11), end="    ")
        print("$", mc[i]["auto2"]["precio"], end="         ")
        print("$", mc[i]["auto2"]["flete"])
        print(str(mc[i]["auto3"]["cod_id"]).ljust(5), end="   ")
        print(str(mc[i]["auto3"]["modelo"]).ljust(10), end="    ")
        print(str(mc[i]["auto3"]["color"]).ljust(11), end="    ")
        print("$", mc[i]["auto3"]["precio"], end="         ")
        print("$", mc[i]["auto3"]["flete"])
        print(str(mc[i]["auto4"]["cod_id"]).ljust(5), end="   ")
        print(str(mc[i]["auto4"]["modelo"]).ljust(10), end="    ")
        print(str(mc[i]["auto4"]["color"]).ljust(11), end="    ")
        print("$", mc[i]["auto4"]["precio"], end="         ")
        print("$", mc[i]["auto4"]["flete"])
        print(str(mc[i]["auto5"]["cod_id"]).ljust(5), end="   ")
        print(str(mc[i]["auto5"]["modelo"]).ljust(10), end="    ")
        print(str(mc[i]["auto5"]["color"]).ljust(11), end="    ")
        print("$", mc[i]["auto5"]["precio"], end="         ")
        print("$", mc[i]["auto5"]["flete"])
    return None


# Nombre del Módulo: realizar_act_b
# Descripción: Muestra por pantalla el formato especificado en la actividad b mostrando el modelo, color, cantidad
# existente y monto total del flete
# Datos de Entrada: vector mis_autos, dimensión de filas, dimensión de columnas
# Datos de Salida: monto_total_flete
def realizar_act_b(ma, fil):
    num_concesionaria = int(input("Ingrese el número de concesionaria (1 - 5): "))
    monto_total_flete = 0
    cantidad = 0
    print("Concesionaria: ", num_concesionaria)
    print("Modelo       Color         Cantidad existente      Monto total del flete")
    for i in range(fil):
        if ma[i]["auto1"]["cod_id"] or ma[i]["auto2"]["cod_id"] or ma[i]["auto3"]["cod_id"] or ma[i]["auto4"]["cod_id"]\
                or ma[i]["auto5"]["cod_id"] == num_concesionaria:
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

tdatos_camiones = np.dtype(
    [
        ("auto1", tdatos_autos),
        ("auto2", tdatos_autos),
        ("auto3", tdatos_autos),
        ("auto4", tdatos_autos),
        ("auto5", tdatos_autos)

    ]
)

# Arreglo de registros

autos = 5
mis_camiones = np.empty(autos, dtype=tdatos_camiones)
camiones = int(input("Ingrese la cantidad de camiones (1 - 5): "))

salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado!")
        salir = True
    elif opc == 1:
        cargar_registro(mis_camiones, camiones)
    elif opc == 2:
        mostrar_registro(mis_camiones, camiones)
    elif opc == 3:
        monto_total = realizar_act_b(mis_autos, camiones)
        print("TOTAL:                                            ", monto_total)
