# A partir de 3 números muestre el mayor y el menor.

# Definición de módulos


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Ingresar 3 números")
    print("2) Mostrar mayor")
    print("3) Mostrar menor")
    print("Ingrese el '0' para finalizar.")


def mostrar_mayor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        print(f"El mayor es: {n1}")
    elif n2 >= n1 and n2 >= n3:
        print(f"El mayor es: {n2}")
    else:
        print(f"El mayor es: {n3}")


def mostrar_menor(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        print(f"El menor es: {n1}")
    elif n2 <= n1 and n2 <= n3:
        print(f"El menor es: {n2}")
    else:
        print(f"El menor es: {n3}")


# Programa principal

salir = False
bandera = False
num1 = ""
num2 = ""
num3 = ""
while not salir:
    mostrar_menu()
    opc = int(input("Por favor seleccione una opción para continuar: "))
    if opc == 0:
        salir = True
    elif opc == 1:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        num3 = int(input("Ingrese el tercer número: "))
        bandera = True
        print("Números cargados exitosamente...")
    elif opc == 2:
        if bandera:
            mostrar_mayor(num1, num2, num3)
        else:
            print("Seleccione la opción 1")
    elif opc == 3:
        if bandera:
            mostrar_menor(num1, num2, num3)
        else:
            print("Debe seleccionar la opción 1")
    else:
        print("Opción inválida!!")
