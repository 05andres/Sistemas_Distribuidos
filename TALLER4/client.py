import funciones


# Print list of available methods 
fin=False  
while not fin: 
	numero1= input("ingrese un la operacion que desea realizar : ")
	lista=numero1.split(" ")
	respuesta=funciones.operacion(lista[0],lista[1],lista[2])
	print (" el resultado de la operacion es :",respuesta)
	continuar= input("si desea continuar operando ingrese la tecla S de lo contrario N : ")
	if continuar == 'N':
		fin=True
	else :
		fin=False



