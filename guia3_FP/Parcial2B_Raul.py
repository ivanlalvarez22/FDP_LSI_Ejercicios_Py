import numpy as np
import math
#El vector se compone de numeros que, sus 2 ultimos digitos son los metros cuadrados y el resto al numero d departamento.
#Cada departamento para 25$ expensas por mt2 mas un porcentaje del total.
#Clases:
#Clase C -- Menos de 75mt2 -- 10%
#Clase B -- Entre 75mt2 y 90mt2 -- 7%
#Clase A -- Mas de 90mt2 -- 5%

#a) Desarrolle una funcion que retorne verdadero si todos los departamentos tienen mas de 75mt2
#b) Genere un vector con el monto de las expensas que debe pagar cada departamento que tenga una determinada cant de mt2
#c) Retornar la cantidad de mt2 promedio de los departamentos de clase A
#d) Retornar la cantidad de mt2 y el monto a pagar para un det dep si es de clase C.

#Seccion de modulos.
def mostrarmenu():
    print('------------')
    print('1* Mostrar lista de departamentos.')
    print('2* Verificar 75mt2.')
    print('3* Calcular monto de expensas de un departamento.')
    print('4* Mostrar promedio de mt2 de la Clase A.')
    print('5* Mostrar cantidad de mt2 y monto de un dep de Clase C.')
    print('0* Salir.')



def masde75mt2(vector,dim): 
    masde75 = True
    for i in range(dim):
        if vector[i]%100 <= 75:
            masde75 = False
    return masde75



#Algoritmo principal.
dimension = 5
Metros = np.array([10185,10290,20195,20280,20380],dtype=int)


if masde75mt2(Metros,dimension):    
    print('Todos los departamentos son de mas de 75mt2.')
else:
    print('No todos los departamentos son de mas de 75mt2.')
    

