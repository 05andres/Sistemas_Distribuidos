import socket
print "taller 13"
host="localhost"
puerto = 9998
socket1= socket.socket()

try:
    socket1= socket.socket()
    socket1.connect((host,puerto))
    print  "############## COMUNICACION EN GRUPO ###########"
    print "1. crear grupo"
    print "2. eliminar grupo"
    print "3. consultar grupos"
    numero1= raw_input("ingrese un la operacion que desea realizar y el nombre(eliminado o el nuevo grupo) : ")
    socket1.send(numero1)
    respuesta=socket1.recv(1024)
    print " el resultado de la operacion es :",respuesta
    tiempo = raw_input("presione enter para terminar")
    socket1.close()
except :
    print "NO SE HA ESTABLECIDO UNA CONEXION CON EL SERVIDOR"