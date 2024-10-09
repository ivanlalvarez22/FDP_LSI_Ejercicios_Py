# 11-Dados 100 números, realizar la suma de los números pares e impares. Imprimir sumas.

sumapar = 0
sumaimpar = 0

for i in range (10):
    nro = int(input(f"Ingresar el {i + 1}° nro: "))
    if nro % 2 == 0:
        sumapar += nro
    else:
        sumaimpar += nro

print("La suma de los números pares da", sumapar)
print("La suma de los números impares da", sumaimpar)
