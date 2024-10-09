# Apellido: Alvarez             DNI: 38484357           CARRERA: LSI
# Nombre: Iván Leandro          LEGAJO: 458/2021
# Una empresa constructora para gestionar sus proyectos registra la siguiente información: código de proyecto,
# nombre del cliente, tipo de proyecto {‘D’- Departamento, ‘C’- Casa, ‘E’ -Edificio}, duración  -  expresada en meses,
# fecha de inicio (mes, año),  costo en dólares y estado del proyecto { 0 – En Ejecución, 1 - Finalizado}.
# Como programador se le pide que realice lo siguiente:

# 1) Colocar los parámetros en la descripción de todos los módulos provistos en el código y convocar al
# módulo CargarProyectos. (5 Puntos)

# 2) Proyectos de Un Tipo: generar una estructura de datos con el código de proyecto y el costo, de
# todos aquellos proyectos que son de un determinado tipo de proyecto a ser ingresado,
# debiendo luego mostrar en el programa principal la estructura resultante. (15 Puntos)

# 3)    Informe de Costos: para un tipo de proyecto determinado, mostrar la siguiente información de acuerdo al
# siguiente formato: (15 Puntos)

# Tipo de proyecto: E                               Denominación: Edificio

# Cantidad de Proyectos: 3                     Costo de todos los proyectos: $ 13.500.000

# Si no existen proyectos del tipo de proyecto ingresado, mostrar el siguiente mensaje: “No hay obras para el
# tipo de proyecto solicitado”
# Nota: para su realización debe diseñar el procedimiento ObtenerDatosTipoProyecto, y en su interior convocar al
# módulo DescripcionTipoProyecto.

# Nombre del Módulo: ObtenerDatosTipoProyecto
# Descripción: determina la cantidad y el costo de todos los proyectos para un determinado tipo de proyecto y su
# denominación. En caso de que el código no exista, se deberá retornar cantidad cero, costo cero y
# denominación vacía (“”)

# Datos de Entrada: tipoDeProyecto
# Datos de Salida: CantidadProyectos, CostoTodosProyectos, DenominacionTipoDeProyecto

# 4) Proyecto Más Viejo: mostrar la siguiente información para todos los proyectos que aún no han finalizado.
# (15 Puntos)

# Proyectos Sin Finalizar
# Código                        Fecha de Inicio                Fecha de Finalización    Meses Para Terminar
#
#   346                         8/2018                         12/2021                         1
#
#   265                         2/2020                         2/2022                          3
#
#   723                         10/2021                        4/2023                          17

# Total de Proyectos Sin Terminar: 3

import numpy as np

# Definición de módulos


def mostrar_menu():
    print("------------MENÚ PRINCIPAL---------------\n"
          "1) Cargar proyectos\n"
          "2) Mostrar proyectos\n"
          "3) Realizar act '2' (Generar estructura)\n"
          "4) Realizar act '3' (Informe de costos para proyecto de determinado tipo)\n"
          "5) Relizar")
    op = int(input("Por favor ingrese ualizar act '4' (Mostrar información para proyectos no finalizados)\n"
                   "Ingrese el '0' para finana opción para continuar: "))
    return op


# Nombre del módulo: CargarProyectos
# Descripción: realiza la carga de los proyectos de la empresa.
# Datos de Entrada:
# Datos de Salida:
def cargar_proyectos(proyectos):
    dim_proyectos = 6
    proyectos[0] = (345, "Belen Garcia", 'C', 25, (7, 2018), 55000, 1)
    proyectos[1] = (346, "Carlos Trejo", 'E', 40, (8, 2018), 8000000, 0)
    proyectos[2] = (478, "Luis Cano", 'C', 18, (9, 2019), 45000, 1)
    proyectos[3] = (265, "Ana Luna", 'E', 24, (2, 2020), 3000000, 0)
    proyectos[4] = (546, "Sofia Lopez", 'C', 4, (4, 2021), 50000, 1)
    proyectos[5] = (723, "Juan Perez", 'E', 18, (10, 2021), 2500000, 0)
    print("\nProyectos cargados correctamente\n")
    return dim_proyectos


