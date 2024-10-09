# 5-Dado un número que representa la cantidad de lados de un polígono, determinar si se trata de un
# triángulo, cuadrilátero o de un pentágono;en caso de no tratarse de una de estas figuras, imprimir un mensaje.

LADOS = int(input("Cantidad de lados del polígono: "))

if LADOS == 3:
    print("Es un triangulo")
elif LADOS == 4:
    print("Es un cuadrilatero")
elif LADOS == 5:
    print("Es un pentagono")
else:
    print("No sé")

