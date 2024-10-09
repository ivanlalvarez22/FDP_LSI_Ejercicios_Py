# 7-Dados 100 números, realizar la suma de los positivos y de los negativos.

pos = 0
neg = 0

for i in range(10):
    numeros = int(input(f"Ingresar el {i + 1}° nro: "))

    if numeros > 0:
        pos += numeros
    else:
        neg += numeros

print("La suma de números positivos da: ", pos)
print("La suma de números negativos da: ", neg)
