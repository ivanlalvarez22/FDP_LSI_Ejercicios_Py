import random

def cargarVector(dim, v):
    """
    Carga elementos enteros en un vector
    :param dim: tipo entero
    :param v: tipo vector de enteros
    :return: None
    """
    for i in range(dim):
        v[i] = int(input("Ingrese un valor: "))
    return None

def Mayor(Vector, dim):
    """
    Devuelve el mayor elemento de un vector de enteros
    :param Vector: vector de enteros
    :param dim: dimensión del vector. Número entero
    :return: el mayor elemento entero
    """
    mayor = -1
    for i in range(dim):
        if Vector[i] > mayor:
            mayor = Vector[i]
    return mayor


def Menor(Vector, dim):
    """

    :param Vector:
    :param dim:
    :return:
    """
    menor = 9999999999999
    for i in range(dim):
        if menor > Vector[i]:
            menor = Vector[i]
    return menor

def MayoryMenor(Vector, dim):
    mayor = -1
    menor = 99999999999999
    for i in range(dim):
        if mayor < Vector[i]:
            mayor = Vector[i]

        if menor > Vector[i]:
            menor = Vector[i]

    return mayor, menor

def insert(vector, dim):
    num = int(input("\nElemento a insertar: "))
    is_insert = False
    i = 0
    while i < dim and not is_insert:
        if num < vector[i]:
            j = dim - 1
            while j >= i:
                vector[j + 1] = vector[j]
                j -= 1
            vector[i] = num
            dim += 1
            is_insert = True
        else:
            i += 1
    if not is_insert:
        vector[i] = num
        dim += 1
    return dim, num

def cargarEstatica(v):
    v[0] = 14
    v[1] = 12
    v[2] = 42
    v[3] = 23
    v[4] = 82
    v[5] = 54
    v[6] = 67
    v[7] = 99
    v[8] = 76
    v[9] = 15
    dim = 10
    return dim

def ordenarVector(v,dim):
    i = dim
    b = 1
    while b != 0:
        b = 0
        j = 0
        while j < i - 1:
            # AQUI en el if debo cambiar el signo si quiero que el ordenamiento sea ascendente o descendente
            if v[j] > v[j + 1]:
                aux = v[j]
                v[j] = v[j + 1]
                v[j + 1] = aux
                b = 1
            j += 1
        i -= 1
    return None

def mostrarVector(v,dim):
    print("[", end="")
    for i in range(dim):
        if i < dim - 1:
            print(v[i], end=", ")
        else:
            print(v[i], end="]\n")
    return None

def cargarandom(Vector, dim):
    for i in range(dim):
        Vector[i] = random.randrange(0, 100)

def estaEnVectorLineal(elemento,vector,dim):
    #Búsqueda lineal
    b = False
    for i in range(dim):
        if vector[i] == elemento:
            b = True
    return b


def estaEnVectorBinaria(elemento, vector, dim):
    ordenarVector(vector,dim)
    p = 0
    u = dim - 1
    m = int((p + u) / 2)
    while p <= u and elemento != vector[m]:
        if elemento < vector[m]:
            u = m - 1
        else:
            p = m + 1
        m = int((p + u) / 2)
    if p <= u:
        b = True
    else:
        b = False
    return b
