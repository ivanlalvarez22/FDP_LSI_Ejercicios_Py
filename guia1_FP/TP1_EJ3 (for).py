# Para aprobar una materia se debe sacar 6 ó más en cada una de las 6 evaluaciones.
# También se sabe que solo se puede desaprobar una sola evaluación y en ese caso,
# se debe aprobar la evaluación integral con una nota mayor a 7.
# Diseñe un algoritmo que ayude a saber si aprobó o no la materia. '''

# Datos de entrada: La nota de cada una de las 6 evaluaciones
# Datos de salida: Saber si desaprobó o no la materia y en caso de haber desaprobado 1 solo examen
# averiguar si aprobó o no la evaluación integral

C = 0
nombre = input("Hola ¿Cómo te llamas? ")
for i in ["primer", "segunda", "tercera", "cuarta", "quinta", "sexta"]:
    nota = float(input(f"Ingrese la {i} nota del examen: "))
    if (nota >= 6) and (nota <= 10):
        C = C + 1

if C == 6:
    print("FELICITACIONES %s ¡Aprobaste!" % nombre)
elif C == 5:
    nota_integrador = float(input("Ingrese la nota del examen integrador: "))
    if (nota_integrador >= 7) and (nota_integrador <= 10):
        print("FELICITACIONES %s ¡Aprobaste!" % nombre)
    else:
        print("Desaprobaste")
else:
    print("Desaprobaste")
