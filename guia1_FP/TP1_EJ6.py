# Una empresa tiene 7 empleados. Indicar la cantidad de empleados varones y mujeres que tiene la misma.
# Datos de entrada: ingreso por teclado de letra V para varon y M para mujer
# Datos de salida: indicar la cantidad de empleados varones y cant de empleadas mujeres de la empresa.
# estructura iterativa

emp_mujer = 0
emp_varon = 0
i = 1
print("M = mujer / V = varón")
while i <= 7:
    print("Ingresar el sexo del ", i, " empleado: ")
    empleado = str(input()).upper()

    if empleado == "M":
        emp_mujer += 1
        i += 1

    elif empleado == "V":
        emp_varon += 1
        i += 1

print("La cantidad de varones es: %d \n La cantidad de mujeres es: %d" % (emp_varon, emp_mujer))
