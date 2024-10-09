# El Departamento Personal de la UNSE registra para sus profesores los siguientes datos:
# Número de Legajo, Documento, Apellido y Nombre, Fecha de Nacimiento, Sexo {‘M’,’F’}, Código de Facultad,
# Fecha de Ingreso y Estado {1-Activo, 2-Pasivo, 3-En Edad de Jubilarse}.
# Mostrar:

# a) Número de Legajo y Apellido y Nombre de aquellos empleados de la universidad de sexo femenino y que se
# encuentran activos.

# b) Número de Legajo de todos los empleados con una antigüedad igual a 25 años.

# c) Actualizar el registro del Departamento Personal, con aquellos profesores que se encuentren en edad de jubilarse,
# para lo cual deberá tener en cuenta que las mujeres se jubilan con 60 años de edad, y los hombres con 65 años.

import numpy as np

# Definición de módulos


# Nombre del módulo: mostrar_menu
# Descripción: Muestra un menú interactivo con el usuario
# Datos de Entrada:
# Datos de Salida: retorna el número de opción seleccionado por el usuario
def mostrar_menu():
    print("------------------------ MENÚ PRINCIPAL --------------------------------\n"
          "1) Cargar registro\n"
          "2) Mostrar registro\n"
          "3) Mostrar datos de empleados de sexo femenino que se encuentran activos\n"
          "4) Mostrar legajos de los empleados con antiguedad mayor o igual a 25 años\n"
          "5) Actualizar registro para empleados en edad de jubilarse\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


# Nombre del módulo: cargar_registro
# Descripción: realiza la carga de datos de cada empleado del departamento personal de la UNSE
# Datos de Entrada: el arreglo de registros "mis_empleados"
# Datos de Salida:
def cargar_registro(me):
    me[0] = (458, 38484357, "Alvarez", "Iván", (22, 9, 1994), "M", 2202, (25, 2, 2014), 1)
    me[1] = (159, 24785654, "Bottoni", "Julieta", (2, 5, 1973), "F", 1244, (17, 3, 2008), 1)
    me[2] = (321, 14785632, "Alvarez", "Sergio", (7, 8, 1969), "M", 7707, (21, 7, 2004), 1)
    me[3] = (140, 13154789, "Basualdo", "Sabrina", (2, 12, 2000), "F", 1477, (15, 9, 2018), 1)
    me[4] = (658, 45781235, "Newton", "Isaac", (4, 1, 1955), "M", 4632, (22, 5, 1990), 1)
    me[5] = (571, 94872123, "Perlman", "Radia", (18, 12, 1951), "F", 1114, (27, 11, 1975), 1)
    me[6] = (747, 15647892, "Hawking", "Stephen", (8, 1, 1942), "M", 3164, (11, 11, 1972), 2)
    me[7] = (279, 45781245, "Tesla", "Nikola", (10, 7, 1956), "M", 8825, (12, 2, 1977), 3)
    me[8] = (227, 25478654, "Thompson", "Emma", (15, 4, 1959), "F", 6589, (20, 7, 1986), 3)
    me[9] = (568, 11356897, "Figueroa", "Lucinda", (12, 2, 1944), "F", 9863, (30, 5, 1977), 2)
    print("\nRegistro cargado correctamente\n")
    return None


# Nombre del módulo: convertir_estado
# Descripción: convierte un estado de tipo entero a tipo caracter
# Datos de Entrada: estado de tipo entero
# Datos de Salida: estado de tipo caracter
def convertir_estado(estado):
    if estado == 1:
        estado = "Activo"
    elif estado == 2:
        estado = "Pasivo"
    else:
        estado = "En edad de jubilarse"
    return estado


# Nombre del módulo: mostrar_registro
# Descripción: muestra el registro cargado previamente de manera estática o dinámica
# Datos de Entrada: arreglo de registros "mis_empleados" y su dimensión
# Datos de Salida:
def mostrar_registro(me, d):
    print("LEGAJO   DNI        APELLIDO     NOMBRE     NACIMIENTO   SEXO   COD. FACULTAD   FECHA INGRESO   ESTADO")
    for i in range(d):
        fecha_nac = (str(me[i]["fecha_nac"]["dia"]) + "/" + str(me[i]["fecha_nac"]["mes"]) + "/" +
                     str(me[i]["fecha_nac"]["anio"]))
        fecha_ing = (str(me[i]["fecha_ingreso"]["dia"]) + "/" + str(me[i]["fecha_ingreso"]["mes"]) + "/" +
                     str(me[i]["fecha_ingreso"]["anio"]))
        print(me[i]["legajo"], end="      ")
        print(me[i]["documento"], end="   ")
        print(str(me[i]["apellido"]).ljust(10), end="   ")
        print(str(me[i]["nombre"]).ljust(10), end=" ")
        print(str(fecha_nac).ljust(10), end="    ")
        print(me[i]["sexo"], end="     ")
        print(me[i]["cod_facultad"], end="            ")
        print(str(fecha_ing).ljust(10), end="      ")
        print(convertir_estado(me[i]["estado"]))
    print("-"*120)
    return None


# Nombre del módulo: realizar_act_a
# Descripción: muestra el número de Legajo y apellido y nombre de aquellos empleados de la universidad de sexo
# femenino y que se encuentran activos.
# Datos de Entrada: arreglo de registros "mis_empleados" y su dimension
# Datos de Salida:
def realizar_act_a(me, d):
    print("LEGAJO    APELLIDO    NOMBRE")
    for i in range(d):
        if me[i]["sexo"] == "F" and me[i]["estado"] == 1:
            print(str(me[i]["legajo"]) + "      ", str(me[i]["apellido"]).ljust(10) + " ",
                  str(me[i]["nombre"]).ljust(10) + "   ")
    print("-"*50)
    return None


# Nombre del módulo: realizar_act_b
# Descripción: nos muestra el nro de legajo de empleados con antiguedad mayor o igual a 25 años con estado activo o
# en edad de jubilarse
# Datos de Entrada: arreglo de registros "mis_empleados" y su dimensión
# Datos de Salida:
def realizar_act_b(me, d):
    for i in range(d):
        if calcular_antiguedad(me[i]["fecha_ingreso"]["anio"]) >= 25 and (me[i]["estado"] == 1 or me[i]["estado"] == 3):
            print(me[i]["legajo"], me[i]["nombre"])
    return None


# Nombre del módulo: calcular_antiguedad
# Descripción: nos muestra la antiguedad de años trabajados de los empleados
# Datos de Entrada: el año de ingreso al puesto
# Datos de Salida: la cantidad de años de antiguedad en el puesto
def calcular_antiguedad(anio):
    antiguedad = 2021 - anio
    return antiguedad


# Nombre del módulo: calcular_edad
# Descripción: calcula la edad según el año de nacimineto ingresado
# Datos de Entrada: año de nacimiento
# Datos de Salida: la edad actual
def calcular_edad(anio_nacimiento):
    edad = 2021 - anio_nacimiento
    return edad


# Nombre del módulo: realizar_act_c
# Descripción: actualiza el registro cambiando el estado para los empleados en edad de jubilarse
# Datos de Entrada: el arreglo de registros "mis_empleados" y su dimensión
# Datos de Salida:
def realizar_act_c(me, d):
    for i in range(d):
        if me[i]["sexo"] == "F" and calcular_antiguedad(me[i]["fecha_nac"]["anio"]) >= 60:
            me[i]["estado"] = 3
        elif me[i]["sexo"] == "M" and calcular_antiguedad(me[i]["fecha_nac"]["anio"]) >= 65:
            me[i]["estado"] = 3
    print("\n¡El registro se actualizó con éxito!\n"
          "Seleccione la opción 2) para mostrar el registro actualizado\n")
    return None


# Programa principal
# Estructura del registro

Tfecha = np.dtype(
    [
        ("dia", int),
        ("mes", int),
        ("anio", int)
    ]
)

Tdatos_empleados = np.dtype(
    [
        ("legajo", int),
        ("documento", int),
        ("apellido", "U50"),
        ("nombre", "U50"),
        ("fecha_nac", Tfecha),
        ("sexo", "U1"),
        ("cod_facultad", int),
        ("fecha_ingreso", Tfecha),
        ("estado", int)
    ]
)

# Arreglo de registros
N = 10
mis_empleados = np.empty(N, Tdatos_empleados)
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado")
        salir = True
    elif opc == 1:
        cargar_registro(mis_empleados)
    elif opc == 2:
        mostrar_registro(mis_empleados, N)
    elif opc == 3:
        realizar_act_a(mis_empleados, N)
    elif opc == 4:
        realizar_act_b(mis_empleados, N)
    elif opc == 5:
        realizar_act_c(mis_empleados, N)
