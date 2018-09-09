import socket
import sys
 

def sock(puer,cadena):
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.connect(('localhost',int(puer)))
	s.send(cadena)
	recibido = s.recv(1024)
	print "---------------------------------"
	print "reaultado recibido del  servidor = " ,recibido
	print "---------------------------------"
	s.close()
	return recibido

try:
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    data1 = raw_input("Escriba una operacion valida : ")
    s.connect(('localhost',8927)) 
    s.send(data1)
    recibido = s.recv(1024)
    separacion = recibido.split(" ")
    print len(separacion)
    separacion1 = separacion[1]+" "+separacion[2]+" "+separacion[3]
    print separacion,separacion1
    result=sock(separacion[0],separacion1)
    print "---------------------------------"
    print "reaultado recibido del  servidor = " ,result
    print "---------------------------------"
except:
    print " Escriba una operacion valida"

s.close()