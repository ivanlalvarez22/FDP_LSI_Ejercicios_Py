import numpy as np

"""
7. Una docente de un Colegio privado tiene la siguiente información de los
alumnos de un curso: DNI, Cantidad de Cuotas Abonadas, Cantidad de
Inasistencias a Clases, Nota de Matemática, Nota de Lengua, Nota de Historia,
Nota de Geografía, se pide:

a) Dado el DNI de un alumno informar la cantidad de cuotas adeudadas. En caso
de que el alumno no pertenezca a la institución, mostrar el mensaje
“Alumno Inexistente”.

b) Generar una estructura de datos que posea para cada alumno: DNI, Cantidad de
inasistencias y Categoría. El alumno será categorizado por su promedio de la
siguiente manera:

    Promedio    Categoría
    0 a 5       “Insuficiente”
    6 a 8       “Aprobado”
    9 y 10      “Excelente”

c) A partir de la estructura generada en el ítem (b) se pide dar de baja a los
alumnos con más de 10 inasistencias.
"""
# ------------------------------Sección de Módulos------------------------------


def load_students_info_s(s):
    s[0] = (46345678, 10, 21, 10, 10, 10, 10)
    s[1] = (39548789, 11, 0, 10, 10, 10, 10)
    s[2] = (45666664, 1, 5, 7, 8, 1, 6)
    s[3] = (39548979, 9, 13, 9, 8, 7, 6)
    s[4] = (46456879, 6, 7, 10, 8, 7, 2)
    s[5] = (39656556, 4, 4, 7, 8, 7, 9)
    s[6] = (45648797, 2, 180, 1, 8, 2, 6)
    s[7] = (39545644, 10, 0, 3, 1, 1, 6)
    s[8] = (42546879, 7, 9, 1, 8, 9, 6)
    s[9] = (40546468, 9, 10, 9, 9, 9, 9)
    dim_s = 10
    return dim_s


# ------------------------------------Item a------------------------------------


def student_fees(s, dim_s, dni):
    exist = False
    for i in range(dim_s):
        if s[i]["dni"] == dni:
            exist = True
            print("El alumno con DNI", dni, "debe", s[i]["cuotas"], "cuotas.")
    if not exist:
        print("No existe un alumno con DNI " + str(dni) + ".")


# ------------------------------------Item b------------------------------------


def get_category(note_1, note_2, note_3, note_4):
    average = int((note_1 + note_2 + note_3 + note_4) / 4)
    if 0 <= average <= 5:
        cat = "Insuficiente"
    elif 6 <= average <= 8:
        cat = "Aprobado"
    elif 9 <= average <= 10:
        cat = "Excelente"
    return cat


def categories_students(s, dim_s, c):
    for i in range(dim_s):
        cat = get_category(
            s[i]["nota_matematica"],
            s[i]["nota_lengua"],
            s[i]["nota_historia"],
            s[i]["nota_geografia"]
        )
        c[i]["dni"] = s[i]["dni"]
        c[i]["inasistencias"] = s[i]["inasistencias"]
        c[i]["categoria"] = cat


def print_categories(c, dim_c):
    print("DNI          INASISTENCIAS    CATEGORÍA")
    for i in range(dim_c):
        document = str(c[i]["dni"])
        absences = str(c[i]["inasistencias"])
        category = str(c[i]["categoria"])
        print(
            document + " " * (13 - len(document))
            + absences + " " * (17 - len(absences)) + category
        )


# ------------------------------------Item c------------------------------------


def delete_absent(c, dim_c):
    i = 0
    while i < dim_c:
        if c[i]["inasistencias"] > 10:
            j = i
            while j < dim_c - 1:
                c[j]["dni"] = c[j + 1]["dni"]
                c[j]["inasistencias"] = c[j + 1]["inasistencias"]
                c[j]["categoria"] = c[j + 1]["categoria"]
                j += 1
            dim_c -= 1
        else:
            i += 1
    return dim_c


# ------------------------------------------------------------------------------


def main():
    student = np.dtype(
        [
            ("dni", int),
            ("cuotas", int),
            ("inasistencias", int),
            ("nota_matematica", int),
            ("nota_lengua", int),
            ("nota_historia", int),
            ("nota_geografia", int)
        ]
    )
    student_cat = np.dtype(
        [
            ("dni", int),
            ("inasistencias", int),
            ("categoria", "U12")
        ]
    )
    students_info = np.empty(100, dtype=student)
    students_category = np.empty(100, dtype=student_cat)
    dim_s = load_students_info_s(students_info)
    categories_students(students_info, dim_s, students_category)
    dim_c = dim_s
    print_categories(students_category, dim_c)
    print("")
    dim_c = delete_absent(students_category, dim_c)
    print_categories(students_category, dim_c)


# ------------------------------Programa Principal------------------------------
main()
