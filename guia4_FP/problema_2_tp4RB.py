import numpy as np

"""
2. El gerente de producción de una fábrica de muebles registra para cada uno de
sus productos: Código de Producto, Nombre, Producción Anual, Cantidad Vendida y
 Precio. Se pide:

a) Mostrar un informe al gerente general con el siguiente formato:

INFORME DE PRODUCCIÓN Y VENTA
Producción Anual        Nombre Producto        Ganancia Anual
60000                   Mesa                    $ xxxxx
80000                   Silla                   $ xxxxx
50000                   Placard                 $ xxxxx
…                       …                       …

"""
# Sección de módulos.


def load_report(r, dim: int) -> None:
    """
    Carga valores en el arreglo report.
    :param r: Arreglo report.
    :param dim: Dimensión de report.
    :return: None
    """
    for i in range(dim):
        r[i]["codigo"] = int(input(f"{i+1}º mueble - código: "))
        r[i]["nombre"] = input(f"{i+1}º mueble - nombre (1-20 caracteres): ")
        r[i]["produccion"] = int(input(f"{i+1}º mueble - producción: "))
        r[i]["ventas"] = int(input(f"{i+1}º mueble - cantidad vendida: "))
        r[i]["precio"] = int(input(f"{i+1}º mueble - precio: "))


def print_report(r, dim: int) -> None:
    """
    Muestra los valores de report en una tabla.
    :param r: Arreglo report.
    :param dim: Dimensión de report.
    :return: None
    """
    print("INFORME DE PRODUCCIÓN Y VENTA")
    print("Producción Anual        Nombre Producto        Ganancia Anual")
    for i in range(dim):
        print(
            str(r[i]["produccion"]) + " " * (24 - len(str(r[i]["produccion"])))
            + str(r[i]["nombre"]) + " " * (24 - len(str(r[i]["nombre"])))
            + "$ " + str(r[i]["ventas"] * r[i]["precio"])
        )


def main() -> None:
    """
    Función principal.
    :return: None
    """
    furniture = np.dtype(
        [
            ("codigo", int),
            ("nombre", "U20"),
            ("produccion", int),
            ("ventas", int),
            ("precio", float)
        ]
    )
    products = int(input("Cantidad de productos: "))
    report = np.empty(products, dtype=furniture)
    load_report(report, products)
    print_report(report, products)


# Programa principal.
main()
