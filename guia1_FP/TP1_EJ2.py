# La cordialidad ante todo. Se desea saludar al usuario dada una hora determinada diciéndole
#  “Buenos días”, “Buenas tardes” o ”Buenas noches” según corresponda
# Datos de entrada: la hora
# Datos de salidad: un saludo dependiendo la hora ingresada
# Estructuras condicionales para verificar si la hora está entre ciertos valores

hora = int(input("Ingrese la hora (1-24): "))
if (hora >= 1) and (hora <= 12):
    print("¡Buenos días!")
elif (hora >= 13) and (hora <= 18):
    print("¡Buenas tardes!")
elif (hora >= 19) and (hora <= 24):
    print("¡Buenas noches!")
else:
    print("¡Hora inválida!")
