# maneras de intercambiar variables en python

# Forma clásica

a = int(input("a -> "))
b = int(input("b -> "))
aux = a
a = b
b = aux
print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")

# Otra forma permitida por python sin auxiliar

a = int(input("a -> "))
b = int(input("b -> "))

a, b = b, a
print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")
