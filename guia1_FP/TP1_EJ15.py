# Una empresa posee 3 sucursales. Cada sucursal tiene N empleados. Por cada sucursal se ingresa su
# Código de Sucursal; y para cada uno de sus empleados su DNI, sueldo y año de ingreso a la empresa. Se pide:
# * Calcular y mostrar el código de sucursal con el menor promedio de Sueldo
# * Calcular  y mostrar  para cada  sucursal  la  cantidad  de  empleados  que  tengan  una
# antigüedad mayor  o igual a 15 años y menor a 25 años.
# Datos de entrada: Por cada sucursal indicar la cantidad N de empleados, código de suc
# DNI, sueldo y año de ingreso
# Datos de salida: mostrar el código de sucursal con el menor número de promedio
# mostrar la cantidad de empleados que tengan una antigüedad mayor o igual a 15 años y menor a 25 años

c = 0
bandera = False
prom = 0
menor = 0
menor_prom_suc = 0

for c in range(3):
    cod_suc = int(input("Ingresar el código de sucursal: "))
    N = int(input("Ingresar la cantidad (N) de empleados: "))
    cant_emp = 0
    sum_prom = 0
    cant_antiguedad = 0

    for cant_emp in range(N):
        DNI = int(input(f"Ingresar el DNI del {cant_emp + 1}° empleado/a: "))
        sueldo = float(input("Ingresar el sueldo: "))
        anio_ingreso = int(input("Ingresar el año de ingreso: "))
        antiguedad = 2021 - anio_ingreso
        if 15 <= antiguedad < 25:
            cant_antiguedad += 1
        sum_prom = sum_prom + sueldo
        cant_emp += 1

    if cant_emp > 0:
        prom = sum_prom / cant_emp

    if not bandera:
        menor = prom
        menor_prom_suc = cod_suc
        bandera = True
    elif prom < menor:
        menor = prom
        menor_prom_suc = cod_suc

    print(f"De la sucursal {cod_suc}")
    print(f"Cantidad de empleados con antigüedad entre 15 y 25 años: {cant_antiguedad}")
    c += 1

print(f"La sucursal con menor promedio de sueldos es la suc {menor_prom_suc}")
print("El promedio de sueldos de la misma es: %.2f" % menor)
