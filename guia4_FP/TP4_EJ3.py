# Un hotel registra la siguiente información para cada una de sus 10 habitaciones:
# Número de Habitación, Tipo de Habitación{simple,  doble,  triple,  suite}, Precio por Día,
# Estado {ocupado,  disponible} y  Cantidad  de  Días Ocupados.
# Mostrar:
# a) La recaudación de una determinada habitación teniendo en cuenta la Cantidad de Días Ocupados.
# b) El porcentaje de ocupación total del hotel, y el porcentaje de ocupación de cada uno de
# los tipos de habitaciones existentes.

import numpy as np


# Definición de módulos


def mostrar_menu():
    print("------ MENÚ PRINCIPAL------\n"
          "1) Cargar registro estático\n"
          "2) Mostrar registro\n"
          "3) Mostrar recaudación por habitación\n"
          "4) Mostrar el porcentaje de ocupación\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para finalizar: "))
    return op


def cargar_registro_estatico(mh):
    mh[0] = (121, "suite", 6500, "ocupado", 7)
    mh[1] = (127, "triple", 3900, "ocupado", 12)
    mh[2] = (125, "simple", 2700, "disponible", 0)
    mh[3] = (123, "doble", 3500, "ocupado", 14)
    mh[4] = (129, "doble", 3500, "disponible", 0)
    print("Registro correctamente cargado")
    return None


def mostrar_registro(mh, d):
    print("Nro habitación         Tipo habitación          Precio          Estado          C. dias ocupado")
    for i in range(d):
        print(mh[i]["nro_habitacion"], end="                    ")
        print(str(mh[i]["tipo_habitacion"]).ljust(10), end="             ")
        print("$", mh[i]["precio"], end="          ")
        print(str(mh[i]["estado"]).ljust(10), end="            ")
        print(mh[i]["cant_dias_ocupado"])
    return None


def mostrar_recaudacion(mh, d):
    hab = int(input("Ingrese un número de habitación para calcular la recaudación: "))
    b = False
    for i in range(d):
        if hab == mh[i]["nro_habitacion"]:
            recaudacion = mh[i]["cant_dias_ocupado"] * mh[i]["precio"]
            print(f"La recaudación de la habitación {hab} es: ${recaudacion}")
            b = True
    if not b:
        print("Habitación inexistente")
    return None


def obtener_pje_ocup_total(mh, d):
    cp = 0
    c_simple_total = 0
    c_simple = 0
    c_doble_total = 0
    c_doble = 0
    c_triple_total = 0
    c_triple = 0
    c_suite_total = 0
    c_suite = 0
    for i in range(d):
        if mh[i]["estado"] == "ocupado":
            cp += 1
        if mh[i]["tipo_habitacion"] == "simple":
            c_simple_total += 1
            if mh[i]["estado"] == "ocupado":
                c_simple += 1
        if mh[i]["tipo_habitacion"] == "doble":
            c_doble_total += 1
            if mh[i]["estado"] == "ocupado":
                c_doble += 1
        if mh[i]["tipo_habitacion"] == "triple":
            c_triple_total += 1
            if mh[i]["estado"] == "ocupado":
                c_triple += 1
        if mh[i]["tipo_habitacion"] == "suite":
            c_suite_total += 1
            if mh[i]["estado"] == "ocupado":
                c_suite += 1
    pje_ocup_total = obtener_pje(cp, d)
    pje_ocup_simple = obtener_pje(c_simple, c_simple_total)
    pje_ocup_doble = obtener_pje(c_doble, c_doble_total)
    pje_ocup_triple = obtener_pje(c_triple, c_triple_total)
    pje_ocup_suite = obtener_pje(c_suite, c_suite_total)
    print(f"El porcentaje de ocupación total en el hotel es del %{pje_ocup_total}")
    print(f"El porcentaje de ocupación en habitaciones simples es: %{pje_ocup_simple}")
    print(f"El porcentaje de ocupación en habitaciones dobles es: %{pje_ocup_doble}")
    print(f"El porcentaje de ocupación en habitaciones triples es: %{pje_ocup_triple}")
    print(f"El porcentaje de ocupación en habitaciones suites es: %{pje_ocup_suite}")
    return None


def obtener_pje(suma_parcial, suma_total):
    pje = (suma_parcial / suma_total) * 100
    return pje


# Programa principal
# Estructura del registro

Tdatos_habitacion = np.dtype(
    [
        ("nro_habitacion", int),
        ("tipo_habitacion", "U50"),
        ("precio", float),
        ("estado", "U50"),
        ("cant_dias_ocupado", int)
    ]
)

# Arreglo de registros
N = 5
mis_habitaciones = np.empty(N, dtype=Tdatos_habitacion)
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado")
        salir = True
    elif opc == 1:
        cargar_registro_estatico(mis_habitaciones)
    elif opc == 2:
        mostrar_registro(mis_habitaciones, N)
    elif opc == 3:
        mostrar_recaudacion(mis_habitaciones, N)
    elif opc == 4:
        obtener_pje_ocup_total(mis_habitaciones, N)
