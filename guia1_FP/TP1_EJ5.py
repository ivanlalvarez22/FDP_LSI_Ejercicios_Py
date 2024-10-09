# El cuadrante en el que comienza una recta con respecto al origen se encuentra determinado por el valor
# del ángulo de la línea con el eje x positivo, de acuerdo a lo siguiente:
# Entre 0 y 90 grados: primer cuadrante, entre 90 y 180 grados: segundo cuadrante, entre 180 y 270 grados
# tercer cuadrante y entre 270 y 360 grados cuarto cuadrante.
# Ingresar  el  ángulo  de  la  línea, y  proceder  a determinar  y  mostrar  el  cuadrante  correcto  para
# el  dato proporcionado. (Nota: Si el ángulo es exactamente 0, 90, 180, o 270 grados,
# la línea correspondiente no reside en ningún cuadrante, pero se encuentra en un eje,
# por lo tanto debe mostrar esta situación).
# Datos de entrada: el ángulo de una recta
# Datos de salida: mostrar a qué cuadrante pertenece esa recta
# si el angulo es 0, 90, 180 o 270 aclarar que no pertenece a ningún cuadrante pero se encuentra
# en un eje

angulo = int(input("Escribir el ángulo de la recta: "))
if (angulo > 0) and (angulo < 90):
    print("El ángulo se encuentra en el I cuadrante")
elif (angulo > 90) and (angulo < 180):
    print("El ángulo se encuentra en el II cuadrante")
elif (angulo > 180) and (angulo < 270):
    print("El ángulo se encuentra en el III cuadrante")
elif (angulo > 270) and (angulo < 360):
    print("El ángulo se encuentra en el IV cuadrante")

eje = angulo/90
if eje == 1:
    print("La recta se encuentra en el eje Y positivo")
elif eje == 2:
    print("La recta se encuentra en el eje X negativo")
elif eje == 3:
    print("La recta se encuentra en el eje Y negativo")
elif (eje == 4) or (eje == 0):
    print("La recta se encuentra en el eje X positivo")
