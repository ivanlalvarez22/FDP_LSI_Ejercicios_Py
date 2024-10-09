# 12-Obtener e imprimir la suma de todos los números pares entre 1 y 100.

suma = 0

i = 0
while i <= 100:
    print(i)

    suma += i
    i += 2
print("La suma de los números pares es", suma)

for i in range(0, 101, 2):
    print(i)
