# Dado los lados de un triángulo, determinar el tipo de triángulo (equilátero, isósceles,escaleno).

# Definición de módulos

def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Determinar tipo de triángulo")
    print("Ingrese el '0' para finalizar.")


def determinar_tipo(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3:
        triangulo = "equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        triangulo = "isósceles"
    else:
        triangulo = "escaleno"
    return triangulo


# Programa principal
salir = False
while not salir:
    mostrar_menu()
    a = -1
    b = -1
    c = -1
    opc = int(input("Por favor seleccione una opción: "))
    if opc == 0:
        salir = True
    elif opc == 1:
        while not a > 0:
            a = int(input("Ingrese la longitud del lado1: "))
        while not b > 0:
            b = int(input("Ingrese la longitud del lado2: "))
        while not c > 0:
            c = int(input("Ingrese la longitud del lado3: "))
        print("Lados correctamente ingresados")
        print(f"El triángulo es de tipo: {determinar_tipo(a, b, c)}")
