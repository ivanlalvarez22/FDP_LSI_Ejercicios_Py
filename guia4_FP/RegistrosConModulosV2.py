import numpy as np


def cargar_empleados_estatica(me):
    me[0] = (12345678, "Juan Perez", 45)
    me[1] = (14725836, "Julian Alvarez", 22)
    me[2] = (14578236, "Leonardo Ponzio", 39)


def mostrar_registro(me, d):
    print("DNI          Nombre          Edad")
    for i in range(d):
        print(me[i]["dni"], end="  ")
        print(me[i]["nombre"], end="    ")
        print(me[i]["edad"])


def cargar_empleados_dinamica(me, d):
    for i in range(d):
        me[i]["dni"] = int(input("Ingrese el dni: "))
        me[i]["nombre"] = input("Ingrese el nombre: ")
        me[i]["edad"] = int(input("Ingrese la edad: "))


# Estructura del registro
datos_personas = np.dtype(
    [
        ("dni", int),
        ("nombre", "U50"),
        ("edad", int)
    ]
)

# Arreglo de registros
N = 3
mis_empleados = np.empty(N, dtype=datos_personas)

cargar_empleados_estatica(mis_empleados)
mostrar_registro(mis_empleados, N)
cargar_empleados_dinamica(mis_empleados, N)
mostrar_registro(mis_empleados, N)
