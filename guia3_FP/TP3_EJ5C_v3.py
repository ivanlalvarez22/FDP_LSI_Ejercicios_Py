# El vector P (N) contiene números de 3 cifras, en donde las dos primeras indican la cantidad de internados
# en el Sanatorio Sur y el último dígito el código de obra social.
#
# [123 209 153 109 171 259 ... ]     '123' indica '12' pacientes con código de obra social '3'.
#
# Además, el Sanatorio trabaja solamente con las obras sociales que figuran en la siguiente tabla:
#
# Código de Obra Social      Denominación      Costo de Internación Por Paciente
# 1                          IOSEP             200
# 2                          SMAUNSE           210
# 3                          OSPE              180
# 4                          OSPLA             190
# Se pide:
#
# a) Para un código de obra social determinado, mostrar la información de acuerdo al siguiente formato:
#
# Obra Social: 3                                 Nombre: OSPE
# Cantidad de Pacientes internados: 27           Costo Total por Internación: $4860
#
# Si el sanatorio no trabaja con el código de la obra social significa que nos encontramos en presencia de
# un paciente particular, el cual deberá pagar de contado un monto de $1000 como Costo de Internación por Paciente.
# Nota: para su realización debe convocar al módulo ObtenerDatosObraSocial, cuya descripción es la siguiente:
#
# Nombre del Módulo: ObtenerDatosObraSocial
# Descripción: determina la denominación y el costo de internación por paciente para una determinada obra social.
# En caso de que el código no exista, se deberá retornar costo cero y denominación vacía ("")
# Datos de Entrada: codigoObraSocial
# Datos de Salida o Resultados: costoInternacionPorPaciente, denominacionObraSocial
#
# b) Mostrar un informe de la recaudación del Sanatorio, debiendo el mismo cumplir con el siguiente formato:
#
#                               RECAUDACION DEL SANATORIO
# Código      Denominación       Cantidad Internados      Recaudacion Por O. Social
# 1           IOSEP              17                      $ 3400,00
# 2           SMAUNSE            0                       $ 0,00
# .....       .......	         ..                       ......
#             PARTICULARES       55                      $ 55000,00
#             Totales            89                      $ 63260,00
#
# c) Proponga una solución para el ítem b) en la cual se muestre el informe con el mismo formato, pero ordenado en
# forma descendente por lo Recaudado por Obra Social
