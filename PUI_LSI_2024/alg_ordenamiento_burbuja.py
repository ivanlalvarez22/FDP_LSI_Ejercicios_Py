import numpy as np

# Definir el tamaño del array y los valores iniciales
A = np.array(
    [5, 6, 3, 1, 4], dtype=int
)

print("Array inicial:", A)

n = len(A)
b = 0
while b != 1:
    b = 1
    for i in range(n - 1):
        if A[i] > A[i + 1]:  # Condición SI A(I) > A(I+1)
            w = A[i]
            A[i] = A[i + 1]
            A[i + 1] = w
            b = 0

print("Array ordenado:", A)
