import numpy as np
import vectores as vec

def ObtenerDatosObraSocial(codigoObraSocial):
    if codigoObraSocial == 1:
        denominacionObraSocial = "IOSEP     "
        costoInternacionPorPaciente = 200
    elif codigoObraSocial == 2:
        denominacionObraSocial = "SMAUNSE   "
        costoInternacionPorPaciente = 210
    elif codigoObraSocial == 3:
        denominacionObraSocial = "OSPE      "
        costoInternacionPorPaciente = 180
    elif codigoObraSocial == 4:
        denominacionObraSocial = "OSPLA     "
        costoInternacionPorPaciente = 190
    else:
        denominacionObraSocial = ""
        costoInternacionPorPaciente = 0
    return costoInternacionPorPaciente, denominacionObraSocial

def informeObraSocial(v,d):
    codOS= int(input("Ingrese el cód. de OS (9 para PARTICULAR): "))
    totalPac = totalPacientes(codOS,v,d)
    print("Obra Social:",codOS, end="      ")
    costo, denom = ObtenerDatosObraSocial(codOS)
    if costo == 0:
        costo = 1000
        denom = "PARTICULAR"
    print("Nombre:",denom)
    print("Cantidad de Pacientes internados:",totalPac,end="       ")
    print("Costo Total por Internación:",costo*totalPac)
    return None

def totalPacientes(codOS, v, d):
    totalPac = 0
    for i in range(d):
        m, d, c, u = vec.descomponer(v[i])
        if u == codOS:
            cPac = d * 10 + c
            totalPac += cPac
    return totalPac

def informeRecaudacion(v,d):
    tfinalPaciente = 0
    recaudacion = 0
    print("----------- RECAUDACIÓN DEL SANATORIO --------------")
    print("Código  Denominación   Cantidad Internados        Recaudacion Por OSocial")
    for j in range(1,5):
        totalPac = totalPacientes(j,v,d)
        tfinalPaciente += totalPac
        costo, denom = ObtenerDatosObraSocial(j)
        recaudacion += (costo * totalPac)
        print(j,"   ",denom,"               ",totalPac,"                 ",totalPac*costo)
    totalPac = totalPacientes(9,v,d)
    tfinalPaciente += totalPac
    costo = 1000
    denom = "PARTICULAR"
    recaudacion += (costo * totalPac)
    print("     ", denom, "               ",totalPac,"                 ",totalPac*costo)
    print("      Totales:                  ",tfinalPaciente,"                 ",recaudacion)
    return None


def informeRecaudacionOrdenado(v,d,matriz):
    matrizRecaudacion(sanatorio, N, matriz)
    ordenarMatriz(1, matriz, 2, 5)
    tfinalPaciente = 0
    recaudacion = 0
    print("----------- RECAUDACIÓN DEL SANATORIO --------------")
    print("Código  Denominación   Cantidad Internados        Recaudacion Por OSocial")
    for j in range(5):
        totalPac = totalPacientes(matriz[j,0],v,d)
        tfinalPaciente += totalPac
        costo, denom = ObtenerDatosObraSocial(matriz[j,0])
        if costo == 0:
            costo = 1000
            denom = "PARTICULAR"
        recaudacion += (costo * totalPac)
        print(matriz[j,0],"   ",denom,"               ",totalPac,"                 ",totalPac*costo)
    print("      Totales:                  ",tfinalPaciente,"                 ",recaudacion)
    return None



def matrizRecaudacion(v,d,matriz):
    for i in range(5):
        if i == 0:
            costo = 1000
            tp = totalPacientes(9,v,d)
            matriz[i, 0] = 9
        else:
            costo,denom = ObtenerDatosObraSocial(i)
            tp = totalPacientes(i,v,d)
            matriz[i, 0] = i
        matriz[i,1] = tp * costo
    return None

def ordenarMatriz(col, matrizB, dc, df):
    # Ordena la matriz en función de la columna seleccionada.
    i = 0
    while i < df - 1:
        p = i
        j = i + 1
        while j < df:
            if matrizB[j, col] > matrizB[p, col]:
                p = j
            j = j + 1
        k = 0
        while k < dc:
            x = matrizB[p, k]
            matrizB[p, k] = matrizB[i, k]
            matrizB[i, k] = x
            k = k + 1
        i = i + 1

#programa principal

N=6
sanatorio = np.empty(N,dtype=int)
matriz = np.empty((5, 2), dtype=int)
sanatorio = np.array([123,209,153,109,171,259])
#informeObraSocial(sanatorio,N)
#informeRecaudacion(sanatorio,N)
informeRecaudacionOrdenado(sanatorio,N,matriz)
