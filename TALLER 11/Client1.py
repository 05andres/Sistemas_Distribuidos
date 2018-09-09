from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import time
import funciones

class MyFuncs():
	def rest(self,x,y):
		s = xmlrpclib.ServerProxy('http://localhost:9980')
		return s.rest(x,y)
	def div(self, x, y):
		s = xmlrpclib.ServerProxy('http://localhost:9995')
		return s.div(x,y)
	def sum(self,x,y):
		s = xmlrpclib.ServerProxy('http://localhost:9997')
		return s.sum(x,y)
	def mult(self,x,y):
		s = xmlrpclib.ServerProxy('http://localhost:9996')
		return s.mult(x,y)
	def exp(self,x,y):
		s = xmlrpclib.ServerProxy('http://localhost:9990')
		return s.exp(x,y)
	def raiz(self,x,y):
		s = xmlrpclib.ServerProxy('http://localhost:9993')
		return s.raiz(x,y)
	def log(self,x,y):
		s = xmlrpclib.ServerProxy('http://localhost:9992')
		return s.log(x,y)
	
class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):
    def __init__(self):
         threading.Thread.__init__(self)
         self.localServer = SimpleThreadedXMLRPCServer(("localhost",10009))
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
        respuesta=funciones.operacion(lista[0],lista[1],lista[2])
        print " el resultado de la operacion es :",respuesta
        continuar= raw_input("si desea continuar operando ingrese la tecla S de lo contrario N : ")
        if continuar == 'N':
          fin=True
        else :
          fin=False
         
client = ClientThread()
client.start() # The server is now running





    