# Nombre del Módulo: DescripcionTipoProyecto
# Descripción: retorna la descripcion o denominacion de un tipo de Proyecto.
# Datos de Entrada:
# Datos de Salida:
def descripcion_tipo_proyecto(proyecto):
    descripcion = ""
    if proyecto == 'D':
        descripcion = "Departamento"
    elif proyecto == 'C':
        descripcion = "Casa"
    elif proyecto == 'E':
        descripcion = "Edificio"
    return descripcion


def convertir_num_a_string(num):
    if num == 0:
        string = "En ejecución"
    else:
        string = "Finalizado"
    return string


def mostrar_proyectos(proyectos, dim_proyectos):
    print("COD    NOMBRE            TIPO DE PROYECTO      DURACIÓN        FECHA DE INICIO       COSTO          ESTADO")
    for i in range(dim_proyectos):
        tipo_proyectos = descripcion_tipo_proyecto(proyectos[i]["tipo_proyecto"])
        estado = convertir_num_a_string(proyectos[i]["estado_proyecto"])
        print(proyectos[i]["codigo_proyecto"], end="    ")
        print(str(proyectos[i]["nombre_cliente"]).ljust(15), end="   ")
        print(str(tipo_proyectos).ljust(12), end="          ")
        print(str(proyectos[i]["duracion"]).ljust(2), end="              ")
        print(str(proyectos[i]["fecha_inicio"]["mes"]).ljust(2) + "/" +
              str(proyectos[i]["fecha_inicio"]["anio"]), end="             ")
        print("$", str(proyectos[i]["costo"]).ljust(12), end="   ")
        print(estado)
    return None


def generar_proyectos_de_un_tipo(proyectos, dim_proyectos, estructura_t_proyecto):
    tipo = input("Ingrese un tipo de proyecto ('D' Departamento, 'C' Casa, 'E' Edificio): ")
    tipo = tipo.upper()
    b = False
    j = 0
    for i in range(dim_proyectos):
        if proyectos[i]["tipo_proyecto"] == tipo:
            b = True
            estructura_t_proyecto[j]["codigo_proyecto"] = proyectos[i]["codigo_proyecto"]
            estructura_t_proyecto[j]["costo"] = proyectos[i]["costo"]
            j += 1
    if not b:
        print(f"\nNo hay proyectos de tipo '{descripcion_tipo_proyecto(tipo)}'\n")
    return j


def mostrar_proyectos_de_un_tipo(estructura_t_proyecto, dim_estructura):
    print("")
    print("COD       COSTO")
    for i in range(dim_estructura):
        print(estructura_t_proyecto[i]["codigo_proyecto"], end="     ")
        print("$", estructura_t_proyecto[i]["costo"])
    print("")
    return None


# Nombre del Módulo: obtener_datos_tipo_proyecto
# Descripción: determina la cantidad y el costo de todos los proyectos para un determinado tipo de proyecto
# y su denominación. En caso de que el código no exista, se deberá retornar cantidad cero, costo cero y
# denominación vacía (“”)
# Datos de Entrada: tipo_proyectos
# Datos de Salida: cant_de_proyectos, costo_todos_proyectos, denominacion
def obtener_datos_tipo_proyecto(proyectos, dim_proyectos, tipo_proyectos):
    cant_de_proyectos = 0
    costo_todos_proyectos = 0
    denominacion = ""
    existe = False
    for i in range(dim_proyectos):
        if proyectos[i]["tipo_proyecto"] == tipo_proyectos:
            existe = True
            tipo_proyectos = proyectos[i]["tipo_proyecto"]
            cant_de_proyectos += 1
            costo_todos_proyectos += proyectos[i]["costo"]
            denominacion = descripcion_tipo_proyecto(tipo_proyectos)
    if existe:
        print("")
        print("Tipo de proyecto:", tipo_proyectos, "      Denominación:", denominacion)
        print("Cantidad de proyectos:", cant_de_proyectos, " Costo de todos los proyectos: $", costo_todos_proyectos)
        print("")
    else:
        print("\nNo hay obras para el tipo de proyecto solicitado\n")
        return cant_de_proyectos, costo_todos_proyectos, denominacion
    return None


