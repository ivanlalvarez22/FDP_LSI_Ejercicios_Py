# Una empresa de seguros registra la siguiente información de las pólizas vendida: número de póliza,
# tipo de póliza {1-Casa, 2-Auto, 3-Vida}, fecha de inicio de cobertura, nombre y apellido del beneficiario, DNI,
# cantidad de cuotas adeudadas, monto mensual de la póliza. Como programador se le pide:

# 1.- Colocar los parámetros en la descripción de todos lo módulos provistos y convocar al
# módulo CargarPolizas (5 Puntos).

# 2.- Información de una póliza: mostrar la información de una determinada póliza a partir de su número a ser
# ingresado, siempre y cuando exista, y de acuerdo al siguiente formato: (15 Puntos)

#                                 INFORMACIÓN DE LA PÓLIZA

# Nro: 12345        Beneficiario: Juan Perez        Tipo: Casa        Fecha de inicio de cobertura: 19/10/2019

# Cantidad de cuotas adeudadas: 2        Monto adeudado: $ 11000,00

# En caso de que el número de póliza ingresado no existiera, se deberá mostrar "Póliza inexistente".
# NOTA: debe en su interior convocar obligatoriamente al menos al módulo existe_poliza.

# 3.- Actualizar pólizas viejas: actualizar el monto mensual para aquellas pólizas que tienen cinco o más años de
# antigüedad. Para ello debe realizar un procedimiento que a partir del año actual y de un porcentaje de descuento,
# actualice el monto mensual de las pólizas aplicándole el porcentaje de descuento proporcionado, debiendo a su vez
# retornar la cantidad de pólizas que fueron actualizados. (15 Puntos).

# 4.- Póliza de un tipo: generar una estructura de datos con aquellos números de pólizas que son de un tipo a
# ser ingresado. Mostrar la estructura resultante (15 Puntos).

import numpy as np

# Definición de módulos


def mostrar_menu():
    print("-----------MENÚ PRINCIPAL----------\n"
          "1) Cargar registro\n"
          "2) Mostrar registro\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


def cargar_polizas(p):
    p[0] = (12345, 1, (19, 10, 2019), "Juan Perez", 35098765, 2, 5500.00)
    p[1] = (34665, 2, (13, 2, 2015), "Maria Gomez", 23465789, 3, 2500.00)
    p[2] = (35421, 3, (3, 11, 2018), "Silvia Sanchez", 29087654, 0, 4000.00)
    p[3] = (23456, 1, (5, 4, 2020), "Roberto Salas", 13987456, 0, 5500.00)
    p[4] = (12577, 1, (8, 9, 2016), "Atilio Coria", 36932678, 5, 5500.00)
    p[5] = (12346, 3, (17, 7, 2018), "Franco Sosa", 22456987, 4, 4000.00)
    print("\nRegistro cargado exitosamente\n")
    return None


def convertir_num_string(num):
    if num == 1:
        string = "Casa"
    elif num == 2:
        string = "Auto"
    else:
        string = "Vida"
    return string


def mostrar_registro(p, d):
    print("NRO      TIPO        FECHA         NOMBRE Y APELLIDO      DNI         CUOTAS AD.      MONTO MENSUAL")
    for i in range(d):
        tipo = convertir_num_string(p[i]["tipo"])
        print(p[i]["numero"], end="    ")
        print(tipo, end="        ")
        print(str(p[i]["fecha"]["dia"]).ljust(2) + "/" + str(p[i]["fecha"]["mes"]).ljust(2) + "/" +
              str(p[i]["fecha"]["año"]).ljust(4), end="    ")
        print(str(p[i]["nombre_apellido"]).ljust(15), end="        ")
        print(p[i]["dni"], end="    ")
        print(p[i]["cant_cuotas_ad"], end="              ")
        print("$", p[i]["monto_mensual"])
    return None


def existe_poliza(num, num_poliza):
    existe = False
    if num == num_poliza:
        existe = True
    return existe


def mostrar_info_poliza(p, d):
    num = int(input("Ingrese un número de póliza para mostrar su información: "))
    existe = False
    print("")
    for i in range(d):
        if existe_poliza(num, p[i]["numero"]):
            existe = existe_poliza(num, p[i]["numero"])
            print("Nro:", p[i]["numero"], "Beneficiario:", p[i]["nombre_apellido"], "Tipo:",
                  convertir_num_string(p[i]["tipo"]), "Fecha de inicio de cobertura:", str(p[i]["fecha"]["dia"]) + "/"
                  + str(p[i]["fecha"]["mes"]) + "/" + str(p[i]["fecha"]["año"]))
            print("Cantidad de cuotas adeudadas:", p[i]["cant_cuotas_ad"], "Monto adeudado:", "$",
                  p[i]["cant_cuotas_ad"] * p[i]["monto_mensual"])
    if not existe:
        print("Número de póliza inexistente")
    return None


def calcular_antiguedad(anios):
    antiguedad = 2021 - anios
    return antiguedad


def actualizar_polizas(p, d):
    porcentaje = int(input("Ingrese un porcentaje de descuento: "))
    cantidad = 0
    for i in range(d):
        antiguedad = calcular_antiguedad(p[i]["fecha"]["año"])
        if antiguedad >= 5:
            p[i]["monto_mensual"] = p[i]["monto_mensual"] - (p[i]["monto_mensual"] * (porcentaje / 100))
            cantidad += 1
    return cantidad


def generar_estructura(p, d, num_pol):
    tipo = int(input("Ingrese un tipo de póliza (1.-Casa 2.-Auto 3.-Vida): "))
    j = 0
    for i in range(d):
        if p[i]["tipo"] == tipo:
            num_pol[j]["numero"] = p[i]["numero"]
            j += 1
    return j


def mostrar_estructura_num_polizas(num_pol, d):
    for i in range(d):
        print(num_pol[i]["numero"])
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

Tdatos_polizas = np.dtype(
    [
        ("numero", int),
        ("tipo", int),
        ("fecha", Tfecha),
        ("nombre_apellido", "U40"),
        ("dni", int),
        ("cant_cuotas_ad", int),
        ("monto_mensual", float)
    ]
)

# Arreglo de registros
N = 6
polizas = np.empty(N, dtype=Tdatos_polizas)
num_polizas = np.empty(N, dtype=Tdatos_polizas)
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado")
        salir = True
    elif opc == 1:
        cargar_polizas(polizas)
    elif opc == 2:
        mostrar_registro(polizas, N)
    elif opc == 3:
        mostrar_info_poliza(polizas, N)
    elif opc == 4:
        cant = actualizar_polizas(polizas, N)
        mostrar_registro(polizas, N)
        print(f"La cantidad de pólizas actualizadas fueron: {cant}")
    elif opc == 5:
        dim_num_polizas = generar_estructura(polizas, N, num_polizas)
        mostrar_estructura_num_polizas(num_polizas, dim_num_polizas)
