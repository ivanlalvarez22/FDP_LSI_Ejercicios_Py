import numpy as np

# Definición de módulos


def carga_estatica(me):
    me[0] = (12345678, "Juan Perez", 45)
    me[1] = (14725836, "Pedro Simon", 50)
    me[2] = (78945612, "Sergio Alvarez", 52)
    return None


def carga_dinamica(me, d):
    for i in range(d):
        me[i]["dni"] = int(input("Ingrese el dni: "))
        me[i]["nombre"] = input("Ingrese el nombre: ")
        me[i]["edad"] = int(input("Ingrese la edad: "))


def mostrar_empleados(me, d):
    print("DNI          Nombre          Edad")
    for i in range(d):
        print(me[i]["dni"], end="    ")
        print(me[i]["nombre"], end="       ")
        print(me[i]["edad"])


# Programa principal

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

carga_estatica(mis_empleados)
mostrar_empleados(mis_empleados, N)
carga_dinamica(mis_empleados, N)
mostrar_empleados(mis_empleados, N)
