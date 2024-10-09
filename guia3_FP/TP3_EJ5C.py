import numpy as np

#   RecaudacionDenominacion
#   Descripcion: calcula la recaudacion por obra social y si el pacientes es particular
#   Datos De entrada: costoInternacionPorPaciente,denominacionObraSocial,pacientes
#   Datos de Salida: recaudacionPorObraSocial,denominacionObraSocial
def RecaudacionDenominacion(costoInternacionPorPaciente,denominacionObraSocial,pacientes):
    if costoInternacionPorPaciente == 0:
        recaudacionPorObraSocial = 1000 * pacientes
        denominacionObraSocial = 'PARTIC.'
    else:
        recaudacionPorObraSocial = costoInternacionPorPaciente * pacientes
    return recaudacionPorObraSocial,denominacionObraSocial

#   DescomposicionDeCodigo
#   Descripcion: descompone el codigo
#   Datos de Entrada: datosDelSanatorio
#   Datos de Salida:codigoObraSocial,pacientes
def descomponerCodigo(datosDelSanatorio):
    codigoObraSocial = datosDelSanatorio % 10
    pacientes = int(datosDelSanatorio / 10)
    return codigoObraSocial,pacientes

#     ----------------  ITEM A -------------------

#   ObtenerDatosObraSocial
#   Descripción: determina la denominación y el costo de internación por paciente para una determinada obra
#       social. En caso de que el código no exista, se deberá retornar costo cero y denominación vacía (“”)
#   Datos de Entrada: codigoObraSocial
#   Datos de Salida o Resultados: costoInternacionPorPaciente, denominacionObraSocial
def ObtenerDatosObraSocial(codigoObraSocial):

    if codigoObraSocial == 1:
        denominacionObraSocial = 'IOSEP  '
        costoInternacionPorPaciente = 200

    elif codigoObraSocial == 2:
        denominacionObraSocial = 'SMAUNSE'
        costoInternacionPorPaciente = 210

    elif codigoObraSocial == 3:
        denominacionObraSocial = 'OSPE   '
        costoInternacionPorPaciente = 180

    elif codigoObraSocial == 4:
        denominacionObraSocial = 'OSPLA  '
        costoInternacionPorPaciente = 190

    else:
        denominacionObraSocial = 'PARTIC.'
        costoInternacionPorPaciente = 1000

    return costoInternacionPorPaciente, denominacionObraSocial

#   MuestraInformacion
#   Descripcion: Obtiene la inforamcion necesaria para mostrarla
#   Datos de Entrada: datosDelSanatorioSur,dim
#   Datos de Salida: ----
def MuestraInformacion(datosDelSanatorio,dim):
    codigo = int(input(f'Ingrese el codigo:'))
    while codigo < 99 or codigo >999:
        print(f'El codigo {codigo} es incorrecto')
        codigo = int(input(f'Ingrese nuevamente un codigo'))
    for i in range(dim):
        if datosDelSanatorio[i] == codigo:
            codigoObraSocial, pacientes = descomponerCodigo(datosDelSanatorio[i])
            print(f'\t\t---En la posicion {i + 1}---')
            print(f'Obra social: {codigoObraSocial}')
            print(f'Cantidad de pacientes internados: {pacientes}')
            costoInternacionPorPaciente, denominacionObraSocial = ObtenerDatosObraSocial(codigoObraSocial)
            recaudacionPorObraSocial,denominacionObraSocial=RecaudacionDenominacion(costoInternacionPorPaciente, denominacionObraSocial, pacientes)
            print(f'Nombre: {denominacionObraSocial}')
            print(f'Costo Total por inernaciónes: ${recaudacionPorObraSocial}')
    return None

#     ----------------  ITEM B -------------------

#   MuestraInfromacionSanatorioSur
#   Descripcion: Muestra la informacion del sanatorio del sur
#   Datos de Entrada: datosDelSanatorio,dim
#   Datos de Salida: -----
def MuestraInfromacionSanatorioSur(datosDelSanatorio,dim):
    print(f'---------------------------------------------------------------------------')
    print(f'\t\t\t♦♦♦  Recaudacion Del Sanatorio  ♦♦♦')
    print('---------------------------------------------------------------------------')
    print('\tCodigo\tDenominacion\tCantidad Internados\tRecaudacion Por Obra Social')
    for i in range(dim):
        codigoObraSocial, pacientes = descomponerCodigo(datosDelSanatorio[i])
        costoInternacionPorPaciente, denominacionObraSocial = ObtenerDatosObraSocial(codigoObraSocial)
        recaudacionPorObraSocial,denominacionObraSocial=RecaudacionDenominacion(costoInternacionPorPaciente, denominacionObraSocial, pacientes)
        print(f'\t{codigoObraSocial}\t\t{denominacionObraSocial}\t\t\t{pacientes}\t\t\t\t\t${recaudacionPorObraSocial}')
    return None

#     ----------------  ITEM C -------------------

#   OrdenDeRecuadacion
#   Descripcion: ordena los datos de la recaudacion de forma descendente
#   Datos de Entrada:
#   Datos de salida:
def InfoDelSanatorio(datosDelSanatorio,dim,informacionDelSanatorioSur):

    for i in range(dim):
        codigoObraSocial, pacientes = descomponerCodigo(datosDelSanatorio[i])
        costoInternacionPorPaciente, denominacionObraSocial = ObtenerDatosObraSocial(codigoObraSocial)
        recaudacionPorObraSocial, denominacionObraSocial = RecaudacionDenominacion(costoInternacionPorPaciente, denominacionObraSocial, pacientes)
        informacionDelSanatorioSur[i][0] = codigoObraSocial
        informacionDelSanatorioSur[i][1] = 0
        informacionDelSanatorioSur[i][2] = pacientes
        informacionDelSanatorioSur[i][3] = recaudacionPorObraSocial
    return None

