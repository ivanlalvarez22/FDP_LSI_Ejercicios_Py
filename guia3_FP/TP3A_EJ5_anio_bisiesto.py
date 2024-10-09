#  Determinar si una fecha es válida (DD,MM, AAAA).
#  Múltiplo de 4?	¿Múltiplo de 100?	¿Múltiplo de 400?	Es bisiesto	Ejemplos
# 	    No				    No				    No				No		2019, 1981
# 	    Sí				    No				    No				Sí		2020, 2012
# 	    Sí				    Sí				    No				No		1900, 2100
# 	    Sí				    Sí				    Sí				Sí		2000, 2400

def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Validar fecha")
    print("Ingrese el '0' para finalizar.")


def validar_fecha(dia, mes, anio):
    validez = False
    if anio >= 1000:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if 1 <= dia <= 30:
                validez = True
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if 1 <= dia <= 31:
                validez = True
        elif mes == 2:
            if anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0:
                if 1 <= dia <= 28:
                    validez = True
            elif anio % 4 == 0:
                if 1 <= dia <= 29:
                    validez = True
            elif 1 <= dia <= 28:
                validez = True
    return validez


# Programa principal
salir = False
while not salir:
    mostrar_menu()
    opc = int(input("Por favor seleccione una opción para continuar: "))
    if opc == 0:
        salir = True
    elif opc == 1:
        dd = int(input("Ingrese el día: "))
        mm = int(input("Ingrese el mes: "))
        aaaa = int(input("Ingrese el año: "))
        if validar_fecha(dd, mm, aaaa):
            print("Fecha válida")
        else:
            print("Fecha inválida")
