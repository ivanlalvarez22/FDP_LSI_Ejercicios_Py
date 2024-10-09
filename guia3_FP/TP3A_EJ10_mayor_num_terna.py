# Para N ternas de números, mostrar el mayor de cada terna.

# Definición de módulos


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Mostrar el mayor número de una terna")
    print("Ingrese el '0' para finalizar.")


def verificar_mayor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        mayor = n1
    elif n2 >= n1 and n2 >= n3:
        mayor = n2
    else:
        mayor = n3
    return mayor


# Programa principal
salir = False
while not salir:
    mostrar_menu()
    opc = int(input("Por favor ingrese una opción para continuar: "))
    if opc == 0:
        salir = True
    elif opc == 1:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        num3 = int(input("Ingrese el tercer número: "))
        print(f"El mayor número de la terna es el: {verificar_mayor(num1, num2, num3)}")
    else:
        print("Opción inválida")
