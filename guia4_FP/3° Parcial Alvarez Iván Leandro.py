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
#   346                         8/2018                         1/2022                          2
#
#   265                         2/2020                         2/2022                          3
#
#   723                         10/2021                        4/2023                          17

# Total de Proyectos Sin Terminar: 3

import numpy as np

# Definición de módulos


def mostrar_menu():
    print("------------MENÚ PRINCIPAL---------------\n"
          "1) Cargar registro\n"
          "2) Mostrar registro\n"
          "3) Realizar act 2\n"
          "4) Realizar act 3\n"
          "5) Realizar act 4\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


# Nombre del módulo: cargar_proyectos
# Descripción: realiza la carga de los proyectos de la empresa.
# Datos de Entrada: mis_proyectos
# Datos de Salida: dimensión del arreglo
def cargar_proyectos(proyectos):
    dim_proyectos = 6
    proyectos[0] = (345, "Belen Garcia", 'C', 25, (7, 2018), 55000, 1)
    proyectos[1] = (346, "Carlos Trejo", 'E', 40, (8, 2018), 8000000, 0)
    proyectos[2] = (478, "Luis Cano", 'C', 18, (9, 2019), 45000, 1)
    proyectos[3] = (265, "Ana Luna", 'E', 24, (2, 2020), 3000000, 0)
    proyectos[4] = (546, "Sofia Lopez", 'C', 4, (4, 2021), 50000, 1)
    proyectos[5] = (723, "Juan Perez", 'E', 18, (10, 2021), 2500000, 0)
    print("\nRegistro cargado exitosamente!\n")
    return dim_proyectos


# Nombre del Módulo: convertir_u1_a_string
# Descripción: retorna la descripcion o denominacion de un tipo de Proyecto.
# Datos de Entrada: una letra
# Datos de Salida: la denominación de un tipo de proyecto
def convertir_u1_a_string(letra):
    if letra == "D":
        string = "Departamento"
    elif letra == "C":
        string = "Casa"
    else:
        string = "Edificio"
    return string


def convertir_num_string(estado):
    if estado == 1:
        string = "Finalizado"
    else:
        string = "En ejecución"
    return string


def mostrar_proyectos(proyectos, d):
    print("COD      NOMBRE      TIPO      DURACIÓN      FECHA INICIO      COSTO      ESTADO")
    for i in range(d):
        tipo = convertir_u1_a_string(proyectos[i]["tipo"])
        estado = convertir_num_string(proyectos[i]["estado"])
        print(proyectos[i]["codigo"], end="   ")
        print(str(proyectos[i]["nombre_cliente"]).ljust(15), end="   ")
        print(str(tipo).ljust(10), end="   ")
        print(proyectos[i]["duracion"], end="   ")
        print(str(proyectos[i]["fecha_inicio"]["mes"]) + "/" + str(proyectos[i]["fecha_inicio"]["año"]), end="   ")
        print("$", proyectos[i]["costo"], end="   ")
        print(estado)
    return None


def generar_proyectos_de_tipo(proyectos, d, estructura):
    tipo = input("Ingrese un tipo de proyecto ('D': Departamento, 'C': Casa, 'E': Edificio): ")
    j = 0
    for i in range(d):
        if proyectos[i]["tipo"] == tipo:
            estructura[j]["codigo"] = proyectos[i]["codigo"]
            estructura[j]["costo"] = proyectos[i]["costo"]
            j += 1
    return j


def mostrar_estructura_de_proyecto(estructura, d):
    for i in range(d):
        print(estructura[i]["codigo"], end="    ")
        print("$", estructura[i]["costo"])
    return None


# Nombre del Módulo: obtener_datos_tipo_proyecto
# Descripción: determina la cantidad y el costo de todos los proyectos para un determinado tipo de proyecto
# y su denominación. En caso de que el código no exista, se deberá retornar cantidad cero, costo cero y
# denominación vacía (“”)
# Datos de Entrada: mis_proyectos y su dimensión (en su interior solicita el tipo de proyecto por referencia)
# Datos de Salida: CantidadProyectos, CostoTodosProyectos, DenominacionTipoDeProyecto
def obtener_datos_tipo_proyecto(proyectos, d):
    tipo = input("Ingrese un tipo de proyecto ('D': Departamento, 'C': Casa, 'E': Edificio): ")
    existe = False
    tipo_proyecto = ""
    denominacion = ""
    cant = 0
    precio = 0
    for i in range(d):
        if proyectos[i]["tipo"] == tipo:
            existe = True
            tipo_proyecto = proyectos[i]["tipo"]
            denominacion = convertir_u1_a_string(proyectos[i]["tipo"])
            cant += 1
            precio += proyectos[i]["costo"]
    if existe:
        print("Tipo de proyecto:", tipo_proyecto, "Denominación:",
              denominacion)
        print("Cantidad de proyectos:", cant, "Costo de los proyectos:$", precio)
    else:
        print("No hay obras para el tipo de proyecto solicitado")
        return cant, precio, denominacion


# Nombre del Módulo: FechaFinalizacion
# Descripción: determina el mes y el anio de finalizacion de un proyecto
# Datos de Entrada: fechaInicio, duracionProyecto
# Datos de Salida: fechaFin
def fecha_finalizacion(fecha_inicio, duracion_proyecto):
    fecha_fin = np.empty(1, dtype=tfecha)
    anios_proyecto = duracion_proyecto / 12
    resto_meses_proyecto = duracion_proyecto % 12
    anio_finalizacion = fecha_inicio['año'] + anios_proyecto
    mes_finalizacion = fecha_inicio['mes'] + resto_meses_proyecto
    if mes_finalizacion > 12:
        mes_finalizacion = mes_finalizacion - 12
        anio_finalizacion = anio_finalizacion + 1

    fecha_fin['mes'] = mes_finalizacion
    fecha_fin['año'] = anio_finalizacion
    return fecha_fin


# Nombre del Módulo: fecha_finalizacion
# Descripción: determina el mes y el anio de finalizacion de un proyecto
# Datos de Entrada: fechaInicio, duracionProyecto
# Datos de Salida: fechaFin
def proyectos_sin_finalizar(proyectos, d):
    cant = 0
    f_finalizacion = 0
    for i in range(d):
        if proyectos[i]["estado"] == 0:
            f_finalizacion = fecha_finalizacion(proyectos[i]["fecha_inicio"], proyectos[i]["duracion"])
            print(proyectos[i]["codigo"], end="   ")
            print(str(proyectos[i]["fecha_inicio"]["mes"]) + "/" + str(proyectos[i]["fecha_inicio"]["año"]), end="   ")
            print(f_finalizacion)
            print("Meses para terminar: ", f_finalizacion - proyectos[i]["fecha_inicio"])
            cant += 1
    print("Total de Proyectos Sin Terminar: ", cant)
    return f_finalizacion


# -----__________ Programa principal __________-----
# Estructura del registro


tfecha = np.dtype(
    [
        ("mes", int),
        ("año", int)
    ]
)

tdatos_constructora = np.dtype(
    [
        ("codigo", int),
        ("nombre_cliente", "U20"),
        ("tipo", "U1"),
        ("duracion", int),
        ("fecha_inicio", tfecha),
        ("costo", float),
        ("estado", int)
    ]
)

# Arreglo de registros
max_proyectos = 20
dim = 0
mis_proyectos = np.empty(max_proyectos, dtype=tdatos_constructora)
mi_estructura = np.empty(max_proyectos, dtype=tdatos_constructora)
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("¡Programa finalizado!")
        salir = True
    elif opc == 1:
        dim = cargar_proyectos(mis_proyectos)
    elif opc == 2:
        mostrar_proyectos(mis_proyectos, dim)
    elif opc == 3:
        dim_estructura = generar_proyectos_de_tipo(mis_proyectos, dim, mi_estructura)
        mostrar_estructura_de_proyecto(mi_estructura, dim_estructura)
    elif opc == 4:
        print(obtener_datos_tipo_proyecto(mis_proyectos, dim))
    elif opc == 5:
        proyectos_sin_finalizar(mis_proyectos, dim)
