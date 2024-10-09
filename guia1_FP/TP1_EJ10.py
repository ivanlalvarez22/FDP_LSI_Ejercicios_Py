# Leandro quiere entrar en la bóveda secreta de la cátedra (bueno, no es tan secreta ya...) y para eso,
# debe ingresar la clave numérica que salvaguarda todos nuestros tesoros, la cual es de 4 dígitos.
# Está decidido a entrar por lo que no se resignará. Leandro sabrá que ha adivinado la clave,
# cuando vea el mensaje: "Has ingresado a la bóveda secreta"
# Datos de entrada: clave númerica de 4 dígitos
# Datos de salida: un mensaje indicando que ingresó a la bóveda

CLAVE = 1234
codigo = ""

while CLAVE != codigo:
    codigo = int(input("Ingrese la contraseña: "))
    if codigo < 1000 or codigo > 9999:
        print("La clave debe ser de 4 dígitos")

print("Has ingresado a la bóveda")
