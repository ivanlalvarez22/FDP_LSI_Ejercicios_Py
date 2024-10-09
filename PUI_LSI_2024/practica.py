import numpy as np

# Definir el tamaño del array y los valores iniciales
A = np.array(
    [1, 2, 3, 4, 5, 6, 0], dtype=int
)

num = int(input("Ingrese un nro: "))

print(f"Array desordenado")
print(A)

n = len(A) - 1
b = 0
i = 0
while i < n and b == 0:
    if num < A[i]:
        for j in range(n, i, -1):
            A[j] = A[j - 1]
        A[i] = num
        b = 1
    i += 1
if b == 0:
    A[n] = num



print(f"Array ordenado")
print(A)
