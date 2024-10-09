# 10-Dados 75 números, imprimir los números negativos, el promedio de los positivos y la cantidad de nulos

prom = 0
cPos = 0
sumPos = 0
nulos = 0
neg = 0

for i in range(10):
    nro = int(input(f"Ingresar el {i + 1}° nro: "))

    if nro < 0:
        print(nro)
    elif nro == 0:
        nulos += 1
    else:
        sumPos += nro
        cPos += 1

if cPos > 0:
    prom = sumPos / cPos
    print("El promedio de los números positivos es de ", prom)
else:
    print("Div x 0")

print("cant nulos: ", nulos)
