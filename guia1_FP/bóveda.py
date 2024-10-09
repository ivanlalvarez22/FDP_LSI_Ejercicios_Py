bovCode = "0016"
inCode = ""
i = 0
while bovCode != inCode and i < 3:
    print("quedan ", 3-i, " intentos")
    inCode = input("ingrese un numero de 4 cifras ")
    if len(inCode) != 4:  # len (consulta la cantidad de elementos de una variable)
        print("el codigo no tiene 4 cifras")
        i += 1
    elif bovCode != inCode:
        print("el codigo no es correcto")
        i += 1
if i >= 3:
    print("no hay mas intentos")
else:
    print("el codigo es correcto")
