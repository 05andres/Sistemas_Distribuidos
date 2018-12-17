from datetime import datetime, date, time, timedelta
import calendar
import socket
import sys
import time

def getHoraCliente1():

    #horaServidor = horaServer.split(' ') # guardo la hora del servidor en una lista

    horaUTC = time.localtime() # se define horaUTC obteniendo la hora local
    desface = 20
    minutos  = int(horaUTC[3])*60 + int(horaUTC[4])+ desface # se cambia la hora a minutos con desface
    #print "minutos : "+ str(minutos)


    horaTotal = [int(minutos/60), minutos%60] #se cambian los minutos a horas
    #print "hora Cliente 1 -> " + str(horaTotal)

    return horaTotal #se retorna la diferencia y la hora total

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('localhost',8943))

fin = False 
while not fin:
    print "cliente 2.0"
    time.sleep(3) 
    print "servidor solicitando hora"
    p=getHoraCliente1()
    print p  
    data1=str(p[0])+","+str(p[1])
    s.send(data1)
    recibido = s.recv(1024)#recibe un string con la hora pero en minutos
    num1= recibido[1]+recibido[2]+recibido[3]
    print "hora recibida : "+str(int(num1)/60)+":"+str(int(num1)/60)
s.close()

