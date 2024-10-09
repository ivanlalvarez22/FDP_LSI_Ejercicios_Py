# Charly va a hacer una fiesta, pero como es súper popular un montón de gente pretende asistir.
# El problema es que no entra mucha gente en su casa, sólo hay capacidad para 50 personas.
# Entonces se le ocurrió una idea buenísima para definir quienes entran y quiénes no.
# Decidió que a cada uno que quiera ingresar le iba a pedir un número, si este número está entre N y M,
# lo deja entrar, si no, no lo deja.Indique cuantas personas intentaron ingresar a la fiesta.
# Datos de entrada: Ingresar un número y si el mismo está entre N y M podra entrar a la fiesta
# Datos de salida: mostrar la cantidad de personas que intentaron entrar a la fiesta

N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))
c = 0
intentos = 0

while c < 5:
    num = int(input("Diga un número: "))
    if N <= num <= M:
        print("El número %d ingresó a la fiesta" % num)
        c += 1
    else:
        print("El número %d NO ingresó a la fiesta" % num)
        intentos += 1
print("La cantidad de personas que intentaron ingresar a la fiesta son: %d" % intentos)
