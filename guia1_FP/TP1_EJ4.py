# Pedro tiene poca memoria y la regla de los nudillos no le funciona para saber cuántos días tiene un mes,
# entonces, ¿Cómo puede hacer para saber cuántos días tiene cada mes? ¿Aparte del mes, importa el año?
# Ingresar un mes, ver si estamos en año bisiesto
# Mostrar la cantidad de días de cada mes
# Si estamos en año bisiesto febrero tendrá 29 días

anio = int(input("Escribir el año actual: "))
bisiesto = anio % 4
if bisiesto == 0:
    print("enero: 31 días")
    print("febrero: 29 días")
    print("marzo: 31 días")
    print("abril: 30 días")
    print("mayo: 31 días")
    print("junio: 30 días")
    print("julio: 31 días")
    print("agosto: 31 días")
    print("septiembre: 30 días")
    print("octubre: 31 días")
    print("noviembre: 30 días")
    print("diciembre: 31 días")
else:
    print("enero: 31 días")
    print("febrero: 28 días")
    print("marzo: 31 días")
    print("abril: 30 días")
    print("mayo: 31 días")
    print("junio: 30 días")
    print("julio: 31 días")
    print("agosto: 31 días")
    print("septiembre: 30 días")
    print("octubre: 31 días")
    print("noviembre: 30 días")
    print("diciembre: 31 días")
