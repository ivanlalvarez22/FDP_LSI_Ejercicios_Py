import numpy as np

N = 10
vectorA = np.empty(N, dtype=int)
vectorA = np.array([28, 25, 24, 20, 15, 13, 11, 6, 5, 3, 0, 0, 0, 0, 0])

#insertar
c = 1
cant = int(input("Ingrese la cantidad de elementos a insertar en el vector: "))
while c <= cant:
  num = int(input("Ingrese un nro: "))
  i = 0
  b = 0
  while i < N and b == 0:
    if vectorA[i] < num:
      j = N
      while j >= i:
        vectorA[j+1] = vectorA[j]
        j -= 1
      N += 1
      vectorA[i] = num
      b = 1
    else:
      i += 1
  if b == 0:
    vectorA[i] = num
    N += 1
  c += 1


#muestro
print("El vector de inasistencias queda: ")
for i in range(N):
  print(vectorA[i], end=" ")
