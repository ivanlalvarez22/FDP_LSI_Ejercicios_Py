"""
@AUTOR: Iván L. Alvarez

Diagnóstico

Dado los siguientes problemas, defina las estructuras de datos adecuadas
para almacenar la información, diseñe el diagrama de flujo.

Una docente del profesorado tiene la siguiente información de los N
alumnos de un curso : DNI, cantidad de asistencias a clases, nota del
primer parcial, nota de trabajos prácticos, nota del 2do parcial

Se pide:

    a) Dado el DNI de un alumno informar el porcentaje de asistencias
    sobre un total de 15 clases.

    b) Generar una estructura de datos que posea para cada alumno:
    DNI, cantidad de inasistencias y categoria. El alumno será
    categorizado por su promedio de la siguiente manera:
    Promedio categoria 0 a 5 "Insuficiente" 6 a 8 "Aprobado"
    9 y 10 "Excelente"

    c) A partir de la estructura generada en el ítem (b) se pide dar
    de baja a los alumnos con más de 10 inasistencias.
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
          "5) Realizar ítem c)\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


# Nombre del Módulo: cargar_registro
# Descripción: Carga estática de los registros del vector
# Datos de entrada: el vector mis_alumnos
# Datos de salida:
def cargar_registro(ma):
    ma[0] = (38484357, 15, 10, 8, 9)
    ma[1] = (45784123, 10, 8, 7, 6)
    ma[2] = (14675345, 5, 8, 7, 6)
    ma[3] = (50647321, 2, 5, 4, 5)
    ma[4] = (47545124, 9, 10, 6, 9)
    return None


def mostrar_registro(ma, dim):
    print("DNI             ASISTENCIAS     NOTA 1ER PARCIAL     NOTA TP    NOTA 2DO PARCIAL")
    for i in range(dim):
        print(ma[i]["DNI"], end="        ")
        print(str(ma[i]["asistencias"]).ljust(4), end="            ")
        print(str(ma[i]["nota_1er_parcial"]).ljust(4), end="                 ")
        print(str(ma[i]["nota_trabajos_practicos"]).ljust(4), end="       ")
        print(ma[i]["nota_2do_parcial"])
    return None


# a) Dado el DNI de un alumno informar el porcentaje de asistencias
#     sobre un total de 15 clases.
def realizar_act_a(ma, dim):
    dni_alumno = int(input("Ingrese el DNI del alumno: "))
    porcentaje = 0
    for i in range(dim):
        if dni_alumno == ma[i]["DNI"]:
            porcentaje = ma[i]["asistencias"] / 15 * 100
    return porcentaje


# Nombre del módulo: realizar_act_b
# Descripción: carga los registros del vector estructura_alumnos
# Datos de entrada: mis_alumnos, dimension, estructura_alumnos
# Datos de salida: j (dimensión del vector estructura_alumnos)
def realizar_act_b(ma, dim, est_alum):
    j = 0
    for i in range(dim):
        promedio = (ma[i]["nota_1er_parcial"] + ma[i]["nota_trabajos_practicos"] + ma[i]["nota_2do_parcial"]) / 3
        est_alum[j]["DNI"] = ma[i]["DNI"]
        est_alum[j]["inasistencias"] = 15 - ma[i]["asistencias"]
        est_alum[j]["categoria"] = promedio
        j += 1
    return j


# Nombre del módulo: convertir_num_a_string
# Descripción: recibe un promedio y dependiendo de su valor transforma a una cadena de string
# Datos de entrada: promedio (float)
# Datos de salida: categoria (string)
def convertir_num_a_string(prom):
    categoria = ""
    if 0 <= prom <= 6:
        categoria = "Desaprobado"
    elif 7 <= prom <= 8:
        categoria = "Aprobado"
    elif 9 <= prom <= 10:
        categoria = "Excelente"
    return categoria


def mostrar_estructura(est_alum, dim):
    print("DNI          INASISTENCIAS            CATEGORIA")
    for i in range(dim):
        categoria = convertir_num_a_string(est_alum[i]["categoria"])
        print(est_alum[i]["DNI"], end="     ")
        print(str(est_alum[i]["inasistencias"]).ljust(2), end="                       ")
        print(categoria)
    return None


def eliminar_alumnos(est_alum, dim):
    i = 0
    while i < dim:
        if est_alum[i]["inasistencias"] > 10:  # Condición para eliminar
            j = i
            while j < dim - 1:
                est_alum[j]["DNI"] = est_alum[j + 1]["DNI"]
                est_alum[j]["inasistencias"] = est_alum[j + 1]["inasistencias"]
                est_alum[j]["categoria"] = est_alum[j + 1]["categoria"]
                j += 1
            dim -= 1
        else:
            i += 1
    return dim


# Programa principal

# Estructura del registro

tdatos_alumnos = np.dtype(
    [
        ("DNI", int),
        ("asistencias", int),
        ("nota_1er_parcial", float),
        ("nota_trabajos_practicos", float),
        ("nota_2do_parcial", float)
    ]
)

tdatos_alumnos_actb = np.dtype(
    [
        ("DNI", int),
        ("inasistencias", int),
        ("categoria", int)
    ]
)

n = 5
# Arreglo de registros
mis_alumnos = np.empty(n, dtype=tdatos_alumnos)
estructura_alumnos = np.empty(n, dtype=tdatos_alumnos_actb)
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado!")
        salir = True
    elif opc == 1:
        cargar_registro(mis_alumnos)
    elif opc == 2:
        mostrar_registro(mis_alumnos, n)
    elif opc == 3:
        print(f"El porcentaje de asistencia del alumno es: {realizar_act_a(mis_alumnos, n)}%")
    elif opc == 4:
        dim_estructura_b = realizar_act_b(mis_alumnos, n, estructura_alumnos)
        mostrar_estructura(estructura_alumnos, dim_estructura_b)
    elif opc == 5:
        dim_estructura_b = eliminar_alumnos(estructura_alumnos, n)
        mostrar_estructura(estructura_alumnos, dim_estructura_b)
