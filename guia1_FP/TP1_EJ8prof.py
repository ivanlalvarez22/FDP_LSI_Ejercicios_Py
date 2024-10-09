# Entradas: precio del café
# Salidas: El mayor precio, el menor precio, el promedio y si existe uno mayor a $1000
# Por cada precio ingresado verificar con setencias condicionales el mayor,
# el menor y si existe un precio mayor a $1000
# Sumar todos los precios ingresados y contar la cantidad de precios ingresados
# para poder calcular el promedio (suma/cant)

mayor = 0
menor = 9999999
suma = 0
cant = 0
existe = False
precio = float(input("Ingrese el precio del café (0 para Salir): "))
while precio != 0:
    if precio > mayor:
        mayor = precio
    if precio < menor:
        menor = precio
    if precio > 1000:
        existe = True
    suma += precio
    cant += 1
    precio = float(input("Ingrese el precio del café (0 para Salir): "))
if cant > 0: # para que no salte error en la división por 0 en caso de no haber ingresado precios
    print("El mayor precio es %.2f" % mayor)
    print("El menor precio es %.2f" % menor)
    print("El precio promedio es %.2f" % (suma/cant))
    if existe:
        print("Existe un precio mayor a $1000")
    else:
        print("NO existe un precio mayor a $1000")
