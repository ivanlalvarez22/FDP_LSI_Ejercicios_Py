# Para aprobar una materia se debe sacar 6 ó más en cada una de las 6 evaluaciones.
# También se sabe que solo se puede desaprobar una sola evaluación y en ese caso,
# se debe aprobar la evaluación integral con una nota mayor a 7.
# Diseñe un algoritmo que ayude a saber si aprobó o no la materia.

# Datos de entrada: La nota de cada una de las 6 evaluaciones
# Datos de salida: Saber si desaprobó o no la materia y en caso de haber desaprobado 1 solo examen
# averiguar si aprobó o no la evaluación integral

C = 0
nombre = input("¿Cómo te llamas? ")
nota1 = float(input("Ingrese la nota del primer examen: "))
if (nota1 >= 6) and (nota1 <= 10):
    C = C + 1
nota2 = float(input("Ingrese la nota del segundo examen: "))
if (nota2 >= 6) and (nota2 <= 10):
    C = C + 1
nota3 = float(input("Ingrese la nota del tercer examen: "))
if (nota3 >= 6) and (nota3 <= 10):
    C = C + 1
nota4 = float(input("Ingrese la nota del cuarto examen: "))
if (nota4 >= 6) and (nota4 <= 10):
    C = C + 1
nota5 = float(input("Ingrese la nota del quinto examen: "))
if (nota5 >= 6) and (nota5 <= 10):
    C = C + 1
nota6 = float(input("Ingrese la nota del sexto examen: "))
if (nota6 >= 6) and (nota6 <= 10):
    C = C + 1

if C == 6:
    print("¡FELICIDADES %s Aprobaste!" % nombre)
elif C == 5:
    notaIntegral = float(input("Ingrese la nota del examen integrador: "))
    if (notaIntegral >= 7) and (notaIntegral <= 10):
        print("¡FELICIDADES %s Aprobaste!" % nombre)
    else:
        print("Desaprobaste")
else:
    print("Desaprobaste")
