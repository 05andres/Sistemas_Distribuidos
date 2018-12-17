import socket
import math
import thread


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8927))
s.listen(10)

def sock(ip):
    cadena="OK"
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.connect(('localhost',puer))
	s.send(cadenA)
	recibido = s.recv(1024)
	print "---------------------------------"
	print "reaultado recibido del  servidor = " ,recibido
	print "---------------------------------"
	s.close()
	return recibido

def conecOP(sc,addr):
    ope=sc.recv(1024)
    enviar=0
    separacion=ope.split(" ")
    numero1=separacion[0]
    numero2=separacion[2]
    operacion=separacion[1]
    if operacion == "+":
        enviar= sock(9094,ope)
    elif operacion == "-":
        enviar =sock(9093,ope)
    elif operacion == "*":
        enviar =sock(9092,ope)
    elif operacion == "/":
        enviar =sock(9091,ope)
    elif operacion == "E":
        enviar =sock(9090,ope)
    elif operacion == "raiz":
        enviar =sock(9089,ope)
    elif operacion == "log":
        enviar =sock(9088,ope) 
    sc.send(str(enviar))
print "respondiendo..."

while 1:
    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(conecOP,(sc,addr)) 
sc.close()
s.close()