# Actualizar los salarios de 15 empleados de una fábrica, teniendo en cuenta los
# porcentajes de aumento establecidos en un nuevo convenio:
#  Salario Actual             Aumento según Convenio
# Entre 5000 y 9000                   15%
# Entre 9001 y 15000                  10%
# Más de 15000                        5%
# luego mostrar el salario actual y el nuevo salario de cada empleado.

import numpy as np
vector = np.empty(15, dtype=float)
vector_aumento = np.empty(15, float)
# Ciclo para cargar el vector
i = 0
while i < 15:
    print(f"Ingresar el sueldo del {i + 1} empleado: ", end="")
    vector[i] = int(input())
    i += 1
# Ciclo para mostrar el vector
i = 0
print("El vector salario generado es el siguiente: ")
while i < 15:
    print(vector[i], end=" ")
    i += 1
print(" ")
# Ciclo para calcular el aumento de salario
i = 0
while i < 15:
    if 5000 <= vector[i] <= 9000:
        vector_aumento[i] = vector[i] * 1.15
    elif 9001 <= vector[i] < 15000:
        vector_aumento[i] = vector[i] * 1.1
    elif vector[i] > 15000:
        vector_aumento[i] = vector[i] * 1.05
    else:
        vector_aumento[i] = vector[i]
    i += 1
# Ciclo para mostrar el vector aumento
i = 0
print("El vector aumento es: ")
while i < 15:
    print(vector_aumento[i], end=" ")
    i += 1
print(" ")
