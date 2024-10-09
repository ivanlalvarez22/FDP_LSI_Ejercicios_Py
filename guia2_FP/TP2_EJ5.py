# Dado el vector X, el cual contiene la  letra inicial  del nombre  de cada uno de
# los alumnos de  Álgebra  I. Mostrar la cantidad de nombres que comiencen con una vocal.
# Datos de entrada: un vector el cual contiene la letra inicial del nombre de cada alumno
# Datos de salida: mostrar la cantidad de nombres que comiencen con una vocal
import numpy as np
cant_alumnos = int(input("Ingrese la cantidad de alumnos: "))
# "U1" la "U" hace referencia a UNICODE y el número "1" a que solo guardará 1 elemento
X = np.empty(cant_alumnos, dtype="U1")  # Declaramos el vector de tipo "U1" (unicode 1 caracter)
cant_vocales = 0
for i in range(0, cant_alumnos):
    print(f"Ingrese la inicial del nombre del {i + 1}° alumno: ", end="")
    X[i] = input()
    if str(X[i]).upper() in "AEIOU":  # "in" compara un valor con los que hay dentro de una cant finita de elementos
        cant_vocales += 1

# Ciclo para mostrar el vector generado
print("El vector generado es el siguiente: ")
for i in range(0, cant_alumnos):
    print(X[i], end=" ")
print(" ")
print("La cantidad de alumnos cuyos nombres empiezan en vocal son: %d" % cant_vocales)
