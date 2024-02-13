#ge : valor de la variable de gravedad
#radioEnm : radio en metros del astro que se deseas calular en el desafio
#velEsc : velocidad de escape del astro


import math
from math import sqrt

#ge= float(9.8)
ge= float(input("ingrese el valor general de gravedad -9.8-, utilzada para el caso: "))
radioEnm= float(input("ingrese radio en metros"))
velEsc= round(sqrt((2*(ge*radioEnm))),1)
print (f"La velocidad de escape es {velEsc} [m/s]")



