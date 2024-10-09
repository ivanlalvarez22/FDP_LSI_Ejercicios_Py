import numpy as np
from os import system as console

"""
5. El Departamento Personal de la UNSE registra para sus profesores los
siguientes datos: Número de Legajo, Documento, Apellido y Nombre,
Fecha de Nacimiento, Sexo {‘M’,’F’}, Código de Facultad, Fecha de Ingreso y
Estado {1-Activo, 2-Pasivo, 3-En Edad de Jubilarse}.
Mostrar:

a) Número de Legajo y Apellido y Nombre de aquellos empleados de la universidad
de sexo femenino y que se encuentran activos.

b) Número de Legajo de todos los empleados con una antigüedad igual a 25 años.

c) Actualizar el registro del Departamento Personal, con aquellos profesores que
se encuentren en edad de jubilarse, para lo cual deberá tener en cuenta que las
mujeres se jubilan con 60 años de edad, y los hombres con 65 años.
"""


# ------------------------------Sección de Módulos------------------------------


def leap_year(year: int) -> bool:
    """
    Retorna verdadero si el año ingresado es bisiesto, falso en caso contrario.
    :param year: Año.
    :return: bool
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def valid_date(day: int, month: int, year: int) -> bool:
    """
    Retorna verdadero si la fecha ingresada es válida, falso en caso contrario.
    :param day: Dia.
    :param month: Mes.
    :param year: Año.
    :return: is_valid (bool)
    """
    is_valid = False
    if 1 <= month <= 12 and 999 < year:
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8
                or month == 10 or month == 12):
            if 1 <= day <= 31:
                is_valid = True
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if 1 <= day <= 30:
                is_valid = True
        else:
            if leap_year(year):
                if 1 <= day <= 29:
                    is_valid = True
            elif 1 <= day <= 28:
                is_valid = True
    return is_valid


def load_personnel_record_d(p, dim: int) -> None:
    """
    Carga dinámica de datos en el arreglo personnel_record.
    :param p: Arreglo personnel_record
    :param dim: Dimensión de personnel_record.
    :return: None
    """
    for i in range(dim):
        # Ingreso de N.º de legajo.
        p[i]["legajo"] = 0
        while p[i]["legajo"] < 1:
            p[i]["legajo"] = int(
                input(f"{i + 1}º profesor - legajo (positivo): "
                      )
            )
        # Ingreso de Documento.
        p[i]["dni"] = 0
        while p[i]["dni"] < 1:
            p[i]["dni"] = int(input(f"{i + 1}º profesor - DNI (positivo): "))
        # Ingreso de Apellido.
        p[i]["apellido"] = input(f"{i + 1}º profesor - Apellido: ")
        # Ingreso de Nombre.
        p[i]["nombre"] = input(f"{i + 1}º profesor - Nombre: ")
        # Ingreso de Fecha de nacimiento.
        p[i]["nacimiento"]["dia"] = 0
        p[i]["nacimiento"]["mes"] = 0
        p[i]["nacimiento"]["año"] = 0
        while not valid_date(p[i]["nacimiento"]["dia"],
                             p[i]["nacimiento"]["mes"],
                             p[i]["nacimiento"]["año"]):
            print(
                f"{i + 1}º profesor - Fecha de nacimiento (Solo fechas válidas):"
            )
            p[i]["nacimiento"]["dia"] = int(input("Dia: "))
            p[i]["nacimiento"]["mes"] = int(input("Mes: "))
            p[i]["nacimiento"]["año"] = int(input("Año: "))
        # Ingreso de Sexo.
        p[i]["sexo"] = ""
        while not (p[i]["sexo"] == "M" or p[i]["sexo"] == "F"):
            p[i]["sexo"] = input(f"{i + 1}º profesor - Sexo (M, F): ").upper()
        # Ingreso de Código de facultad.
        p[i]["codigo"] = 0
        while p[i]["codigo"] < 1:
            p[i]["codigo"] = int(
                input(
                    f"{i + 1}º profesor - Código de facultad (positivo): "
                )
            )
        # Ingreso de Fecha de ingreso.
        p[i]["ingreso"]["dia"] = 0
        p[i]["ingreso"]["mes"] = 0
        p[i]["ingreso"]["año"] = 0
        while not valid_date(p[i]["ingreso"]["dia"],
                             p[i]["ingreso"]["mes"],
                             p[i]["ingreso"]["año"]):
            print(
                f"{i + 1}º profesor - Fecha de ingreso (Solo fechas válidas):"
            )
            p[i]["ingreso"]["dia"] = int(input("Dia: "))
            p[i]["ingreso"]["mes"] = int(input("Mes: "))
            p[i]["ingreso"]["año"] = int(input("Año: "))
        # Ingreso de Estado.
        p[i]["estado"] = 0
        while not (p[i]["estado"] == 1 or p[i]["estado"] == 2
                   or p[i]["estado"] == 3):
            p[i]["estado"] = int(
                input(
                    f"{i + 1}º profesor - Estado "
                    "(1-Activo, 2-Pasivo, 3-En Edad de Jubilarse): "
                )
            )


def load_personnel_record_s(p) -> None:
    """
    Carga estática de datos en el arreglo personnel_record.
    :param p: Arreglo personnel_record
    :return: None
    """
    p[0] = (
        14, 16345678, "S.", "Juan", (12, 5, 1968), "M", 21, (28, 10, 1996), 1
    )
    p[1] = (
        80, 30548789, "F.", "Paula", (17, 5, 1980), "F", 21, (26, 10, 2010), 1
    )
    p[2] = (
        32, 15666664, "G.", "Judas", (6, 6, 1966), "M", 16, (1, 1, 2000), 2
    )
    p[3] = (
        175, 39548979, "R.", "Pedro", (14, 7, 1995), "M", 21, (26, 10, 2020), 1
    )
    p[4] = (
        48, 26456879, "E.", "Lucas", (12, 12, 1980), "M", 16, (26, 10, 1996), 2
    )
    p[5] = (
        39, 9656556, "J.", "Elena", (8, 8, 1950), "F", 18, (26, 10, 1985), 3
    )
    p[6] = (
        1, 4564879, "D.", "Pablo", (29, 2, 1940), "M", 18, (26, 7, 1970), 2
    )
    p[7] = (
        121, 39545644, "L.", "Gracia", (26, 5, 1995), "F", 18, (26, 10, 2018), 1
    )
    p[8] = (
        92, 32546879, "B.", "Mateo", (11, 11, 1985), "M", 21, (21, 10, 2015), 1
    )
    p[9] = (
        33, 20546468, "C.", "Victoria", (2, 2, 1975), "F", 21, (20, 2, 2000), 1
    )


# ------------------------------------Item a------------------------------------


def female_active(p, dim: int) -> None:
    """
    Muestra Número de Legajo, Apellido y Nombre de aquellos empleados de la
    universidad de sexo femenino y que se encuentran activos.
    :param p: Arreglo personnel_record
    :param dim: Dimensión de personnel_record.
    :return:
    """
    print(
        "Número de Legajo, Apellido y Nombre de aquellos empleados de la "
        "universidad de sexo femenino y que se encuentran activos:\n"
    )
    exist = False
    for i in range(dim):
        if p[i]["sexo"] == "F" and p[i]["estado"] == 1:
            exist = True
            print("Número de legajo:", p[i]["legajo"])
            print("Apellido:", p[i]["apellido"])
            print("Nombre:", p[i]["nombre"])
            print("")
    if not exist:
        print("No hay empleadas activas en la universidad.")


# ------------------------------------Item b------------------------------------


def years(ad: int, am: int, ay: int, d: int, m: int, y: int, yrs: int) -> bool:
    """
    Retorna verdadero si pasó una determinada cantidad de años entre las 2
    fechas, falso en caso contrario.
    :param ad: Dia actual.
    :param am: Mes actual.
    :param ay: Año actual.
    :param d: Dia.
    :param m: Mes.
    :param y: Año.
    :param yrs: Cantidad de años.
    :return: bool
    """
    return (
            ((ay - y == yrs) and ((am > m) or (am == m and ad >= d)))
            or ((ay - y == yrs + 1) and ((am < m) or (am == m and ad <= d)))
    )


def seniority_25(p, dim: int, day: int, month: int, year: int) -> None:
    """
    Muestra el Número de Legajo de todos los empleados con una antigüedad igual
    a 25 años.
    :param p: Arreglo personnel_record
    :param dim: Dimensión de personnel_record.
    :param day: Dia actual.
    :param month: Mes actual.
    :param year: Año actual.
    :return: None
    """
    print(
        "Número de Legajo de todos los empleados "
        "con una antigüedad igual a 25 años:\n"
    )
    exist = False
    for i in range(dim):
        if years(
                day, month, year, p[i]["ingreso"]["dia"],
                p[i]["ingreso"]["mes"], p[i]["ingreso"]["año"], 25
        ):
            exist = True
            print("Número de legajo:", p[i]["legajo"])
            print("")
    if not exist:
        print(
            "No hay empleados con una antigüedad "
            "igual a 25 años en la universidad."
        )


# ------------------------------------Item c------------------------------------


def update_retired(p, dim: int, day: int, month: int, year: int) -> None:
    """
    Actualiza el registro del Departamento Personal, con aquellos profesores
    que se encuentren en edad de jubilarse.
    :param p: Arreglo personnel_record
    :param dim: Dimensión de personnel_record.
    :param day: Dia actual.
    :param month: Mes actual.
    :param year: Año actual.
    :return: None
    """
    for i in range(dim):
        if ((p[i]["sexo"] == "M" and (years(
                day, month, year, p[i]["nacimiento"]["dia"],
                p[i]["nacimiento"]["mes"], p[i]["nacimiento"]["año"], 65)
                                      or year - p[i]["nacimiento"][
                                          "año"] >= 66))
                or (p[i]["sexo"] == "F" and (years(
                    day, month, year, p[i]["nacimiento"]["dia"],
                    p[i]["nacimiento"]["mes"], p[i]["nacimiento"]["año"], 60)
                                             or year - p[i]["nacimiento"][
                                                 "año"] >= 61))):
            if p[i]["estado"] == 1:
                p[i]["estado"] = 3


# ------------------------------------------------------------------------------


def get_state(num: int) -> str:
    """
    Retorna un texto con el estado del profesor.
    :param num: 1, 2 o 3
    :return: state
    """
    if num == 1:
        state = "Activo"
    elif num == 2:
        state = "Pasivo"
    elif num == 3:
        state = "En Edad de Jubilarse"
    else:
        state = ""
    return state


def print_record(p, dim: int) -> None:
    """
    Muestra el registro del departamento personal.
    :param p: Arreglo personnel_record
    :param dim: Dimensión de personnel_record.
    :return: None
    """
    print("REGISTRO DEL DEPARTAMENTO PERSONAL\n")
    print("LEGAJO   DNI        APELLIDO Y NOMBRE        NACIMIENTO   "
          "SEXO   CÓD.FACULTAD   INGRESO      ESTADO")
    for i in range(dim):
        file_num = str(p[i]["legajo"])
        doc = str(p[i]["dni"])
        name = str(p[i]["apellido"] + " " + p[i]["nombre"])
        birth = (
                str(p[i]["nacimiento"]["dia"]) + "/"
                + str(p[i]["nacimiento"]["mes"]) + "/"
                + str(p[i]["nacimiento"]["año"])
        )
        sex = str(p[i]["sexo"])
        code = str(p[i]["codigo"])
        entry = (
                str(p[i]["ingreso"]["dia"]) + "/"
                + str(p[i]["ingreso"]["mes"]) + "/"
                + str(p[i]["ingreso"]["año"])
        )
        state = get_state(p[i]["estado"])
        print(
            file_num + " " * (9 - len(file_num)) + doc + " " * (11 - len(doc))
            + name + " " * (25 - len(name)) + birth + " " * (13 - len(birth))
            + sex + " " * 6 + code + " " * (15 - len(code))
            + entry + " " * (13 - len(entry)) + state
        )


def print_menu() -> None:
    """
    Muestra el menu principal.
    :return: None
    """
    print("-" * 60)
    print("MENU PRINCIPAL")
    print("Seleccione una opción:\n"
          "1- Cargar datos de los profesores (dinámico).\n"
          "2- Cargar datos de los profesores (estático).\n"
          "3- Consultar empleadas activas.\n"
          "4- Consultar empleados con 25 años de antigüedad.\n"
          "5- Actualizar estado en registro (Edad de Jubilarse).\n"
          "6- Mostrar registro.\n"
          "7- Ajustar fecha.\n"
          "8- Limpiar pantalla.\n\n"
          "0- Salir.")
    print("-" * 60)


def main() -> None:
    """
    Función principal.
    :return: None
    """
    date = np.dtype(
        [
            ("dia", int),
            ("mes", int),
            ("año", int)
        ]
    )
    professor = np.dtype(
        [
            ("legajo", int),
            ("dni", int),
            ("apellido", "U20"),
            ("nombre", "U20"),
            ("nacimiento", date),
            ("sexo", "U1"),
            ("codigo", int),
            ("ingreso", date),
            ("estado", int)
        ]
    )
    personnel_record = np.empty(100, dtype=professor)
    day, month, year = 1, 11, 2021
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
                amount = int(input("Cantidad de profesores (1-100): "))
            load_personnel_record_d(personnel_record, amount)
            print("Datos cargados.")
            is_loaded = True
        elif option == 2:
            amount = 10
            load_personnel_record_s(personnel_record)
            print("Datos cargados.")
            is_loaded = True
        elif option == 3:
            if is_loaded:
                female_active(personnel_record, amount)
            else:
                print("Datos no cargados en el arreglo.")
        elif option == 4:
            if is_loaded:
                seniority_25(personnel_record, amount, day, month, year)
            else:
                print("Datos no cargados en el arreglo.")
        elif option == 5:
            if is_loaded:
                update_retired(personnel_record, amount, day, month, year)
                print("Estados actualizados.")
            else:
                print("Datos no cargados en el arreglo.")
        elif option == 6:
            if is_loaded:
                print_record(personnel_record, amount)
            else:
                print("Datos no cargados en el arreglo.")
        elif option == 7:
            day, month, year = 0, 0, 0
            while not valid_date(day, month, year):
                print("Ingresar fecha de hoy:")
                day = int(input("Dia: "))
                month = int(input("Mes: "))
                year = int(input("Año: "))
            print("Fecha actualizada.")
        elif option == 8:
            console("cls")
        else:
            print("Opción inválida.")


# -------------------------------Programa Principal-----------------------------
if __name__ == '__main__':
    main()
