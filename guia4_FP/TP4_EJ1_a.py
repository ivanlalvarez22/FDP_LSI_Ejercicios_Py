# Un negocio desea guardar la siguiente información de sus 10 empleados:
# DNI, Nombre, Edad y Sexo {‘M ‘o ‘F’}.
# Se pide hacer un algoritmo que permita en primer término realizar el proceso de carga de la estructura.
# Luego deberá mostrar el Nombre del empleado de mayor edad de sexo masculino.

import numpy as np

# Definición de módulos


def mostrar_menu():
    print("------MENÚ PRINCIPAL------\n"
          "1) Cargar registro (estático)\n"
          "2) Cargar registro (dinámico)\n"
          "3) Mostrar registro\n"
          "4) Mostrar empleado masculino de mayor edad\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Ingrese una opción para continuar: "))
    return op


def cargar_registro_estatico(me):
    me[0] = (12345678, "Juan Perez", 77, "M")
    me[1] = (38484357, "Iván Alvarez", 27, "M")
    me[2] = (25836914, "Sabrina Basualdo", 20, "F")
    print("...Registro cargado correctamente...")
    return None


def cargar_registro_dinamico(me, d):
    for i in range(d):
        me[i]["dni"] = int(input("Ingrese el dni: "))
        me[i]["nombre"] = input("Ingrese el nombre: ")
        me[i]["edad"] = int(input("Ingrese la edad: "))
        me[i]["sexo"] = input("Ingrese el sexo: ")
    print("Registro cargado exitosamente")
    return None


def mostrar_registro(me, d):
    print("DNI          Nombre                     Edad            Sexo")
    for i in range(d):
        print(me[i]["dni"], end="     ")
        print(str(me[i]["nombre"]).ljust(20), end="        ")
        print(me[i]["edad"], end="              ")
        print(me[i]["sexo"])
    return None


def mostrar_empleado_masc_may_edad(me, d):
    nombre = ""
    mayor = 0
    for i in range(d):
        if me[i]["sexo"] == "M" and me[i]["edad"] >= mayor:
            mayor = me[i]["edad"]
            nombre = me[i]["nombre"]
    print(f"El empleado de masculino de mayor edad es {nombre}\n"
          f"con {mayor} años de edad")


# Programa principal
# Estructura del registro

Tdatos_empleados = np.dtype(
    [
        ("dni", int),
        ("nombre", "U50"),
        ("edad", int),
        ("sexo", "U1")
    ]
)

# Arreglo de registros
N = 3
mis_empleados = np.empty(N, Tdatos_empleados)

salir = False
bandera = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado")
        salir = True
    elif opc == 1:
        cargar_registro_estatico(mis_empleados)
        bandera = True
    elif opc == 2:
        cargar_registro_dinamico(mis_empleados, N)
        bandera = True
    elif opc == 3:
        if bandera:
            mostrar_registro(mis_empleados, N)
        else:
            print("Debe ingresar a la opción 1 o 2 primero")
    elif opc == 4:
        if bandera:
            mostrar_empleado_masc_may_edad(mis_empleados, N)
        else:
            print("Ingrese a la opción 1 o 2")
