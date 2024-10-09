# Para N ternas de datos correspondientes a los empleados de una empresa: DNI,
# Sexo ('F' -Femenino, 'M' -Masculino)  y  DT  (días  trabajados), y teniendo en cuenta que
# por  cada  día  trabajado  se  abona  $9.000, mostrar:
# 1.-Cantidad de empleados mujeres que hayan trabajado menos de 20 días.
# 2.-Sueldo promedio de los empleados varones.
# 3.-Porcentaje de empleadas mujeres.
# 4.-Total  que  gasta  la  empresa  en  sueldos,  discriminar además  lo  que  gasta  tanto
# en  varones  como  en mujeres.
# Datos de entrada: N ternas de datos DNI SEXO (F M) y DT
# Datos de salida: cant empleados mujeres que hayan trabajado menos de 20 días
# sueldo promedio de empleados varones
# porcentaje de empleadas mujeres y lo que gasta la empresa en sueldos
# mostrar lo que gasta en sueldos de varones y mujeres

N = int(input("Escriba la cantidad de empleados a ingresar: "))
c = 0
suel_v = 0
suel_m = 0
prom = 0
cant_v = 0
cant_m = 0
DT_m = 0

while c < N:
    DNI = int(input("Ingrese el DNI del empleado/a: "))
    sexo = str(input("Ingrese el sexo del empleado/a (F: femenino, M: masculino): "))
    DT = int(input("Ingrese los días trabajados por el empleado/a: "))
    if sexo.upper() == "F":
        suel_m = suel_m + DT * 9000
        cant_m += 1
        if DT < 20:
            DT_m += 1

    if sexo.upper() == "M":
        suel_v = suel_v + DT * 9000
        cant_v += 1

    c += 1
sueldo = suel_v + suel_m
porc_m = (cant_m * 100) / c

if cant_v > 0:
    prom = suel_v / cant_v

print("La cantidad de mujeres que trabajaron menos de 20 días son: %d" % DT_m)
print("El sueldo promedio de empleados varones es: $%d" % prom)
print("El porcentaje de mujeres es: %.2f" % porc_m)
print("Total de gasto en sueldos: $%d" % sueldo)
print("Sueldo gastado en empleados varones: $%d" % suel_v)
print("Sueldo gastado en empleadas mujeres: $%d" % suel_m)
