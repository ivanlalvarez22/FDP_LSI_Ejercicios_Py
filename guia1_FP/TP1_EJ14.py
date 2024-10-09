# La liga local de hándbol tiene 8 equipos (identificados de 1 a 8). Cada equipo de la liga tiene
# 7 jugadores. Por cada jugador se ingresan los siguientes datos: identificación de equipo, nombre, altura
# y edad de los jugadores. Se pide:
# *** Calcular y mostrar el equipo con el mayor promedio de edad.
# *** Determinar y mostrar la cantidad de jugadores que se encuentran en los equipos 6 y 4,
# que tengan una altura mayor a 1,70m y menor igual a 1.80m
# Datos de entrada: datos del jugador: equipo, nombre, altura, edad
# Datos de salida: mostrar el promedio de edad, cantidad de jugadores en los equipos 6 y 4 que
# tengan altura mayor a 1.70m y menor a 1.80m

equipo = 1
bandera = 0
cant_jug_alt4 = 0
cant_jug_alt6 = 0
mayor = 0
mayor_prom = 0

while equipo <= 3:
    cant_jug = 0
    sum_edad = 0
    prom_edad = 0

    id_equipo = int(input("Ingresar el equipo (1 - 8): "))
    while cant_jug < 2:
        nombre = str(input("Ingresar el nombre del jugador: "))
        altura = float(input("Ingresar la altura: "))
        edad = int(input("Ingresar la edad: "))
        sum_edad += edad

        if id_equipo == 4 and 170 < altura <= 180:
            cant_jug_alt4 += 1
        if id_equipo == 6 and 170 < altura <= 180:
            cant_jug_alt6 += 1
        cant_jug += 1

    if cant_jug > 0:
        prom_edad = sum_edad / cant_jug

    if bandera == 0:
        mayor = prom_edad
        mayor_prom = id_equipo
        bandera = 1
    elif prom_edad > mayor:
        mayor = prom_edad
        mayor_prom = id_equipo

    equipo += 1

print("El equipo con el mayor promedio de edad es el equipo: ", mayor_prom)
print("El promedio de edad del mismo es: ", mayor)
print("La cantidad de jugadores del E4 con altura mayor a 170 y menor o igual a 180 son: ", cant_jug_alt4)
print("La cantidad de jugadores del E6 con altura mayor a 170 y menor o igual a 180 son: ", cant_jug_alt6)
