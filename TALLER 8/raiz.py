import socket
import sys
import thread
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9089))
s.listen(10)

def conecOP(sc,addr):
    ope=sc.recv(1024)
    enviar=0
    separacion=ope.split(" ")
    numero1=separacion[0]
    numero2=separacion[2]
    operacion=separacion[1]
    exp=float(1/(float(numero1)))
    enviar= float(numero2)**exp
    sc.send(str(float(enviar)))

print "respondiendo..."

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(conecOP,(sc,addr))
    
sc.close()
s.close()