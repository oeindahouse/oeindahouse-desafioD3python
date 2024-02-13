#pSubs : valor de la suscripcion por persona
#uSubs : numero de usuarios suscritos
#tipoUsuario : ingrese el tipo de usuario
#gTotal : gastos totales del proyecto
#utiProyecto : utilidades del proyecto

pSubs= int(input("favor ingrese el valor de la subscripcion: "))
uSubs= int(input("ingrese el n° de usuarios: "))
tipoUsuario= str(input("ingrese tipo de usuario [[normal o premium]]: "))
gTotal= int(input("ingrese los gastos totales: "))


if tipoUsuario=="premium":
    pSubs =(pSubs*1.5)
elif tipoUsuario =="normal":
    pSubs = (pSubs*1.0)
else:
    pSubs = (pSubs*1.0)
utiProyecto = ((pSubs*uSubs)-gTotal)

print(f"la UTILIDAD DEL PROYECTO para es {utiProyecto} u.m.")


# tipoUsuario= str(input("ingrese tipo de usuario [[normal o premium]] : ")