# Nombre del Módulo: Fecha_finalizacion
# Descripción: determina el mes y el año de finalización de un proyecto
# Datos de Entrada: fecha_inicio, duracion_proyecto
# Datos de Salida: fecha_fin
def fecha_finalizacion(fecha_inicio, duracion_proyecto):
    fecha_fin = np.empty(1, dtype=tipo_fecha)
    anios_proyecto = duracion_proyecto / 12
    resto_meses_proyecto = duracion_proyecto % 12
    anio_finalizacion = fecha_inicio['anio'] + anios_proyecto
    mes_finalizacion = fecha_inicio['mes'] + resto_meses_proyecto
    if mes_finalizacion > 12:
        mes_finalizacion = mes_finalizacion - 12
        anio_finalizacion = anio_finalizacion + 1

    fecha_fin['mes'] = mes_finalizacion
    fecha_fin['anio'] = anio_finalizacion
    return fecha_fin


def calcular_meses_fin_proyecto(mes_inicio, anio_inicio, mes_actual, duracion):
    meses_para_finalizar = (12 - mes_inicio) + (12 * (2021 - (anio_inicio + 1))) + mes_actual
    meses_para_finalizar = duracion - meses_para_finalizar
    return meses_para_finalizar


def mostrar_proyectos_sin_finalizar(proyectos, dim_proyectos):
    mes_actual = int(input("Ingrese el número de mes actual (1 - 12): "))
    total_proy_sin_terminar = 0
    print("\nProyectos sin finalizar:\n"
          "CODIGO      FECHA DE INICIO      FECHA DE FINALIZACIÓN      MESES PARA TERMINAR")
    j = 0
    for i in range(dim_proyectos):
        if proyectos[i]["estado_proyecto"] == 0:
            total_proy_sin_terminar += 1
            print(proyectos[i]["codigo_proyecto"], end="         ")
            print(str(proyectos[i]["fecha_inicio"]["mes"]).ljust(2) + "/" +
                  str(proyectos[i]["fecha_inicio"]["anio"]), end="              ")
            vector_fecha_fin[j] = fecha_finalizacion(proyectos[i]["fecha_inicio"], proyectos[i]["duracion"])
            print(str(vector_fecha_fin[j]["mes"]).ljust(2) + "/" +
                  str(vector_fecha_fin[j]["anio"]), end="                    ")
            meses = calcular_meses_fin_proyecto(proyectos[i]["fecha_inicio"]["mes"],
                                                proyectos[i]["fecha_inicio"]["anio"], mes_actual,
                                                proyectos[i]["duracion"])
            print(meses)
            j += 1
    print(f"Total de Proyectos Sin Terminar: {total_proy_sin_terminar}")
    print("")


# __________---------- Programa principal ----------_____
# Estructura del registro

tipo_nuevo_proyecto = np.dtype(
    [
        ("codigo_proyecto", int),
        ("costo", float)
    ]
)

tipo_fecha = np.dtype(
    [
        ("mes", int),
        ("anio", int)
    ]
)

tipo_proyecto = np.dtype(
    [
        ("codigo_proyecto", int),
        ("nombre_cliente", "U30"),
        ("tipo_proyecto", "U1"),
        ("duracion", int),
        ("fecha_inicio", tipo_fecha),
        ("costo", float),
        ("estado_proyecto", int)
    ]
)

# Arreglo de registros

max_proyectos = 20
empresa = np.empty(max_proyectos, dtype=tipo_proyecto)
estructura_de_tipo_proyecto = np.empty(max_proyectos, dtype=tipo_nuevo_proyecto)
vector_fecha_fin = np.empty(max_proyectos, dtype=tipo_fecha)
salir = False
dimension_proyecto = 0
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("¡Programa finalizado!")
        salir = True
    elif opc == 1:
        dimension_proyecto = cargar_proyectos(empresa)
    elif opc == 2:
        mostrar_proyectos(empresa, dimension_proyecto)
    elif opc == 3:
        dim_estructura_tipo_proyecto = generar_proyectos_de_un_tipo(empresa, dimension_proyecto,
                                                                    estructura_de_tipo_proyecto)
        if dim_estructura_tipo_proyecto > 0:
            mostrar_proyectos_de_un_tipo(estructura_de_tipo_proyecto, dim_estructura_tipo_proyecto)
    elif opc == 4:
        tipo_de_proyecto = input("Ingrese un tipo de proyecto ('D' Departamento, 'C' Casa, 'E' Edificio): ")
        obtener_datos_tipo_proyecto(empresa, dimension_proyecto, tipo_de_proyecto)
    elif opc == 5:
        mostrar_proyectos_sin_finalizar(empresa, dimension_proyecto)

""" Iván L. Alvarez"""
