frase = str(input("Ingrese una frase: "))
dim = len(frase)
cant_voc = 0
for i in range(dim):
    if frase[i].lower() in "aeiou":
        cant_voc = cant_voc + 1
print("La cantidad de vocales es: ", cant_voc)
