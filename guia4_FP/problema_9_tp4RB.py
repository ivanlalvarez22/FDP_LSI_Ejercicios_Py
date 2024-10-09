import numpy as np

"""
9. Un aeropuerto registra para cada uno de los aviones la siguiente
información: Línea Aérea, Número de Vuelo, Datos del Viaje (Ciudad Origen,
Hora de Salida, Ciudad Destino, Hora de Llegada) y Cantidad de Pasajeros.
Se pide:

a) Mostrar la línea aérea que tenga el mayor número de pasajeros como Ciudad
Destino Paris.

b) Generar una estructura que contenga el número de vuelo, datos del viaje y la
cantidad de pasajeros de todos los aviones que tienen como Ciudad Origen Roma.
"""


# ------------------------------Sección de Módulos------------------------------


def load_airport_s(a):
    a[0] = ("L.A. 1", 111, ("Roma", (8, 50), "Milan", (10, 15)), 60)
    a[1] = ("L.A. 1", 211, ("Roma", (12, 20), "Paris", (13, 15)), 25)
    a[2] = ("L.A. 1", 181, ("Roma", (16, 5), "Berna", (18, 15)), 50)
    a[3] = ("L.A. 2", 110, ("Roma", (18, 55), "Berlin", (21, 15)), 40)
    a[4] = ("L.A. 2", 145, ("Paris", (13, 20), "Milan", (15, 15)), 90)
    a[5] = ("L.A. 2", 454, ("Madrid", (11, 50), "Londres", (14, 15)), 120)
    a[6] = ("L.A. 3", 147, ("Zurich", (16, 0), "Paris", (18, 15)), 135)
    a[7] = ("L.A. 3", 114, ("Ginebra", (17, 50), "Paris", (20, 15)), 45)
    a[8] = ("L.A. 3", 845, ("Lucerna", (10, 30), "Paris", (12, 15)), 54)
    a[9] = ("L.A. 3", 212, ("Basilea", (11, 0), "Milan", (13, 15)), 80)
    dim_a = 10
    return dim_a


# ------------------------------------Item a------------------------------------


def count_passengers(a, dim_a, airline, city):
    passengers = 0
    for i in range(dim_a):
        if (a[i]["linea_aerea"] == airline
                and a[i]["datos"]["ciudad_destino"] == city):
            passengers += a[i]["cantidad_pasajeros"]
    return passengers


def paris_airline_passengers(a, dim_a):
    high = 0
    for i in range(dim_a):
        passengers = count_passengers(a, dim_a, a[i]["linea_aerea"], "Paris")
        if passengers > high:
            high = passengers
            airline = a[i]["linea_aerea"]
    if high > 0:
        print(f"La linea aérea '{airline}' tiene el mayor numero de pasajeros a "
              f"Paris, con una cantidad de {high} pasajeros.")
    else:
        print("Ninguna linea aérea tiene vuelos con destino a Paris.")


# ------------------------------------Item b------------------------------------


def load_rome_airport(a, dim_a, r):
    j = 0
    for i in range(dim_a):
        if a[i]["datos"]["ciudad_origen"] == "Roma":
            r[j]["numero_vuelo"] = a[i]["numero_vuelo"]
            r[j]["datos"]["ciudad_origen"] = a[i]["datos"]["ciudad_origen"]
            r[j]["datos"]["salida"]["hr"] = a[i]["datos"]["salida"]["hr"]
            r[j]["datos"]["salida"]["min"] = a[i]["datos"]["salida"]["min"]
            r[j]["datos"]["ciudad_destino"] = a[i]["datos"]["ciudad_destino"]
            r[j]["datos"]["llegada"]["hr"] = a[i]["datos"]["llegada"]["hr"]
            r[j]["datos"]["llegada"]["min"] = a[i]["datos"]["llegada"]["min"]
            r[j]["cantidad_pasajeros"] = a[i]["cantidad_pasajeros"]
            j += 1
    return j


def get_time(hours, minutes):
    if hours < 10:
        h = "0" + str(hours)
    else:
        h = str(hours)
    if minutes < 10:
        m = "0" + str(minutes)
    else:
        m = str(minutes)
    return h + ":" + m


def print_rome_airport(r, dim_r):
    print(
        "N.° VUELO    CIUDAD ORIGEN         SALIDA    "
        "CIUDAD DESTINO        LLEGADA    CANT.PASAJEROS"
    )
    for j in range(dim_r):
        number = str(r[j]["numero_vuelo"])
        origin = str(r[j]["datos"]["ciudad_origen"])
        departure = get_time(
            r[j]["datos"]["salida"]["hr"], r[j]["datos"]["salida"]["min"]
        )
        destination = str(r[j]["datos"]["ciudad_destino"])
        arrival = get_time(
            r[j]["datos"]["llegada"]["hr"], r[j]["datos"]["llegada"]["min"]
        )
        passengers = str(r[j]["cantidad_pasajeros"])
        print(
            number + " " * (13 - len(number))
            + origin + " " * (22 - len(origin))
            + departure + " " * (10 - len(departure))
            + destination + " " * (22 - len(destination))
            + arrival + " " * (11 - len(arrival))
            + passengers
        )


# ------------------------------------------------------------------------------


def main():
    time = np.dtype(
        [
            ("hr", int),
            ("min", int)
        ]
    )
    travel = np.dtype(
        [
            ("ciudad_origen", "U20"),
            ("salida", time),
            ("ciudad_destino", "U20"),
            ("llegada", time)
        ]
    )
    plane = np.dtype(
        [
            ("linea_aerea", "U20"),
            ("numero_vuelo", int),
            ("datos", travel),
            ("cantidad_pasajeros", int)
        ]
    )
    airport = np.empty(10, dtype=plane)
    rome_plane = np.dtype(
        [
            ("numero_vuelo", int),
            ("datos", travel),
            ("cantidad_pasajeros", int)
        ]
    )
    rome_airport = np.empty(10, dtype=rome_plane)
    dim_a = load_airport_s(airport)
    print("Item a)")
    paris_airline_passengers(airport, dim_a)
    print("")
    print("Item b)")
    dim_r = load_rome_airport(airport, dim_a, rome_airport)
    print_rome_airport(rome_airport, dim_r)


# ------------------------------Programa Principal------------------------------
main()
