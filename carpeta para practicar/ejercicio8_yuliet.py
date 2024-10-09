#-Dados 100 números, determinar la cantidad de positivos, negativos y nulos

pos = 0
neg = 0
nulo = 0

for i in range (10):
    numeros = int(input(f"Ingresar el {i + 1}° nro: "))
    if numeros > 0:
        pos+=1
    elif numeros == 0:
        nulo+=1
    else:
        neg+=1

print("La cantidad de positivos es de ", pos)
print("La cantidad de negativos es de ", neg)
print("La cantidad de numéros nulos es de ", nulo)
