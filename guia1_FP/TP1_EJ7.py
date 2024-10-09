# Si estuvieras parado en la luna en este momento, tu peso sería 16.5% más de lo que es en
# la Tierra. Si aumentaras un kilo de peso cada año durante los siguientes N años,
# ¿cuál sería tu peso en la Luna cada año y al final de los N años?
# Entradas: Años que estará en la luna y el peso actual
# Salida: El peso lunar al final de lo N años
# Sentencia iterativa para ir calculando el peso lunar año por año
# hasta que sea igual al año ingresado

peso = float(input("Ingrese su peso actual: "))
anios = int(input("Ingrese la cantidad de años: "))

for i in range(anios):
    peso += 1
    peso_lunar = peso * 1.165
    print("Su peso lunar en el", i + 1, "año será: %.2f" % peso_lunar)
