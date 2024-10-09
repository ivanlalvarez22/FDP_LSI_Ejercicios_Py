# Ejemplo de suma de números. Debemos especificar a Python el tipo de dato ingresado
# En éste caso "int" nos indicará que el mismo es de valor entero

a = int(input("Ingrese un número entero: "))
b = float(input("Ingrese un número que contenga decimales: "))
c = a + b
print("La suma de los números ingresados es:", c)

# Ahora haré un ejemplo con las variables sin especificar su tipo
# En este caso al no especificar el tipo de dato, al querer sumar los números lo que hace el programa
# es juntar los números y no sumarlos porque interpreta que son una cadena de caracteres

a = input("Ingrese un número ")
b = input("Ingrese otro número ")
c = a + b
print("La suma de esos números es:", c)

# exponenciación
a = 2
b = 5
resultado = a ** b
print("El resultado de 2 elevado a la 5 es: ", resultado)

# división exacta usando doble '//'
a = 10
b = 3
resultado = a // b
print("El resultado de 10 entre 3 es: ", resultado)

# Módulo de la división

a = 10
b = 3
resultado = a % b
print("El módulo o resto de la división entre 10 y 3 es: ", resultado)
