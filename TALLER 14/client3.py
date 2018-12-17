from datetime import datetime, date, time, timedelta
import calendar
import socket
import sys
import time

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8942))
s.connect(('localhost',8943))

fin = False 
while not fin:
    time.sleep(3) 
    data1="solicitando hora"
    print data1
    s.send(data1)
    recibido = s.recv(1024)
    lis=recibido.split(",")
    hora=int(lis[0])
    min2=int(lis[1])
    seg=int(lis[2])
    seg = seg + 1
    if seg == 60 and min2 != 60:
        min2 = min2 +1
        seg = 0
    if seg == 0 and min2 == 60:
        min2 = 0
        hora = hora + 1
    if seg == 0 and min2 == 0 and hora == 24:
        hora == 0
        time.sleep(1) 
    print str(hora)  + ":" + str(min2) + ":" + str(seg)

s.close()