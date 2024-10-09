import numpy as np

# Definir el tamaño inicial del array y los valores iniciales
A = np.array([3, 6, 8, 12, 45, 0])  # Aumentar el tamaño inicial para permitir espacio adicional

NUM = 77

# Mostrar el array A antes de la inserción
print("Array A antes de la inserción:", A)

# Inicializar variables
N = len(A) - 1  # Ajustar N para no considerar el espacio adicional añadido
B = 0
I = 0
# Buscar la posición de inserción y desplazar elementos
while I < N and B == 0:
    if NUM < A[I]:
        # Desplazar elementos hacia la derecha para hacer espacio para NUM
        for J in range(N, I, -1):
            A[J] = A[J - 1]
        # Insertar NUM en la posición I
        A[I] = NUM
        B = 1
    I += 1

# Si NUM es mayor que todos los elementos en A, se inserta al final
if B == 0:
    A[N] = NUM

# Mostrar el array A después de la inserción
print("Array A después de la inserción:", A)
