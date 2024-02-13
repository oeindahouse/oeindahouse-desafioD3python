#pSubs : valor de la suscripcion por persona
#uSubs : numero de usuarios suscritos
#gTotal : gastos totales del proyecto
#uProyecto : utilidades del proyecto
#uAnterior : utilidades del proyecto año anterior
#calCuociente : cuociente entre año anterior y actual
#calCuociente2 : redondeo del calculo del cuociente


pSubs= float(input("favor ingrese el valor de la subscripcion: "))
uSubs= float(input("ingrese el n° de usuarios: "))
gTotal= float(input("ingrese los gastos totales:"))
uProyecto = int((pSubs*uSubs)-gTotal)
uAnterior= int(input("ingrese Utilidad del año anterior: "))

calCuociente= (float(uAnterior/uProyecto))
calCuociente2= round(calCuociente,2)

print(f"la UTILIDAD DEL PROYECTO del año anterior es {uAnterior}")
print(f"la UTILIDAD DEL PROYECTO del año actual es {uProyecto}")
print(f"el cuociente entre las utilidades de los proyectos es: {calCuociente2}")