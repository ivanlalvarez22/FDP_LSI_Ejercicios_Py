# Una editorial que posee diferentes publicaciones, maneja la siguiente información:
# Código de Publicación, Cantidad de Ejemplares Impresos, Precio Unitario y
# Frecuencia de Tirada{diaria, semanal, mensual,anual}; para atender los siguientes requerimientos de trabajo:

# a) Generar una estructura de datos con los Códigos de Publicación diaria.

# b) Informar cuál sería el monto de dinero que se espera recaudar en el año. Para ello deberá tener en cuenta
# que las publicaciones tienen distinta frecuencia de tirada.

import numpy as np

# Definición de módulos


def mostrar_menu():
    print("-----------------MENÚ PRINCIPAL-----------------\n"
          "1) Cargar registro\n"
          "2) Mostrar registro \n"
          "3) Generar estructura de datos con códigos de publicación diaria\n"
          "4) Informar el monto de dinero que se espera recaudar en el año\n"
          "Ingrese el '0' para finalizar")
    op = int(input("Por favor ingrese una opción para continuar: "))
    return op


def cargar_registro(me):
    me[0] = (1418, 100, 40, 1)
    me[1] = (1564, 150, 55, 1)
    me[2] = (2021, 120, 80, 2)
    me[3] = (2012, 600, 70, 2)
    me[4] = (2133, 150, 50, 2)
    me[5] = (3080, 450, 20, 3)
    me[6] = (3044, 700, 15, 3)
    me[7] = (4099, 100, 60, 4)
    me[8] = (4087, 300, 75, 4)
    me[9] = (1565, 110, 25, 1)
    print("\nRegistro correctamente cargado!\n")
    return None


def mostrar_registro(me, d):
    print("COD. PUBLICACIÓN      CANT. EJEMPLARES IMPRESOS      PRECIO UNITARIO       FREC. TIRADA")
    for i in range(d):
        print(me[i]["cod_publicacion"], end="                  ")
        print(me[i]["cant_ejemplares_impresos"], end="                            ")
        print("$", me[i]["precio_unitario"], end="                ")
        print(convertir_frecuencia_caracter(me[i]["frec_tirada"]))
    return None


def convertir_frecuencia_caracter(num):
    if num == 1:
        num = "diario"
    elif num == 2:
        num = "semanal"
    elif num == 3:
        num = "mensual"
    else:
        num = "anual"
    return num


def generar_estructura_cod_pdiaria(me, d, me_pd):
    j = 0
    for i in range(d):
        if me[i]["frec_tirada"] == 1:
            me_pd[j]["cod_publicacion"] = me[i]["cod_publicacion"]
            j += 1
    return j


def mostrar_estructura_cod_pdiaria(me_pd, d):
    for i in range(d):
        print(me_pd[i]["cod_publicacion"])
    return None


def calcular_importe_anual(frecuencia, precio, cantidad):
    if frecuencia == 1:
        importe_anual = precio * cantidad * 365
    elif frecuencia == 2:
        importe_anual = precio * cantidad * 52
    elif frecuencia == 3:
        importe_anual = precio * cantidad * 12
    else:
        importe_anual = precio * cantidad
    return importe_anual


def generar_informe(me, d):
    monto = 0
    cod = int(input("Ingrese un código de publicación para generar el informe con la recaudación anual: "))
    for i in range(d):
        if cod == me[i]["cod_publicacion"]:
            monto = calcular_importe_anual(me[i]["frec_tirada"], me[i]["precio_unitario"],
                                           me[i]["cant_ejemplares_impresos"])
    print(f"El monto de dinero que se espera recaudar según los datos ingresados es: ${monto}")
    return None


# Programa principal
# Estructura del registro

Tdatos_editorial = np.dtype(
    [
        ("cod_publicacion", int),
        ("cant_ejemplares_impresos", int),
        ("precio_unitario", float),
        ("frec_tirada", int)
    ]
)

# Arreglo de registros
N = 10
mis_editoriales = np.empty(N, dtype=Tdatos_editorial)
mis_editoriales_pub_diarias = np.empty(10, dtype=Tdatos_editorial)
salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado!")
        salir = True
    elif opc == 1:
        cargar_registro(mis_editoriales)
    elif opc == 2:
        mostrar_registro(mis_editoriales, N)
    elif opc == 3:
        dim_pd = generar_estructura_cod_pdiaria(mis_editoriales, N, mis_editoriales_pub_diarias)
        mostrar_estructura_cod_pdiaria(mis_editoriales_pub_diarias, dim_pd)
    elif opc == 4:
        generar_informe(mis_editoriales, N)
