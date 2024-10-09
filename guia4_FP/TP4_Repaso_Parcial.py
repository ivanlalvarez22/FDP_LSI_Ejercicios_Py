# Un edificio de departamentos mantiene la siguiente información de sus departamentos:
# Número de departamento, Piso, Apellido y Nombre del propietario, Categoría {Clase A, Clase B, Clase C),
# Metros cuadrados, Cantidad de Cuotas de Expensas adeudadas.
# Cada departamento paga por las expensas $25 por metro cuadrado, más un porcentaje del total a pagar por
# las expensas teniendo en cuenta la siguiente tabla: (Ej. Si el departamento tiene 75 metros cuadrados:(75*25) + 7%)

# Clase C       Menos de 75 mts2                10 %
# Clase B       Entre 75 mts2 y 90 mts2         7  %
# Clase A       Más de 90 mts2                  5  %

# 1.- Mostrar Número de Departamento, Categoría y Monto de Expensas adeudado.
# 2.- Dada una categoría, mostrar el Número de departamento que más cuotas adeuda.

import numpy as np

# Definición de módulos


def mostrar_menu():
    print("-----------MENÚ PRINCIPAL-------------\n"
          "1) Cargar registro\n"
          "2) Mostrar registro\n"
          "3) Mostrar nro depto cat y monto de expensas adeudado\n"
          "4) Dada una categoría mostrar el nro de depto que más cuotas adeuda\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


def cargar_registro(md):
    md[0] = (11, 1, "Alvarez Iván", 2, 80, 6)
    md[1] = (14, 3, "Basualdo Sabrina", 3, 70, 4)
    md[2] = (22, 2, "Alvarez Sergio", 1, 100, 7)
    md[3] = (23, 1, "Bottoni Julio", 3, 70, 10)
    md[4] = (25, 5, "Alvarez Silvina", 3, 65, 3)
    md[5] = (33, 4, "Perez Juan", 2, 85, 0)
    md[6] = (37, 2, "Newton Isaac", 1, 100, 0)
    md[7] = (45, 7, "Turing Alan", 3, 50, 2)
    md[8] = (54, 1, "Jobs Steve", 1, 100, 7)
    md[9] = (56, 8, "Gates Bill", 2, 80, 1)
    print("\n¡Registro cargado exitosamente!\n")
    return None


def convertir_categoria_caracter(num):
    if num == 1:
        cat = "CLASE A"
    elif num == 2:
        cat = "CLASE B"
    else:
        cat = "CLASE C"
    return cat


def mostrar_registro(md, d):
    print("NRO. DEPTO      PISO      APELLIDO Y NOMBRE      CATEGORÍA      M2      CUOTAS ADEUDADAS")
    for i in range(d):
        print(md[i]["nro_depto"], end="              ")
        print(md[i]["piso"], end="         ")
        print(str(md[i]["apellido_nombre"]).ljust(20), end="   ")
        print(convertir_categoria_caracter(md[i]["categoria"]), end="        ")
        print(str(md[i]["metros_cuadrados"]).ljust(3), end="     ")
        print(str(md[i]["cant_cuotas_adeudadas"]).ljust(2))
    return None


def calcular_monto(metros_cuadrados):
    if metros_cuadrados > 90:
        monto = metros_cuadrados * 25
        monto_total = monto + monto * 0.05
    elif metros_cuadrados < 75:
        monto = metros_cuadrados * 25
        monto_total = monto + monto * 0.1
    else:
        monto = metros_cuadrados * 25
        monto_total = monto + monto * 0.07
    return monto_total


def realizar_act_a(md, d):
    print("NRO. DEPTO      CATEGORIA      MONTO ADEUDADO")
    for i in range(d):
        monto_total = calcular_monto(md[i]["metros_cuadrados"])
        print(md[i]["nro_depto"], end="              ")
        print(md[i]["categoria"], end="              ")
        print(f"${monto_total}")
    return None


def realizar_act_b(md, d):
    cat = int(input("Ingrese una categoría para continuar: "))
    nro = 0
    may = 0
    for i in range(d):
        if md[i]["cant_cuotas_adeudadas"] >= may and md[i]["categoria"] == cat:
            may = md[i]["cant_cuotas_adeudadas"]
            nro = md[i]["nro_depto"]
    print(f"El nro de depto que más cuotas adeuda es el {nro}\n"
          f"el mismo adeuda {may} cantidad de cuotas")
    return None


# Programa principal
# Estructura del registro

Tdatos_departamentos = np.dtype(
    [
        ("nro_depto", int),
        ("piso", int),
        ("apellido_nombre", "U50"),
        ("categoria", int),
        ("metros_cuadrados", int),
        ("cant_cuotas_adeudadas", int)
    ]
)

# Arreglo de registros
N = 10
mis_departamentos = np.empty(N, dtype=Tdatos_departamentos)
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado")
        salir = True
    elif opc == 1:
        cargar_registro(mis_departamentos)
    elif opc == 2:
        mostrar_registro(mis_departamentos, N)
    elif opc == 3:
        realizar_act_a(mis_departamentos, N)
    elif opc == 4:
        realizar_act_b(mis_departamentos, N)
