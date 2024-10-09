# La conjetura de Ulam afirma que dado un entero y siguiendo los siguientes pasos siempre obtenemos 1.
# * Si el número es par se divide por 2.
# * Si es impar se multiplica por 3 y se suma 1.
# Escribe un programa que le pida al usuario el ingreso de números enteros y que compruebe
# si la conjetura de  Ulam  es  cierta,  el  programa  deberá  escribir  toda  la  secuencia
# hasta  llegar  al  uno.  Por  ejemplo,  si  el usuario introduce
# un 5 la secuencia sería: 5, 16, 8, 4, 2, 1. El final viene dado por el ingreso de -1.
# Datos de entrada: se introduce un número
# Datos de salida: mostrar toda la secuencia de operaciones según el nro introducido

num = int(input("Ingrese un número (-1) para finalizar: "))

while num != -1:
    print("La secuencia es la siguiente: ")
    if num != 0:
        while num % 2 == 0 or num != 1:
            if num % 2 != 0:
                num = num * 3 + 1
                print(num, end=" ")  # "end" es equivalente a 'Sin Saltar' de Pseint

            num = int(num / 2)
            print(num, end=" ")

    print(" ")
    num = int(input("Ingrese un número (-1) para finalizar: "))
