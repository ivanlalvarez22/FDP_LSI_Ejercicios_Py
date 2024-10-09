# Un negocio desea guardar la siguiente información de sus 10 empleados:
# DNI, Nombre, Edad y Sexo {‘M ‘o ‘F’}.
# Se pide hacer un algoritmo que permita en primer término realizar el proceso de carga de la estructura.
# Luego deberá mostrar el Nombre del empleado de mayor edad de sexo masculino.
import numpy as np

"""
Definición de módulos
"""


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Cargar registro (estático)")
    print("2) Cargar registro (manual)")
    print("3) Mostrar registro")
    print("4) Mostrar empleado de mayor edad de sexo masculino")
    print("--------------------------------------------------------")
    return None


def cargar_registro_estatico(me):
    me[0] = (12345678, "Juan Perez".ljust(15), 44, "M")
    me[1] = (14725836, "Manu Ginobili".ljust(15), 42, "M")
    me[2] = (45954786, "Sabrina Basualdo".ljust(15), 2, "F")
    print("Registro cargado")
    return None


def cargar_registro_manual(me, d):
    for i in range(d):
        me[i]["dni"] = int(input("Ingrese el dni: "))
        me[i]["nombre"] = input("Ingrese el nombre: ")
        me[i]["edad"] = int(input("Ingrese la edad: "))
        me[i]["sexo"] = input("Ingrese el sexo: ").upper()
    return None


def mostrar_registro(me, d):
    print("DNI           Nombre               Edad      Sexo")
    for i in range(d):
        print(me[i]["dni"], end="      ")
        print(me[i]["nombre"], end="       ")
        print(me[i]["edad"], end="        ")
        print(me[i]["sexo"])
    return None


def mostrar_may_edad_masculino(me, d):
    mayor = 0
    nombre = ""
    for i in range(d):
        if me[i]["sexo"] == "M" and me[i]["edad"] > mayor:
            mayor = me[i]["edad"]
            nombre = me[i]["nombre"]
    print(f"El empleado de mayor edad es {nombre}\n"
          f" con {mayor} años de edad")


# Programa principal
# Estructura del registro

datos_empleados = np.dtype(
    [
        ("dni", int),
        ("nombre", "U50"),
        ("edad", int),
        ("sexo", "U1")
    ]
)

# Arreglo de registros
N = 3  # Modifique éste valor para aumentar la cantidad de empleados
mis_empleados = np.empty(N, dtype=datos_empleados)

salir = False
bandera = False
while not salir:
    mostrar_menu()
    opc = int(input("Ingrese una opción para continuar: "))
    if opc == 1:
        cargar_registro_estatico(mis_empleados)
        bandera = True
    elif opc == 2:
        cargar_registro_manual(mis_empleados, N)
        bandera = True
    elif opc == 3 and bandera:
        mostrar_registro(mis_empleados, N)
    elif opc == 4:
        if bandera:
            mostrar_may_edad_masculino(mis_empleados, N)
        else:
            print("Ingrese la opción 1 o 2")
    elif opc == 0:
        print("Programa finalizado")
        salir = True
    else:
        print("Opción incorrecta")
