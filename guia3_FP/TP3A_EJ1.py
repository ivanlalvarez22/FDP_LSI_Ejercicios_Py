# Convertir un número expresado en horas a minutos.

# Definición de módulos

def ingresar_horas(horas):
    return horas


def convertir_horas(horas):
    minutos = horas * 60
    return minutos


def mostrar_menu():
    print(" ------ MENÚ PRINCIPAL ------")
    print("1) Ingresar cantidad de horas")
    print("2) Convertir horas a minutos")
    print("Ingrese el '0' para finalizar")


# Programa principal
salir = False
b = False
h = -1  # condición para que entre en el ciclo (lin 26)
while not salir:
    mostrar_menu()
    opc = int(input("Ingrese una opción: "))
    if opc == 1:
        while not h >= 0:
            h = int(input("Ingrese la cantidad de horas: "))
            ingresar_horas(h)
        print("Hora ingresada correctamente", h)
        b = True
    elif opc == 2 and b:
        print(h, "horas equivalen a:", convertir_horas(h), "minutos")
    elif opc == 0:
        salir = True
    elif not b:
        print("Debería ingresar una hora primero!")
