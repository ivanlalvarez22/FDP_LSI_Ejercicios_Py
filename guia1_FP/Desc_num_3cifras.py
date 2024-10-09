# Forma sencilla para descomponer un n° de 3 cifras
# La operación '//' lo que hace es devolvernos la parte entera de la división
# lo mismo que escribir 'int(num / 10)'
num = int(input("Ingresar un número de 3 cifras: "))
centena = num // 100
decena = (num // 10) % 10
unidad = num % 10
print("El dígito de la centena del n° ingresado es: ", centena)
print("El dígito de la decena del n° ingresado es: ", decena)
print("El dígito de la unidad del n° ingresado es: ", unidad)

"""
resto del número = (num // 10)
unidad = num % 10
"""
