# print con formato
# string: %s (cadena de texto)
# number: %d (número entero)
# float: %f ".2f" (indica cant de cifras decimales a mostrar)

nombre = "Juan"
edad = 23
peso = 56.7784853
print("%s tiene %d años y pesa %.2f kilos" % (nombre, edad, peso))

# Otro ejemplo

datos = ("Juan", "Perez", 53.44)
format_string = "Hola %s %s. Tu balance es de %d."

print(format_string % datos)

# Otro ejemplo
nombre = "Iván"
apellido = "Alvarez"
edad = 26
peso = 83.0264
print("Hola {} {} tienes {} años y pesas {} kilogramos".format(nombre, apellido, edad, peso))

nombre = "Iván Leandro"
apellido = "Alvarez"
edad = 26
peso = 82.235
print(f"Hola {nombre} {apellido} tienes {edad} años y tu peso es de {peso} kilogramos")

# Mostrar el tipo de dato función 'type'
'''Los comentarios en python
pueden tener 2 líneas o mas usando comillas triples'''
dato1 = 10
dato2 = 3.1415
dato3 = "computadora"
dato4 = True
print(type(dato1))
print(type(dato2))
print(type(dato3))
print(type(dato4))
