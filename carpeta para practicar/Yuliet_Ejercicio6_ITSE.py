# 6-Dados tres números A, B y C imprimir el mayor de ellos.

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

if A > B and A > C:
    print("El mayor es: ", A)
elif B > C:
    print("El mayor es: ", B)
else:
    print("El mayor es: ", C)
