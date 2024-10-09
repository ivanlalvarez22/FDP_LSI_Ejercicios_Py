# A partir de 3 números determine el mayor y el menor.

# Definición de módulos


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Ingresar números")
    print("2) Mostrar mayor")
    print("3) Mostrar menor")
    print("Ingrese el '0' para finalizar.")


def verificar_mayor(n1, n2, n3):
    # Verificando mayor
    if n1 >= n2 and n1 >= n3:
        mayor = n1
    elif n2 >= n1 and n2 >= n3:
        mayor = n2
    else:
        mayor = n3
    print(f"El mayor número ingresado es el: {mayor}")
    return None


def verificar_menor(n1, n2, n3):
    # Verificando menor
    if n1 <= n2 and n1 <= n3:
        menor = n1
    elif n2 <= n1 and n2 <= n3:
        menor = n2
    else:
        menor = n3
    print(f"El menor número ingresado es el: {menor}")
    return None


# Programa principal

salir = False
bandera = False
num1 = ""
num2 = ""
num3 = ""

while not salir:
    mostrar_menu()
    opc = int(input("Por favor ingrese una opción para continuar: "))
    if opc == 0:
        salir = True
    elif opc == 1:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        num3 = int(input("Ingrese el tercer número: "))
        bandera = True
        print("Números cargados exitosamente")
    elif opc == 2:
        if bandera:
            verificar_mayor(num1, num2, num3)
        else:
            print("Sugerencia: seleccionar la opción 1")
    elif opc == 3:
        if bandera:
            verificar_menor(num1, num2, num3)
        else:
            print("Sugerencia: ingrese la opción 1")
    else:
        print("Opción inválida")
