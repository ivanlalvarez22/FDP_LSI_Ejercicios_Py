#3-Leer dos  números,  almacenarlos  en  las  variables  X  y  Y  respectivamente.  Intercambiar  el  contenido
# de  las variables de manera que el valor contenido en X pase a Y, y el valor contenido en Y pase a X.

X = int(input("X: "))
Y = int(input("Y: "))

aux = X
X = Y
Y = aux

print("El valor de X es: ", X)
print("El valor de Y es: ", Y)
