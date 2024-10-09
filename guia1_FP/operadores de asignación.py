# Para poder usar operadores de asignación es necesario darle un valor a nuestra variable
# porque esto nos sirve para aumentar lo que ya tenemos, en caso de no asignar un valor
# python no entendería a qué valor queremos operarlo
a = 0
# al valor a que vale 0 lo incrementamos 5 unidades
a += 5
# a las 5 unidades le restamos 4
a -= 4
# ahora al resultado anterior que era 1 lo multiplicamos por 9
a *= 9
# seguidamente lo dividimos entre 3
a /= 3
# 9 / 3 = 3, a ese 3 lo elevamos al exponente 3 nos dará 27
a **= 3
# ahora al 27 lo dividimos entre 2 y obtenemos el módulo o resto de la misma que será 1
a %= 2

print(a)
