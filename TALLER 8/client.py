import socket
import sys
 
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('localhost',8927))


data1 = raw_input("Escriba una operacion valida : ")
s.send(data1)
recibido = s.recv(1024)
print "---------------------------------"
print "reaultado recibido del  servidor = " ,recibido
print "---------------------------------"


s.close()