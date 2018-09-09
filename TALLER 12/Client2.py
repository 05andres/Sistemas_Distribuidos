from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import time
import funciones,funciones2

class MyFuncs():
	def rest(self):
		s =9980
		opr="rest"
		return str(s)+" "+opr
	def div(self):
		s =9995
		opr="div"
		return str(s)+" "+opr
	def sum(self):
		s =9997
		opr="sum"
		return str(s)+" "+opr
	def mult(self):
		s =9996
		opr="mult"
		return str(s)+" "+opr
	def exp(self):
		s =9990
		opr="exp"
		return str(s)+" "+opr
	def raiz(self):
		s =9993
		opr="raiz"
		return str(s)+" "+opr
	def log(self):
		s =9992
		opr="log"
		return str(s)+" "+opr
class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):
    def __init__(self):
         threading.Thread.__init__(self)
         self.localServer = SimpleThreadedXMLRPCServer(("localhost",10010))
         self.localServer.register_instance(MyFuncs())

    def run(self):
         self.localServer.serve_forever()
         
server = ServerThread()
server.start() # The server is now running
print "Listo servidor."

class ClientThread(threading.Thread):
    def __init__(self):
      threading.Thread.__init__(self)
		
    def run(self):
      fin=False  
      while not fin: 
        numero1= raw_input("ingrese un la operacion que desea realizar : ")
        lista=numero1.split(" ")
        respuesta=funciones2.operacion(lista[0],lista[1],lista[2])
        respuesta2=respuesta.split(" ")
        respuesta3=funciones2.resultado(lista[0],respuesta2[1],lista[2],respuesta2[0])
        print " el resultado de la operacion es :",respuesta3
        continuar= raw_input("si desea continuar operando ingrese la tecla S de lo contrario N : ")
        if continuar == 'N':
          fin=True
        else :
          fin=False
         
client = ClientThread()
client.start() # The server is now running





    


