# Una inmobiliaria registra para cada uno de los departamentos que tiene en alquiler la siguiente información:
# Código de Departamento, Superficie, Estado {excelente, buena, regular o mala}, Precio,
# Dirección (calle, número, piso, nro. dpto.) y Disponibilidad {ocupado, disponible}. Mostrar:
# a).- Los datos de todos los departamentos disponibles que tengan un Estado excelente y una
# Superficie mayor o igual a un cierto valor.
# b).- Para cada una de las solicitudes de alquiler, indicar si puede satisfacer o no la demanda, mostrando el
# Precio y la Dirección, en función a la Superficie y Estado solicitado.

import numpy as np

# Definción de módulos


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------\n"
          "1) Cargar registro\n"
          "2) Mostrar registro\n"
          "3) Realizar actividad a)\n"
          "4) Realizar actividad b)\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


def cargar_registro(md):
    md[0] = (1001, 150, "excelente", 50000.0, ("Roca", 100, 3, 31), "disponible")
    md[1] = (1002, 130, "regular", 10000.0, ("Roca", 100, 2, 22), "ocupado")
    md[2] = (1003, 110, "mala", 5000.0, ("Roca", 100, 2, 21), "disponible")
    md[3] = (1004, 120, "buena", 20000.0, ("Roca", 100, 3, 32), "disponible")
    md[4] = (1005, 100, "regular", 15000.0, ("Libertad", 70, 1, 11), "ocupado")
    md[5] = (1006, 250, "excelente", 70000.0, ("Libertad", 70, 1, 12), "ocupado")
    md[6] = (1007, 120, "buena", 30000.0, ("Libertad", 70, 2, 25), "disponible")
    md[7] = (1008, 130, "regular", 20000.0, ("Libertad", 70, 3, 34), "ocupado")
    md[8] = (1009, 300, "excelente", 80000.0, ("Pellegrini", 210, 8, 88), "disponible")
    md[9] = (1010, 60, "mala", 5000.0, ("Pellegrini", 210, 2, 28), "ocupado")
    return None


def realizar_act_a(md, d):
    sup = int(input("Ingrese una superficie: "))
    print("Cod. depto       Estado        Precio      Calle          Nro     Piso        Nro. depto")
    for i in range(d):
        if md[i]["estado"] == "excelente" and md[i]["superficie"] >= sup and md[i]["disponibilidad"] == "disponible":
            print(md[i]["cod_depto"], end="             ")
            print(md[i]["estado"], end="   ")
            print("$", md[i]["precio"], end="     ")
            print(str(md[i]["direccion"]["calle"]).ljust(15), end="")
            print(md[i]["direccion"]["numero"], end="      ")
            print(md[i]["direccion"]["piso"], end="            ")
            print(md[i]["direccion"]["nro_depto"])
    return None


def realizar_act_b(md, d):
    sup = int(input("Ingrese la superficie: "))
    estado = input("Ingrese el estado (excelente, buena, regular, mala): ")
    for i in range(d):
        if md[i]["superficie"] == sup and md[i]["estado"] == estado:
            print("Se encotraron coincidencias!")
            print("Precio       Calle       Nro     Piso        Nro depto")
            print("$", md[i]["precio"], end="    ")
            print(md[i]["direccion"]["calle"], end="        ")
            print(md[i]["direccion"]["numero"], end="      ")
            print(md[i]["direccion"]["piso"], end="          ")
            print(md[i]["direccion"]["nro_depto"])


# Programa principal
# Estructura de los registros

Tdireccion = np.dtype(
    [
        ("calle", "U20"),
        ("numero", int),
        ("piso", int),
        ("nro_depto", int)
    ]
)

Tdatos_departamentos = np.dtype(
    [
        ("cod_depto", int),
        ("superficie", int),
        ("estado", "U10"),
        ("precio", float),
        ("direccion", Tdireccion),
        ("disponibilidad", "U10")
    ]
)

# Arreglo de registros
N = 10
mis_departamentos = np.empty(N, Tdatos_departamentos)
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado")
        salir = True
    elif opc == 1:
        cargar_registro(mis_departamentos)
    elif opc == 3:
        realizar_act_a(mis_departamentos, N)
    elif opc == 4:
        realizar_act_b(mis_departamentos, N)
