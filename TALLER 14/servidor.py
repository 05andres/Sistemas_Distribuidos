import socket
import math
import thread
import time

clientes=[]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8943))
s.listen(10)
def conecOP(sc,addr):
    
    ope=sc.recv(1024)
    clientes.append(ope)
    enviar=0
    print clientes
    if ope == "solicitando hora":
        ho= time.strftime("%X")
        lis= ho.split(":")
        strHO=str(lis[0]+","+lis[1]+","+lis[2])
        enviar=strHO
        
    else:
        enviar="Esperando solitidd de hora"
        
    
    sc.send(str(enviar))
while 1:
   
    
    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    print sc
    thread.start_new_thread(conecOP,(sc,addr))
    print clientes
sc.close()
s.close()