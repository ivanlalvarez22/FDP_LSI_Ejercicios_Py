import numpy as np
from os import system as console

"""
4. Una inmobiliaria registra para cada uno de los departamentos que tiene en
alquiler la siguiente información: Código de Departamento, Superficie,
Estado {excelente, buena, regular o mala}, Precio,
Dirección (calle, número, piso, nro. dpto.)
y Disponibilidad {ocupado, disponible}.
Mostrar:

a) Los datos de todos los departamentos disponibles que tengan un Estado
excelente y una Superficie mayor o igual a un cierto valor.

b) Para cada una de las solicitudes de alquiler, indicar si puede satisfacer o
no la demanda, mostrando el Precio y la Dirección, en función a la Superficie y
Estado solicitado.
"""


# ------------------------------Sección de Módulos------------------------------


def load_apartments_d(a, dim):
    """

    :param a:
    :param dim:
    :return:
    """
    for i in range(dim):
        #
        a[i]["codigo"] = int(
            input(
                f"{i + 1}º departamento - código: "
            )
        )
        #
        a[i]["superficie"] = float(
            input(
                f"{i + 1}º departamento - Superficie: "
            )
        )
        #
        a[i]["estado"] = input(
            f"{i + 1}º departamento - Estado "
            "(excelente, buena, regular o mala): "
        )
        #
        a[i]["precio"] = float(
            input(
                f"{i + 1}º departamento - Precio: "
            )
        )
        #
        a[i]["direccion"]["calle"] = input(
            f"{i + 1}º departamento - Calle: "
        )
        #
        a[i]["direccion"]["numero"] = int(
            input(
                f"{i + 1}º departamento - Número: "
            )
        )
        #
        a[i]["direccion"]["piso"] = int(
            input(
                f"{i + 1}º departamento - Piso: "
            )
        )
        #
        a[i]["direccion"]["nro dpto"] = int(
            input(
                f"{i + 1}º departamento - Número de departamento: "
            )
        )
        #
        a[i]["disponibilidad"] = input(
            f"{i + 1}º departamento - Disponibilidad (ocupado, disponible): "
        )


def load_apartments_s(a):
    """

    :param a:
    :return:
    """
    a[0] = (1001, 150, "excelente", 50000.0, ("Roca", 100, 3, 31), "disponible")
    a[1] = (1002, 130, "regular", 10000.0, ("Roca", 100, 2, 22), "ocupado")
    a[2] = (1003, 110, "mala", 5000.0, ("Roca", 100, 2, 21), "disponible")
    a[3] = (1004, 120, "buena", 20000.0, ("Roca", 100, 3, 32), "disponible")
    a[4] = (1005, 100, "regular", 15000.0, ("Libertad", 70, 1, 11), "ocupado")
    a[5] = (1006, 250, "excelente", 70000.0, ("Libertad", 70, 1, 12), "ocupado")
    a[6] = (1007, 120, "buena", 30000.0, ("Libertad", 70, 2, 25), "disponible")
    a[7] = (1008, 130, "regular", 20000.0, ("Libertad", 70, 3, 34), "ocupado")
    a[8] = (1009, 300, "excelente", 80000.0, ("Roca", 210, 8, 88), "disponible")
    a[9] = (1010, 60, "mala", 5000.0, ("Roca", 210, 2, 28), "ocupado")


# ------------------------------------Item a------------------------------------


def big_excellent_available_apartment(a, dim, surface):
    """

    :param a:
    :param dim:
    :param surface:
    :return:
    """
    print(
        "\nLista de departamentos disponibles en un estado excelente y "
        "con una superficie mayor a " + str(surface) + "m²"
    )
    exist = False
    for i in range(dim):
        if (a[i]["superficie"] >= surface and a[i]["estado"] == "excelente"
                and a[i]["disponibilidad"] == "disponible"):
            exist = True
            print("\nCódigo de departamento:", a[i]["codigo"])
            print("Superficie: " + str(a[i]["superficie"]) + "m²")
            print("Estado:", a[i]["estado"])
            print("Precio: $" + str(a[i]["precio"]))
            print(
                "Dirección: " + str(a[i]["direccion"]["calle"]) + " "
                + str(a[i]["direccion"]["numero"]) + ", piso "
                + str(a[i]["direccion"]["piso"]) + ", departamento "
                + str(a[i]["direccion"]["nro dpto"])
            )
            print("Disponibilidad:", a[i]["disponibilidad"])
            print("")
    if not exist:
        print("Ningún departamento cumple con los requisitos.")


# ------------------------------------Item b------------------------------------


def check_apartments(a, dim, surface, state):
    """

    :param a:
    :param dim:
    :param surface:
    :param state:
    :return:
    """
    print(
        "\nDepartamentos en estado " + state + " con superficie "
        + str(surface) + "m²:\n"
    )
    exist = False
    for i in range(dim):
        if a[i]["superficie"] == surface and a[i]["estado"] == state:
            exist = True
            print("Precio: $" + str(a[i]["precio"]))
            print(
                "Dirección: " + str(a[i]["direccion"]["calle"]) + " "
                + str(a[i]["direccion"]["numero"]) + ", piso "
                + str(a[i]["direccion"]["piso"]) + ", departamento "
                + str(a[i]["direccion"]["nro dpto"])
            )
            print("")
    if not exist:
        print("\nNinguno.")


# ------------------------------------------------------------------------------


def print_menu():
    """

    :return:
    """
    print("-" * 60)
    print("MENU PRINCIPAL")
    print("Seleccione una opción:\n"
          "1- Cargar datos de los departamentos (dinámico).\n"
          "2- Cargar datos de los departamentos (estático).\n"
          "3- Consultar departamentos excelentes disponibles.\n"
          "4- Ingresar una solicitud de alquiler.\n"
          "5- Limpiar pantalla.\n\n"
          "0- Salir.")
    print("-" * 60)


def main():
    """

    :return:
    """
    address = np.dtype(
        [
            ("calle", "U20"),
            ("numero", int),
            ("piso", int),
            ("nro dpto", int)
        ]
    )
    apartment = np.dtype(
        [
            ("codigo", int),
            ("superficie", int),
            ("estado", "U9"),
            ("precio", float),
            ("direccion", address),
            ("disponibilidad", "U10")
        ]
    )
    apartments = np.empty(100, dtype=apartment)
    is_loaded = False
    run = True
    while run:
        print_menu()
        option = int(input("> "))
        if option == 0:
            run = False
            print("Ejecución finalizada.")
        elif option == 1:
            amount = -1
            while amount <= 0 or amount > 100:
                amount = int(input("Cantidad de departamentos (1-100): "))
            load_apartments_d(apartments, amount)
            print("Datos cargados.")
            is_loaded = True
        elif option == 2:
            amount = 10
            load_apartments_s(apartments)
            print("Datos cargados.")
            is_loaded = True
        elif option == 3:
            if is_loaded:
                surface = int(input("Ingrese la superficie mínima: "))
                big_excellent_available_apartment(apartments, amount, surface)
            else:
                print("Datos no cargados en el arreglo.")
        elif option == 4:
            if is_loaded:
                surface = int(input("Superficie: "))
                state = input("Estado (excelente, buena, regular o mala): ")
                check_apartments(apartments, amount, surface, state)
            else:
                print("Datos no cargados en el arreglo.")
        elif option == 5:
            console("cls")
        else:
            print("Opción inválida.")


# ------------------------------Programa Principal------------------------------
if __name__ == '__main__':
    main()
