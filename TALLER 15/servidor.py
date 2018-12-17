import socket
import math
import thread
import time

#------------------------------------- Servidor ----------------------------------#

#Obtiene la hora del servidor
def getHoraServer():

    horaUTC = time.localtime() # se define horaUTC obteniendo el tiempo local
    horaServer = [horaUTC[3], horaUTC[4]] # se define la hora del server

    #print "Hora Server ->" +str(horaServer)

    return horaServer #se retorna la diferencia y la hora total

def calcularDiferencias(horaCliente, horaServer):

    minutosCliente = int(horaCliente[0])*60  + int(horaCliente[1]) # se cambian las horas del cliente a minutos
    #print "minutos Cliente : "+ str(minutosCliente)

    minutosServer = int(horaServer[0])*60 + int(horaServer[1]) # se cambian las horas del server a minutos
    #print "minutos Servidor : "+ str(minutosServer)

    diferencia = minutosCliente - minutosServer #se hace la diferencia de los minutos
    #print "diferencia : "+ str(diferencia)

    return str(diferencia)

def calcularHoras(diferencias, *horas):

    #horas = horas.split(' ')
    print "horas: "+ str(horas)

    minutos = []
    i = 0
    #print (horas[i][0])
    for hora in horas:
        while(i<len(horas)):
            minutos.append(int(horas[i][0])*60+int(horas[i][1]))
            i += 1

    print "minutos: "+ str(minutos)


    #calculando promedios--------------------------------
    cantidadDiferencias = len(diferencias)
    suma = 0
    for diferencia in diferencias:
        suma = suma + int(diferencia)
    promedio = suma / cantidadDiferencias
    print "promedio : " + str(promedio)

    #calculando nuevas diferencias ----------------------
    nuevasDiferencias = []
    for diferencia in diferencias:
        nuevasDiferencias.append(promedio-int(diferencia))
    print "nuevas Diferencias: "+ str(nuevasDiferencias)

    #calculando nuevas horas ----------------------------
    pos = 0
    nuevasHoras = []
    for nuevaDiferencia in nuevasDiferencias:

        nuevasHoras.append(minutos[pos] + int(nuevaDiferencia))
        pos += 1

    print "nuevas Horas: "+ str(nuevasHoras)

    return nuevasHoras

def obtenerHoraCliente(horaCliente):

    horas = []
    diferencias = [] # cadena de diferencias

    horaServer = getHoraServer() # obtiene la hora del Servidor
    print "hora servidor : "+ str(horaServer)
    diferenciaServer = calcularDiferencias(horaServer, horaServer)
    diferencias.append(diferenciaServer)
    horas.append(str(horaServer))

    
    print "hora cliente 1: "+ str(horaCliente)
    diferenciaCliente1 = calcularDiferencias(horaCliente, horaServer) #calcula diferencia del cliente con respecto al servidor
    diferencias.append(diferenciaCliente1)
    horas.append(str(horaCliente))

    #Grenerando cadena de Horas ---------------------------
    strHoras = ' '.join(horas) #
    bracketLeft = strHoras.replace("[", "")
    bracketRight = bracketLeft.replace ("]", "")
    commas = bracketRight.replace (",", "")

    print commas
    hrs = commas.split(" ")
    print hrs

    i = 0
    horas = []
    while i < len(hrs):
        hourAux = []
        hourAux.append(hrs[i])
        hourAux.append(hrs[i+1])
        horas.append(hourAux)
        i+=2
    #------------------------------------------------------


    print "diferencias: "+str(diferencias)

    nuevasHoras = calcularHoras(diferencias, *horas)
    print nuevasHoras
    return nuevasHoras




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8943))
s.listen(10)
def conecOP(sc,addr):
    hora=[]
    ope=sc.recv(1024)
    enviar=0
    ope2=ope.split(",")
    hora.append(int(ope2[0]))
    hora.append(int(ope2[1]))
    horaclient= obtenerHoraCliente(hora)
        
    sc.send(str(horaclient))
while 1:
   
    
    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    print sc
    thread.start_new_thread(conecOP,(sc,addr))
sc.close()
s.close()