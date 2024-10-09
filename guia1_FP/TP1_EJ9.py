# La hija de la profe Bea se niega a decir las vocales débiles (I, U),
# entonces ella decidió hacer silencio hasta que ella diga alguna de las 2 vocales.
# Datos de entrada: vocales
# Datos de salida: La hija de la profe Bea dijo una vocal débil

bandera = False

while not bandera:
    vocal = str(input("Ingrese una vocal: "))
    if vocal.upper() == "I" or vocal.upper() == "U":
        bandera = True
        print("Usted ingresó una vocal débil")
    elif vocal.upper() == "A" or vocal.upper() == "E" or vocal.upper() == "O":
        print("No se ingresó vocal débil")
