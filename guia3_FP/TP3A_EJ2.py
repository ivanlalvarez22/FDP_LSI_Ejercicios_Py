# Calcular el área de un círculo conociendo su perímetro (r = p / 2π) y (a = π*r^2)
# entrada -> perímetro
# proceso:
#         pedimos el ingreso del perímetro
#         calcular el radio:
#                entrada:perimetro
#                salida:radio
#         calcular área
#                entrada:radio
#                salida:area
# salida: área del círculo

# Definición de módulos

import math


def ingresar_perimetro(p):
    r = p / (2 * math.pi)  # El denominador debe ir entre paréntesis para respetar la jerarquía de operaciones
    return r


def calcular_area(r):
    a = math.pi * r ** 2
    return a


def print_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Ingresar perímetro")
    print("2) Determinar área")
    print("Ingrese el '0' para finalizar.")


# Programa principal
print("La función de éste programa es calcular el área de un círculo conociendo su períemtro")
salir = False
b = False
radio = ""
while not salir:
    print_menu()
    perimetro = -1  # Condición para entrar en el ciclo (lin 43)
    opc = int(input("Por favor ingrese una opción: "))
    if opc == 1:
        while not perimetro >= 0:
            perimetro = int(input("Ingresar el perímetro para calcular el área del círculo: "))
            radio = ingresar_perimetro(perimetro)
        print("perímetro ingresado correctamente")
        b = True
    elif opc == 2 and b:
        print("El área según el perímetro ingresado es: ", calcular_area(radio))
    elif opc == 0:
        salir = True
    elif not b:  # éste mje debe ir después de la opc 0 para no mostrarse en caso de seleccionar esa opc
        print("Debes ingresar el perímetro antes!")
