# Una docente de un Colegio privado tiene la siguiente información de los alumnos de un curso: DNI,
# Cantidad de Cuotas Abonadas, Cantidad de Inasistencias a Clases, Nota de Matemática, Nota de Lengua,
# Nota de Historia, Nota de Geografía, se pide:

# a) Dado el DNI de un alumno informar la cantidad de cuotas adeudadas. En caso de que el alumno no
# pertenezca a la institución, mostrar el mensaje “Alumno Inexistente”.

# b) Generar una estructura de datos que posea para cada alumno: DNI, Cantidad de inasistencias y Categoría.
# El alumno será categorizado por su promedio de la siguiente manera:

# Promedio         |  Categoría
# 0 a 5            | “Insuficiente”
# 6 a 8            | “Aprobado”
# 9 y 10           | “Excelente”

# c) A partir de la estructura generada en el ítem (b) se pide dar de baja a los alumnos con más de 10 inasistencias.

import numpy as np

# Definición de módulos


def mostrar_menu():
    print("-------------MENÚ PRINCIPAL------------------\n"
          "1) Cargar registro\n"
          "2) Mostrar registro\n"
          "3) Informar cuotas adeudadas según dni de alumno\n"
          "4) Generar estructura según categoría\n"
          "5) Dar de baja los alumnos con más de 10 inasistencias\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


def cargar_registro(ma):
    ma[0] = (38484357, 9, 7, 10, 7, 10, 10)
    ma[1] = (45954786, 4, 8, 10, 5, 7, 6)
    ma[2] = (45666664, 1, 5, 7, 8, 1, 6)
    ma[3] = (39548979, 9, 13, 9, 8, 7, 6)
    ma[4] = (46456879, 6, 7, 10, 8, 7, 2)
    ma[5] = (39656556, 4, 4, 7, 8, 7, 9)
    ma[6] = (45648797, 2, 180, 1, 8, 2, 6)
    ma[7] = (39545644, 10, 0, 3, 1, 1, 6)
    ma[8] = (42546879, 7, 9, 1, 8, 9, 6)
    ma[9] = (40546468, 9, 10, 9, 9, 9, 9)
    print("\nRegistro cargado correctamente\n")
    return None


def mostrar_registro(ma, d):
    print("DNI         CUOTAS ABONADAS    CANT. INASISTENCIAS    N. MAT    N. LENGUA    N. HISTORIA  N. GEOGRAFIA")
    for i in range(d):
        print(ma[i]["dni"], end="    ")
        print(str(ma[i]["cant_cuotas_abonadas"]).ljust(2), end="                 ")
        print(str(ma[i]["cant_inasistencias"]).ljust(3), end="                    ")
        print(str(ma[i]["nota_matematica"]).ljust(4), end="      ")
        print(str(ma[i]["nota_lengua"]).ljust(4), end="         ")
        print(str(ma[i]["nota_historia"]).ljust(4), end="         ")
        print(str(ma[i]["nota_geografia"]).ljust(4))
    return None


def informar_cuotas_adeudadas(ma, d):
    i = 0
    b = False
    dni = int(input("Por favor ingrese el dni del alumno: "))
    # También la condición podría funcionar sin la conjunción con la falsedad de b salvo que en ésta
    # ocasión optimizamos nuestro ciclo al terminar la iteración en el instante que que "b = True". Caso contrario
    # el ciclo seguiría repitiéndose hasta recorrer todo el arreglo de registros.
    while i < d and not b:
        if ma[i]["dni"] == dni:
            cuotas_adeudadas = 10 - ma[i]["cant_cuotas_abonadas"]
            print(f"La cantidad de cuotas adeudadas por el alumno ingresado son: {cuotas_adeudadas}")
            b = True
        i += 1
    if not b:
        print("Alumno inexistente")
    return None


def calcular_promedio_nota(n1, n2, n3, n4):
    promedio = (n1 + n2 + n3 + n4) / 4
    return promedio


def calcular_categoria(promedio):
    categoria = ""
    if 0 <= promedio < 6:
        categoria = "Insuficiente"
    elif 6 <= promedio < 9:
        categoria = "Aprobado"
    elif 9 <= promedio <= 10:
        categoria = "Excelente"
    return categoria


def generar_estructura_cat(ma, d, mac):
    for i in range(d):
        promedio = calcular_promedio_nota(ma[i]["nota_matematica"], ma[i]["nota_lengua"], ma[i]["nota_historia"],
                                          ma[i]["nota_geografia"])
        categoria = calcular_categoria(promedio)
        mac[i]["dni"] = ma[i]["dni"]
        mac[i]["cant_inasistencias"] = ma[i]["cant_inasistencias"]
        mac[i]["categoria"] = categoria
    return None


def mostrar_estructura_cat(mac, d):
    for i in range(d):
        print(mac[i]["dni"], mac[i]["cant_inasistencias"], mac[i]["categoria"])
    return None


def eliminar_alumnos(mac, d):
    i = 0
    while i < d:
        if mac[i]["cant_inasistencias"] >= 10:  # Condición para eliminar
            j = i
            while j < d - 1:
                mac[j]["dni"] = mac[j + 1]["dni"]
                mac[j]["cant_inasistencias"] = mac[j + 1]["cant_inasistencias"]
                mac[j]["categoria"] = mac[j + 1]["categoria"]
                j += 1
            d -= 1
        else:
            i += 1
    return d


# Programa principal
# Estructura del registro

Tdatos_alumnos = np.dtype(
    [
        ("dni", int),
        ("cant_cuotas_abonadas", int),
        ("cant_inasistencias", int),
        ("nota_matematica", float),
        ("nota_lengua", float),
        ("nota_historia", float),
        ("nota_geografia", float)
    ]
)

Tdatos_alumnos_cat = np.dtype(
    [
        ("dni", int),
        ("cant_inasistencias", int),
        ("categoria", "U15")
    ]
)

# Arreglo de registros
N = 10
mis_alumnos = np.empty(N, dtype=Tdatos_alumnos)
mis_alumnos_cat = np.empty(10, dtype=Tdatos_alumnos_cat)
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado!")
        salir = True
    elif opc == 1:
        cargar_registro(mis_alumnos)
    elif opc == 2:
        mostrar_registro(mis_alumnos, N)
    elif opc == 3:
        informar_cuotas_adeudadas(mis_alumnos, N)
    elif opc == 4:
        generar_estructura_cat(mis_alumnos, N, mis_alumnos_cat)
        mostrar_estructura_cat(mis_alumnos_cat, 10)
    elif opc == 5:
        dim_cat = eliminar_alumnos(mis_alumnos_cat, 10)
        mostrar_estructura_cat(mis_alumnos_cat, dim_cat)
