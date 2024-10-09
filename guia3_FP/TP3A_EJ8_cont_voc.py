# Para una cadena de caracteres determinar y mostrar la cantidad de vocales que tiene la cadena.

# Definición de módulos

def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Ingresar cadena de caracteres")
    print("2) Mostrar vocales")
    print("Ingrese el '0' para finalizar.")


def ingresar_cadena():
    cad = str(input("Ingrese una letra, palabra o frase: "))
    print("Cadena cargada correctamente")
    return cad


def contar_vocales(cad):
    dim = len(cad)  # Muestra la cantidad de caracteres en una frase
    cant_voc = 0
    for i in range(dim):
        if cad[i].lower() in "aeiou":
            cant_voc = cant_voc + 1
    print("La cantidad de vocales es: ", cant_voc)


# Programa principal
salir = False
bandera = False
cadena = ""
while not salir:
    mostrar_menu()
    opc = int(input("Por favor ingrese una opción para continuar: "))
    if opc == 0:
        salir = True
    elif opc == 1:
        cadena = ingresar_cadena()
        bandera = True
    elif opc == 2:
        if bandera:
            contar_vocales(cadena)
        else:
            print("Primero debe ingresar una letra, palabra o frase")
    else:
        print("Opción inválida")
