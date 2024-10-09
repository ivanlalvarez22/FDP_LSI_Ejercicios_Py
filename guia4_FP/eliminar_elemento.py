import numpy as np

N = 10
inasistencias = np.empty(N,dtype=int)
inasistencias = np.array([12,8,2,0,15,28,4,6,7,10])

#elimino
i = 0
while i < N:
  if inasistencias[i] >= 10:
    j = i
    while j < N-1:
      inasistencias[j] = inasistencias[j+1]
      j += 1
    N -= 1 # actualiza la cantidad de elementos del vector
  else:
    i += 1

#muestro
print("El vector de inasistencias queda: ")
for i in range(N):
  print(inasistencias[i], end=" ")
