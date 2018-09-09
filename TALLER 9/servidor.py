import socket
import math
import thread


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8927))
s.listen(10)
def conecOP(sc,addr):
    ope=sc.recv(1024)
    enviar=0
    separacion=ope.split(" ")
    print len(separacion)
    if len(separacion) == 3:
        numero1=separacion[0]
        numero2=separacion[2]
        operacion=separacion[1]
        if operacion == "+":
            enviar="9094"+" "+ope
        elif operacion == "-":
            enviar ="9093"+" "+ope
        elif operacion == "*":
            enviar ="9092"+" "+ope
        elif operacion == "/":
            enviar ="9091"+" "+ope
        elif operacion == "E":
            enviar ="9090"+" "+ope
        elif operacion == "raiz":
            enviar ="9089"+" "+ope
        elif operacion == "log":
            enviar ="9088"+" "+ope
        else:
            enviar="ingrese una operacion valida"
        
    else:
        enviar="error de sintaxis"
    sc.send(str(enviar))
print "respondiendo..."

while 1:
    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(conecOP,(sc,addr)) 
sc.close()
s.close()