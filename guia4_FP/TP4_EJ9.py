# Un aeropuerto registra para cada uno de los aviones la siguiente información: Línea Aérea, Número de vuelo,
# Datos del viaje (Ciudad Origen, Hora de Salida, Ciudad Destino, Hora de Llegada) y Cantidad de Pasajeros.
# Se pide:

# a) Mostrar una línea aérea que tenga el mayor número de pasajeros como ciudad destino París.

# b) Generar una estructura que contenga el número de vuelo, datos del viaje y la cantidad de pasajeros de
# todos los aviones que tienen como Ciudad Origen Roma.

import numpy as np

# Definición de módulos


def mostrar_menu():
    print("--------MENÚ PRINCIPAL--------\n"
          "1) Cargar registro\n"
          "2) Mostrar registro\n"
          "3) Realizar ítem a\n"
          "4) Realizar ítem b\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


def cargar_registro(ma):
    ma[0] = ("American Airlines", 111, ("Roma", "8:50", "Milan", "10:15"), 60)
    ma[1] = ("American Airlines", 211, ("Roma", "12:20", "Paris", "13:15"), 25)
    ma[2] = ("American Airlines", 181, ("Roma", "16:50", "Berna", "18:15"), 50)
    ma[3] = ("British Airways", 110, ("Roma", "18:55", "Berlin", "21:15"), 40)
    ma[4] = ("British Airways", 145, ("Paris", "13:20", "Milan", "15:15"), 90)
    ma[5] = ("British Airways", 454, ("Madrid", "11:50", "Londres", "14:15"), 120)
    ma[6] = ("Fly Emirates", 147, ("Zurich", "16:00", "Paris", "18:15"), 135)
    ma[7] = ("Fly Emirates", 114, ("Ginebra", "17:50", "Paris", "20:15"), 45)
    ma[8] = ("Iberia", 845, ("Lucerna", "10:30", "Paris", "12:15"), 54)
    ma[9] = ("Iberia", 212, ("Basilea", "11:00", "Milan", "13:15"), 80)
    print("\nRegistro cargado exitosamente\n")
    return None


def mostrar_registro(ma, d):
    print("LINEA               NRO     CIUDAD ORIGEN     H. SALIDA      CIUDAD DESTINO     H. LLEGADA     "
          " C. PASAJEROS")
    for i in range(d):
        print(str(ma[i]["linea"]).ljust(17), end="   ")
        print(ma[i]["numero"], end="     ")
        print(str(ma[i]["datos_viaje"]["ciudad_origen"]).ljust(8), end="          ")
        print(str(ma[i]["datos_viaje"]["hora_salida"]).ljust(5), end="          ")
        print(str(ma[i]["datos_viaje"]["ciudad_destino"]).ljust(10), end="         ")
        print(str(ma[i]["datos_viaje"]["hora_llegada"]).ljust(5), end="           ")
        print(ma[i]["cant_pasajeros"])
    return None


def realizar_act_a(ma, d):
    mayor = 0
    linea = ""
    for i in range(d):
        if ma[i]["datos_viaje"]["ciudad_destino"] == "Paris" and ma[i]["cant_pasajeros"] > mayor:
            mayor = ma[i]["cant_pasajeros"]
            linea = ma[i]["linea"]
    print(f"La línea con mayor cantidad de pasajeros con destino París es {linea}, con {mayor} cantidad de pasajeros")
    return None


def realizar_act_b(ma, d, pr):
    j = 0
    for i in range(d):
        if ma[i]["datos_viaje"]["ciudad_origen"] == "Roma":
            pr[j]["numero"] = ma[i]["numero"]
            pr[j]["datos_viaje"]["ciudad_origen"] = ma[i]["datos_viaje"]["ciudad_origen"]
            pr[j]["datos_viaje"]["hora_salida"] = ma[i]["datos_viaje"]["hora_salida"]
            pr[j]["datos_viaje"]["ciudad_destino"] = ma[i]["datos_viaje"]["ciudad_destino"]
            pr[j]["datos_viaje"]["hora_llegada"] = ma[i]["datos_viaje"]["hora_llegada"]
            pr[j]["cant_pasajeros"] = ma[i]["cant_pasajeros"]
            j += 1
    return j


def mostrar_estructura(pr, d):
    print("")
    for i in range(d):
        print(pr[i]["numero"], end="   ")
        print(pr[i]["datos_viaje"]["ciudad_origen"], end="   ")
        print(str(pr[i]["datos_viaje"]["hora_salida"]).ljust(5), end="   ")
        print(str(pr[i]["datos_viaje"]["ciudad_destino"]).ljust(10), end="   ")
        print(pr[i]["datos_viaje"]["hora_llegada"], end="   ")
        print(pr[i]["cant_pasajeros"])
    return None


def main():
    # Estructura del registro

    tdatos_viaje = np.dtype(
        [
            ("ciudad_origen", "U30"),
            ("hora_salida", "U6"),
            ("ciudad_destino", "U30"),
            ("hora_llegada", "U6")
        ]
    )

    tdatos_aviones = np.dtype(
        [
            ("linea", "U30"),
            ("numero", int),
            ("datos_viaje", tdatos_viaje),
            ("cant_pasajeros", int)
        ]
    )

    # Arreglo de registros
    n = 10
    mis_aviones = np.empty(n, dtype=tdatos_aviones)
    pasajeros_roma = np.empty(n, dtype=tdatos_aviones)
    salir = False
    while not salir:
        opc = mostrar_menu()
        if opc == 0:
            print("Programa finalizado!")
            salir = True
        elif opc == 1:
            cargar_registro(mis_aviones)
        elif opc == 2:
            mostrar_registro(mis_aviones, n)
        elif opc == 3:
            realizar_act_a(mis_aviones, n)
        elif opc == 4:
            dim_roma = realizar_act_b(mis_aviones, n, pasajeros_roma)
            mostrar_estructura(pasajeros_roma, dim_roma)
    return None


# Programa principal
if __name__ == '__main__':
    main()
