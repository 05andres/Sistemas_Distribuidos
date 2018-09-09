import funciones
# Print list of available methods 
fin=False  
while not fin: 
	numero1= raw_input("ingrese un la operacion que desea realizar : ")
	lista=numero1.split(" ")
	respuesta=funciones.operacion(lista[0],lista[1],lista[2])
	respuesta2=respuesta.split(" ")
	respuesta3=funciones.resultado(lista[0],respuesta2[1],lista[2],respuesta2[0])
	print " el resultado de la operacion es :",respuesta3
	continuar= raw_input("si desea continuar operando ingrese la tecla S de lo contrario N : ")
	if continuar == 'N':
		fin=True
	else :
		fin=False



