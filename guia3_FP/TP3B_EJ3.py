# Dado un número X de 3 cifras determine la cantidad de dígitos pares y la cantidad de
# dígitos impares. Ejemplo: Si el número de tres cifras es 364, la cantidad de
# pares es 2 y la cantidad de impareses 1.

# Definición de módulos


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Ingresar número")
    print("2) Mostrar cantidad de dígitos pares")
    print("3) Mostrar cantidad de dígitos impares")
    print("4) Ingrese el '0' para finalizar.")


def mostrar_cant_pares(n):
    cant_pares = 0
    centena = n // 100
    decena = (n // 10) % 10
    unidad = n % 10
    if centena % 2 == 0:
        cant_pares += 1
    if decena % 2 == 0:
        cant_pares += 1
    if unidad % 2 == 0:
        cant_pares += 1
    print(f"La cantidad de dígitos pares son: {cant_pares}")
    return None


def mostrar_cant_impares(n):
    cant_impares = 0
    centena = n // 100
    decena = (n // 10) % 10
    unidad = n % 10
    if centena % 2 != 0:
        cant_impares += 1
    if decena % 2 != 0:
        cant_impares += 1
    if unidad % 2 != 0:
        cant_impares += 1
    print(f"La cantidad de dígitos impares son: {cant_impares}")
    return None


# Programa principal
salir = False
bandera = False
num = ""
while not salir:
    mostrar_menu()
    opc = int(input("Por favor ingrese una opción para continuar: "))
    if opc == 0:
        salir = True
    elif opc == 1:
        num = 0
        while not 99 < num < 1000:
            num = int(input("Ingrese un número de 3 cifras: "))
        bandera = True
        print("Número correctamente cargado..")
    elif opc == 2:
        if bandera:
            mostrar_cant_pares(num)
        else:
            print("Debe seleccionar la opción 1")
    elif opc == 3:
        if bandera:
            mostrar_cant_impares(num)
        else:
            print("Seleccione la opción 1")
    else:
        print("Opción inválida!!")
