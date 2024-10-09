import numpy as np

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

# Carga estática del registro
mis_empleados[0] = (12345678, "Juan Perez", 45)
mis_empleados[1] = (14725836, "Julian Alvarez", 21)
mis_empleados[2] = (78945612, "Leonardo Ponzio", 45)

# Mostrar arreglo de registros
print("DNI          Nombre          Edad")
for i in range(N):
    print(mis_empleados[i]["dni"], end="   ")
    print(mis_empleados[i]["nombre"], end="      ")
    print(mis_empleados[i]["edad"])

# Carga dinámica del registro
for i in range(N):
    mis_empleados[i]["dni"] = int(input("Ingrese el dni: "))
    mis_empleados[i]["nombre"] = input("Ingrese el nombre: ")
    mis_empleados[i]["edad"] = int(input("Ingrese la edad: "))

# Mostrar el arreglo de registros
print("DNI          Nombre          Edad")
for i in range(N):
    print(mis_empleados[i]["dni"], end="   ")
    print(mis_empleados[i]["nombre"], end="      ")
    print(mis_empleados[i]["edad"])
