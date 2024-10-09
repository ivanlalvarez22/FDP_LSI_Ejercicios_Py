# En un Rapipago hay una cola de N personas con varias boletas de impuestos para pagar;
# mostrar el total que debe abonar cada persona.
# Datos de entrada: La cantidad de personas, la cantidad de boletas a pagar
# Datos de salida: Mostrar por cada persona el total que debe abonar de todas las boletas
# Estrategia de resolución: Estructura de datos iterativa dentro de otra estructura iterativa
# una estructura para cada persona y otra para la cantidad de boletas.

c = 0
N = int(input("Ingrese la cantidad de personas: "))

while c < N:
    boletas = 0
    monto = 0
    suma = 0

    cant_boletas = int(input("Ingrese la cantidad de boletas a pagar: "))

    while boletas < cant_boletas:
        print(f"Ingrese el monto de la {boletas + 1} boleta: ")
        monto = float(input())
        suma += monto
        boletas += 1

    print("La cantidad total que debe abonar es: $%.2f" % suma)
    c += 1