#   OrdenacionDescendente
#   Descripcion: Ordena los elementos con respecto a la recaudacion por obra social
#   Datos de Entrada: informacionDelSanatorioSur
#   Datos de Salida: informacionDelSanatorioSur
def OrdenacionDescendente(informacionDelSanatorioSur,dim):
    i = 0
    col = 4-1
    while i <= dim - 1:
        p = i
        #j=i+1
        for j in range(0, dim):
            if informacionDelSanatorioSur[j, col] > informacionDelSanatorioSur[p, col - 1]:
                p = j
        for k in range(0, 4):
            aux = informacionDelSanatorioSur[p, k]
            informacionDelSanatorioSur[p, k] = informacionDelSanatorioSur[i, k]
            informacionDelSanatorioSur[i, k] = aux
        i += 1
    return informacionDelSanatorioSur

#   MuestraSanatorioSur
#   Descripcion: muestra la informacion del sanatorio del sur
#   Datos de entrada: informacionDelSantorioSur, TotalDePacientes,MontoTotal,dim
#   Datos de salida:
def MuestraSanatorioSur(informacionDelSanatorioSur,dim,datosDelSanatorio):
    OrdenacionDescendente(informacionDelSanatorioSur, dim)
    totalDePacientes = 0
    montoTotal = 0
    print(f'---------------------------------------------------------------------------')
    print(f'\t\t\t♦♦♦  Recaudacion Del Sanatorio  ♦♦♦')
    print('-' * 69)
    print('\tCodigo\tDenominacion\tCantidad Internados\tRecaudacion Por Obra Social')
    print('-' * 69)

    # Recorrer los codigos de las obras sociales
    for cod in range(1, 5):
        cantidadTotalInternados = 0
        for i in range(dim):
            codigoObraSocial, pacientes = descomponerCodigo(datosDelSanatorio[i])
            if (codigoObraSocial == cod):
                cantidadTotalInternados = cantidadTotalInternados + pacientes

        costoInternacionPorPaciente, denominacionObraSocial = ObtenerDatosObraSocial(cod)
        recaudacionPorObraSocial, denominacionObraSocial = RecaudacionDenominacion(costoInternacionPorPaciente,
                                                                                   denominacionObraSocial, pacientes)

        print(f'\t{cod}\t\t{denominacionObraSocial}\t\t\t{cantidadTotalInternados}\t\t\t\t\t${recaudacionPorObraSocial}')
        print()


        totalDePacientes = totalDePacientes + int(cantidadTotalInternados)
        montoTotal = montoTotal + int(recaudacionPorObraSocial)

    # Calculo los codigos del 5 al 9 como particulares
    cantidadTotalInternados = 0
    for cod in range(5, 10):
        for i in range(dim):
            codigoObraSocial, pacientes = descomponerCodigo(datosDelSanatorio[i])
            if (codigoObraSocial == cod):
                cantidadTotalInternados = cantidadTotalInternados + pacientes

        costoInternacionPorPaciente, denominacionObraSocial = ObtenerDatosObraSocial(cod)
        # recaudacionPorObraSocial, denominacionObraSocial = RecaudacionDenominacion(costoInternacionPorPaciente,
        #                                                                            denominacionObraSocial, pacientes)

    recaudacionPorObraSocial = cantidadTotalInternados * costoInternacionPorPaciente
    print(f'\t \t\t{denominacionObraSocial}\t\t\t{cantidadTotalInternados}\t\t\t\t\t${recaudacionPorObraSocial}')
    print()

    print(' ' * 7 + 'Totales' + ' ' * 30 + str(totalDePacientes) + ' ' * 20 + '$',str(montoTotal))
    print('-' * 69)
    print('-' * 69)
    return None

#   MenuDeOpciones
#   Descripcion: muestra las opciones al usuario
#   Datos de Entrada: ---
#   Datos de Salida: ---
def MenuDeOpciones():
    print('1. -Mostrar la Informacion Segun un determinado codigo')
    print('2. -Muestra la informacion del Sanatorio Del Sur')
    print('3. -Muestra la Informacion ordenada segun lo Recaudado por Obra Social ')
    print('0. -Finalizar el Programa')



#       Programacion Principal
datosDelSanatorioSur = np.array([123,209,153,109,171,254,402,306,104],dtype=int)
dim = 9
informacionDelSanatorioSur = np.empty([dim,4],dtype=int)
MenuDeOpciones()
print('')
op = int(input(f' opcion-->  '))
while op != 0 :
    if op == 1:
        #         -----  Item A  -------            #
        MuestraInformacion(datosDelSanatorioSur, dim)
    elif op == 2:
        #         -----  Item B  -------            #
        MuestraInfromacionSanatorioSur(datosDelSanatorioSur,dim)
    elif op ==3:
        #       -----   Item C  ------              #
        InfoDelSanatorio(datosDelSanatorioSur,dim,informacionDelSanatorioSur)
        MuestraSanatorioSur(informacionDelSanatorioSur, dim,datosDelSanatorioSur)
    print('')
    op = int(input(f' opcion-->  '))
