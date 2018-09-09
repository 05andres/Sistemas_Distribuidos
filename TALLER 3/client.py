import socket
print "taller 1"
host="localhost"
puerto = 9998
socket1= socket.socket()
def sock(puer,cadena):
	try:
			print "enviendo datos"
			puerto=int(puer)
			host="localhost"
			socket1= socket.socket()
			socket1.connect((host,puerto))
			socket1.send(cadena)
			respuesta=socket1.recv(1024)
			socket1.close()
			return  respuesta
	except :
		print "NO SE HA ESTABLECIDO UNA CONEXION CON EL SERVIDOR"

try:
    socket1= socket.socket()
    socket1.connect((host,puerto))
    numero1= raw_input("ingrese un la operacion que desea realizar : ")
    socket1.send(numero1)
    respuesta=socket1.recv(1024)
    result=respuesta.split(",")
    numeros=result[2]+" "+result[3]
    print numeros
    result1=sock(result[0],numeros)
    print " el resultado de la operacion es : ",result1

    tiempo = raw_input("presione enter para terminar")
    socket1.close()
except :
    print "NO SE HA ESTABLECIDO UNA CONEXION CON EL SERVIDOR"