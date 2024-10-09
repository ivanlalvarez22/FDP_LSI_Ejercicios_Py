# Leandro quiere entrar en la bóveda secreta de la cátedra (bueno, no es tan secreta ya...) y para eso,
# debe ingresar la clave numérica que salvaguarda todos nuestros tesoros, la cual es de 4 dígitos.
# Está decidido a entrar por lo que no se resignará. Leandro sabrá que ha adivinado la clave,
# cuando vea el mensaje: "Has ingresado a la bóveda secreta"
# Datos de entrada: clave númerica de 4 dígitos
# Datos de salida: un mensaje indicando que ingresó a la bóveda

CLAVE = 2202
i = 3
codigo = int(input("Ingresar la contraseña: "))

while i > 0 and codigo != CLAVE:
    if codigo < 1000 or codigo > 10000:
        print("La clave debe ser de 4 dígitos")
    print("Quedan %d intentos" % i)
    codigo = int(input("Ingresar la contraseña: "))
    i -= 1

if codigo == CLAVE:
    print("Has ingresado a la bóveda secreta")
else:
    print("BÓVEDA BLOQUEDA!!!")
