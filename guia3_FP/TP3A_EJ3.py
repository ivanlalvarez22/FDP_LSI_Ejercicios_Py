# Mostrar el factorial de un número.

# Definición de módulos
def calcular_factorial(num):
    factorial = 1
    if num == 0:
        factorial = 0
    for i in range(1, num + 1, 1):
        factorial = factorial * i
    return factorial


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Calcular factorial")
    print("Ingrese el '0' para finalizar.")


# Programa principal

salir = False
bandera = False
while not salir:
    mostrar_menu()
    opc = int(input("Por favor ingrese una opción: "))
    n = -1
    if opc == 1:
        while not n >= 0:
            n = int(input("Ingrese un número para calcular su factorial: "))
        print(f"el factorial de {n} es: ", calcular_factorial(n))
    elif opc == 0:
        salir = True
