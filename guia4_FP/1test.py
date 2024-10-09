# Apellido y Nombre del Alumno:
# Numero de Documento:
# Legajo:
import numpy as np

tipo_fecha = np.dtype([
    ('mes', int),
    ('anio', int)
    ])

tipo_proyecto = np.dtype(
    [('codigo_proyecto', int),
     ('nombre_cliente','U30'),
     ('tipo_proyecto','U1'), #{'D'-Departamento, 'C'-Casa, 'E'-Edificio}
     ('duracion', int),
     ('fecha_inicio', tipo_fecha),
     ('costo', float),
     ('estado_proyecto', int) # { 0 - En Ejecucion, 1 - Terminado }
     ])

#Nombre del módulo: CargarProyectos
#Descripción: realiza la carga de los proyectos de la empresa.
#Datos de Entrada:
#Datos de Salida:
def cargar_proyectos(proyectos):
    dim_proyectos = 6
    proyectos[0] = (345, "Belen Garcia", 'C', 25, (7, 2018), 55000, 1)
    proyectos[1] = (346, "Carlos Trejo", 'E', 40, (8, 2018), 8000000, 0)
    proyectos[2] = (478, "Luis Cano", 'C', 18, (9, 2019), 45000, 1)
    proyectos[3] = (265, "Ana Luna", 'E', 24, (2, 2020), 3000000, 0)
    proyectos[4] = (546, "Sofia Lopez", 'C', 4, (4, 2021), 50000, 1)
    proyectos[5] = (723, "Juan Perez", 'E', 18, (10, 2021), 2500000, 0)
    return dim_proyectos

#Nombre del Módulo: DescripcionTipoProyecto
#Descripción: retorna la descripcion o denominacion de un tipo de Proyecto.
#Datos de Entrada:
#Datos de Salida:
def descripcion_tipo_proyecto(tipo_proyecto):
    descripcion=""
    if tipo_proyecto == 'D':
        descripcion="Departamento"
    elif tipo_proyecto == 'C':
        descripcion="Casa"
    elif tipo_proyecto == 'E':
        descripcion="Edificio"
    return descripcion

#Nombre del Módulo: ObtenerDatosTipoProyecto
#Descripción: determina la cantidad y el costo de todos los proyectos para un determinado tipo de proyecto
# y su denominación. En caso de que el código no exista, se deberá retornar cantidad cero, costo cero y
# denominación vacía (“”)
#Datos de Entrada: tipoDeProyecto
#Datos de Salida: CantidadProyectos, CostoTodosProyectos, DenominacionTipoDeProyecto

#Nombre del Módulo: FechaFinalizacion
#Descripción: determina el mes y el anio de finalizacion de un proyecto
#Datos de Entrada: fechaInicio, duracionProyecto
#Datos de Salida: fechaFin
def fecha_finalizacion(fecha_inicio, duracion_proyecto):
    fecha_fin = np.empty(1,dtype=tipo_fecha)
    anios_proyecto = duracion_proyecto / 12
    resto_meses_proyecto = duracion_proyecto % 12
    anio_finalizacion = fecha_inicio['anio'] + anios_proyecto
    mes_finalizacion = fecha_inicio['mes'] + resto_meses_proyecto
    if mes_finalizacion>12:
        mes_finalizacion = mes_finalizacion - 12
        anio_finalizacion = anio_finalizacion + 1

    fecha_fin['mes'] = mes_finalizacion
    fecha_fin['anio'] = anio_finalizacion
    return fecha_fin


############ PROGRAMA PRINCIPAL ###################
MAX_PROYECTOS = 20
empresa = np.empty(MAX_PROYECTOS,dtype=tipo_proyecto)
