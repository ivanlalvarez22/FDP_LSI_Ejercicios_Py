# Dada una serie de números, cuyo final viene dado por el ingreso del cero, que representan los precios
# de las diferentes variedades de café que ofrece una cafetería, mostrar:
# El mayor precio y el menor precio.
# El precio promedio.
# Si existe alguna variedad de café que tiene un costo superior a los $1000
# Datos de entrada: una serie de números cuyo final viene dado por el "0"
# Datos de salida: el mayor precio y el menor precio, precio promedio, mostrar si hay algun cafe > $1000

precio = float(input("Ingresar el precio de las variedades de café (Ingrese el valor '0' para finalizar): "))
mayor = precio
menor = precio
bandera = False
suma = 0
prom = 0
C = 0

while precio != 0:
    suma += precio
    C += 1
    if precio > mayor:
        mayor = precio
    else:
        menor = precio
    if precio >= 1000:
        bandera = True

    precio = float(input("ingrese el precio: "))

print("El promedio es: %.2f" % (suma / C))
print("El mayor precio es: %.2f" % mayor)
print("El menor precio es: %.2f" % menor)

if bandera:  # Solo es necesario poner "if cond:" no hace falta poner "if cond == true"
    print("Hay precios que exceden los $1000")
else:
    print("No hay precios que excedan los $1000")
