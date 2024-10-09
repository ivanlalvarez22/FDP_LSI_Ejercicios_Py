import numpy as np

"""
8. Una biblioteca registra para cada uno de sus libros la siguiente
información: Número de Inventario, Nombre del Libro, Código de Autor, Precio de
 Compra y Estado {1-Buen Estado, 2-Deteriorado, 3-Robado}. Se pide:

a) Realizar el ingreso de los datos, cuyo final está dado por número de
inventario igual a cero.

b) Mostrar los datos de aquellos libros cuyo precio de compra sea
mayor a $1075.

c) Para un código de autor, mostrar la cantidad de libros que se tiene del
mismo.

d) Generar un arreglo con el número de inventario y el nombre de aquellos
libros que estén deteriorados.
"""
# ------------------------------Sección de Módulos------------------------------


def load_inventory_s(inv):
    inv[0] = (1287684, "Álgebra y Geometría", 554, 1500.0, 1)
    inv[1] = (5646484, "Álgebra III", 554, 1200.0, 3)
    inv[2] = (4577845, "Programación IV", 554, 2000.0, 2)
    inv[3] = (8787687, "Lógica I", 252, 700.0, 2)
    inv[4] = (4568878, "Diccionario", 252, 400.0, 1)
    inv[5] = (8897874, "Cálculo I", 252, 1000.0, 2)
    inv[6] = (8775878, "Guia C++", 252, 1300.0, 1)
    inv[7] = (6456788, "Cálculo II", 898, 1100.0, 2)
    inv[8] = (4566767, "Introducción a C", 898, 800.0, 3)
    inv[9] = (6697878, "Guia Photoshop", 898, 600.0, 1)
    dim_i = 10
    return dim_i

# ------------------------------------Item a------------------------------------


def load_inventory_d(inv):
    i = 0
    load = True
    while load:
        inv[i]["num_inventario"] = int(input("N.° de inventario: "))
        if inv[i]["num_inventario"] != 0:
            inv[i]["nombre"] = input("Nombre del libro (max. 20 car.): ")
            inv[i]["codigo_autor"] = int(input("Código de autor: "))
            inv[i]["precio"] = float(input("Precio del libro: "))
            inv[i]["estado"] = int(
                input("Estado (1-Buen Estado, 2-Deteriorado, 3-Robado): ")
            )
            i += 1
        else:
            load = False
    return i


# ------------------------------------Item b------------------------------------


def get_state(num):
    state = ""
    if num == 1:
        state = "Buen Estado"
    elif num == 2:
        state = "Deteriorado"
    elif num == 3:
        state = "Robado"
    return state


def print_exp_books(inv, dim_i):
    print("Libros con un precio mayor a $1075:")
    print(
        "NUM. INVENTARIO   NOMBRE                COD. AUTOR    PRECIO    ESTADO"
    )
    for i in range(dim_i):
        if inv[i]["precio"] > 1075:
            inv_num = str(inv[i]["num_inventario"])
            name = str(inv[i]["nombre"])
            code = str(inv[i]["codigo_autor"])
            price = str(inv[i]["precio"])
            state = get_state(inv[i]["estado"])
            print(
                inv_num + " " * (18 - len(inv_num))
                + name + " " * (22 - len(name))
                + code + " " * (14 - len(code))
                + "$" + price + " " * (10 - len(price))
                + state
            )


# ------------------------------------Item c------------------------------------


def author_books_amount(inv, dim_i):
    code = int(input("Ingrese el código de autor: "))
    counter = 0
    for i in range(dim_i):
        if inv[i]["codigo_autor"] == code:
            counter += 1
    print(f"El autor de código {code} tiene {counter} libros.")


# ------------------------------------Item d------------------------------------


def deteriorated_books(inv, dim_i, det):
    j = 0
    for i in range(dim_i):
        if inv[i]["estado"] == 2:
            det[j]["num_inventario"] = inv[i]["num_inventario"]
            det[j]["nombre"] = inv[i]["nombre"]
            j += 1
    return j


def print_det_books_list(det, dim_d):
    print("Libros en estado deteriorado:")
    print("NUM. INVENTARIO   NOMBRE")
    for j in range(dim_d):
        inv_num = str(det[j]["num_inventario"])
        name = str(det[j]["nombre"])
        print(inv_num + " " * (18 - len(inv_num)) + name)


# ------------------------------------------------------------------------------


def main():
    book = np.dtype(
        [
            ("num_inventario", int),
            ("nombre", "U20"),
            ("codigo_autor", int),
            ("precio", float),
            ("estado", int)
        ]
    )
    inventory = np.empty(100, dtype=book)
    det_book = np.dtype(
        [
            ("num_inventario", int),
            ("nombre", "U20")
        ]
    )
    det_books_list = np.empty(100, dtype=det_book)
    # dim_i = load_inventory_d(inventory)  # Carga dinámica (Item a).
    dim_i = load_inventory_s(inventory)  # Carga estática.
    print_exp_books(inventory, dim_i)
    print("")
    author_books_amount(inventory, dim_i)
    dim_d = deteriorated_books(inventory, dim_i, det_books_list)
    print("")
    print_det_books_list(det_books_list, dim_d)


# ------------------------------Programa Principal------------------------------
main()
