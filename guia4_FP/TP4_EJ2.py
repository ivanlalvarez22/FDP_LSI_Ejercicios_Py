# El gerente de producción de una fábrica de muebles registra para cada uno de sus
# productos: Código de Producto, Nombre, Producción Anual, Cantidad Vendida y Precio. Se pide:
# a) Mostrar un informe al gerente general con el siguiente formato:
# ----------------------------------------------------------------------------------
#            INFORME DE PRODUCCIÓN Y VENTA
# Producción Anual      Nombre Producto     Ganancia Anual
# 60000                 Mesa                $ xxxxx
# 80000                 Silla               $ xxxxx
# 50000                 Placard             $ xxxxx
import numpy as np


def mostrar_menu():
    print("------ MENÚ PRINCIPAL ------")
    print("1) Cargar registro (estático)")
    print("2) Cargar registro (dinámico)")
    print("3) Mostrar registro")
    print("4) Generar infrome de producción y venta")
    print("Ingrese el '0' para finalizar")
    op = int(input("Ingrese una opción para continuar: "))
    return op


def cargar_registro_estatico(mp):
    mp[0] = (1, "Mesa".ljust(10), 60000, 45000, 7000)
    mp[1] = (2, "Silla".ljust(10), 80000, 50000, 3000)
    mp[2] = (3, "Placard".ljust(10), 50000, 35000, 20000)
    print("Registro cargado correctamente")
    return None


def cargar_registro_dinamico(mp, d):
    for i in range(d):
        mp[i]["cod_producto"] = int(input("Ingrese el código de producto: "))
        mp[i]["nombre"] = input("Ingrese el nombre: ")
        mp[i]["prod_anual"] = int(input("Ingrese la producción anual: "))
        mp[i]["cant_vendida"] = int(input("Ingrese la cantidad vendida: "))
        mp[i]["precio"] = float(input("Ingrese el precio: "))
    return None


def mostrar_registro(mp, d):
    print("Código de producto    Nombre           Producción anual    Cantidad vendida    Precio    ")
    for i in range(d):
        print(mp[i]["cod_producto"], end="                     ")
        print(str(mp[i]["nombre"]).ljust(12), end="     ")  # 'ljust()' justifica a la izquierda nuestra cadena
        print(mp[i]["prod_anual"], end="               ")
        print(mp[i]["cant_vendida"], end="               ")
        print(mp[i]["precio"])
    return None


def generar_informe(mp, d):
    print("Producción anual     Nombre producto           Ganancia anual")
    for i in range(d):
        print(mp[i]["prod_anual"], end="                ")
        print(str(mp[i]["nombre"]).ljust(15), end="                ")
        print("$", obtener_ganancia_anual(mp, i))
    return None

# Nombre del módulo: obtener_ganancia_anual
# Recibe como parametros al vector 'mis productos' y a una posición del mismo
# Nos devuelve la ganancia anual multiplicando los campos 'cant_vendida' * 'precio' ubicados en la posicion 'i'
def obtener_ganancia_anual(mp, i):
    ganancia_anual = mp[i]["cant_vendida"] * mp[i]["precio"]
    return ganancia_anual


# -----Programa principal--------
# Estructura del registro
datos_productos = np.dtype(
    [
        ("cod_producto", int),
        ("nombre", "U50"),
        ("prod_anual", int),
        ("cant_vendida", int),
        ("precio", float)
    ]
)

# Arreglo de registros
N = 3
mis_productos = np.empty(N, dtype=datos_productos)

salir = False
while not salir:
    opc = mostrar_menu()
    if opc == 0:
        print("Programa finalizado")
        salir = True
    elif opc == 1:
        cargar_registro_estatico(mis_productos)
    elif opc == 2:
        cargar_registro_dinamico(mis_productos, N)
    elif opc == 3:
        mostrar_registro(mis_productos, N)
    elif opc == 4:
        generar_informe(mis_productos, N)
