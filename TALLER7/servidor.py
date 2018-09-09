import socket
import sys
import thread
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8943))
s.listen(10)

def conecOP(sc,addr):
    ope=sc.recv(1024)
    enviar=0
    separacion=ope.split(" ")
    numero1=separacion[0]
    numero2=separacion[2]
    operacion=separacion[1]
    if operacion == "+":
        enviar= int(numero1)+int(numero2)
    elif operacion == "-":
        enviar =int(numero1)-int(numero2)
    elif operacion == "*":
        enviar =int(numero1) *int(numero2)
    elif operacion == "/":
        enviar =float(float(numero1) / float(numero2))
    elif operacion == "E":
        enviar = int(numero1)**int(numero2)
    elif operacion == "raiz":
        exp=float(1/(float(numero1))) 
        enviar = float(numero2)**exp
    elif operacion == "log":
        enviar = math.log(float(numero1),(float(numero2)))
    
    sc.send(str(int(enviar)))

print "respondiendo..."

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(conecOP,(sc,addr))
    
sc.close()
s.close()