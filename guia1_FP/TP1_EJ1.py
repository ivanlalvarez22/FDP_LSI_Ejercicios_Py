import math
N = float(input("Ingresar la longitud en metros de la escalera "))
M = float(input("Ahora escriba la distancia que separa a la pared del pie de la escalera "))
altura = math.sqrt(N*N - M*M)
print("La altura que alcanza la escalera sobre la pared es: %.4f" % altura)
