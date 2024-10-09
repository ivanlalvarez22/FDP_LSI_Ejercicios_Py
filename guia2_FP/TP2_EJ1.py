# Generar un vector con el mayor valor de cada uno de los 10 pares de números ingresados.
# Datos de entrada: Pares de números. Tipo de dato entero
# Datos de salida: Un vector con el mayor valor de cada número de los pares ingresados
# Estrategia de solución: para cada par de número ingresado, compararlo y guardar el mayor valor en
# el vector

import numpy as np  # Importar la librería numpy
vector = np.empty(10, dtype=int)  # Declaro mi vector

# Ciclo para cargar el vector del elemento 1 al 10
for i in range(0, 10):
    num1 = int(input("Ingresar el primer número: "))
    num2 = int(input("Ingresar el segundo número: "))
    if num1 > num2:
        vector[i] = num1  # Se almacena el valor de num1 en la posición "i" del vector
    else:
        vector[i] = num2  # Se almacena el valor de num2 en la posición "i" del vector

# Ciclo para mostrar el vector
for i in range(0, 10):
    print(vector[i], end=" ")
