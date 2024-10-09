# A  partir  de una matriz  B de N  x N  generar y mostrar la  traspuesta de  dicha matriz
# (la  traspuesta de  una  matriz consiste en la transformación de las filas en columnas y de las columnas en filas).
import numpy as np
import random

# Módulos
def cargarandom(Matriz, dim):
    for i in range(dim):
        for j in range(dim):
            Matriz[i, j] = random.randrange(0, 100)

def mostrarMatriz(Matriz, dim):
    for i in range(dim):
        for j in range(dim):
            print(Matriz[i, j], end=" ")
        print("")

def Generar_Traspuesta(matriz, dim):
    for i in range(dim):
        for j in range(dim):
            if j > i:
                aux = matriz[i, j]
                matriz[i, j] = matriz[j, i]
                matriz[j, i] = aux
    return None

# Programa principal
Matriz = np.empty((5,5), dtype="int")
cargarandom(Matriz, 5)
mostrarMatriz(Matriz, 5)
Generar_Traspuesta(Matriz, 5)
print("La matriz traspuesta es la siguiente: ")
mostrarMatriz(Matriz, 5)
