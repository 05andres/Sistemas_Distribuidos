import SocketServer
import socket
from nltk.tokenize import word_tokenize
import math

def sock(puer,cadena):
	try:
			print "enviendo datos"
			puerto=puer
			host="localhost"
			socket1= socket.socket()
			socket1.connect((host,puerto))
			socket1.send(cadena)
			respuesta=socket1.recv(1024)
			socket1.close()
			return  respuesta
	except :
		print "NO SE HA ESTABLECIDO UNA CONEXION CON EL SERVIDOR"

def operacion(operacion,array):
	string=array[0]+" "+array[2]
	if operacion == "+":
		res=sock(9997,string)
		return res
	elif operacion == "-":
		res=sock(9996,string)
		return res
	elif operacion == "*":
		res=sock(9995,string)
		return res
	elif operacion == "/":
		res=sock(9994,string)
		return res
	elif operacion == "E":
		res=sock(9993,string)
		return res
	elif operacion == "raiz":
		res=sock(9992,string)
		return res
		#exp=float(1/(float(numero1)))
		#return float(numero2)**exp
	elif operacion == "log":
		res=sock(9991,string)
		return res
		#return math.log(float(numero1),(float(numero2)))
	else:
		return "ingrese una operacion valida"
  
def resultado(cade1):
    text1 = str(cade1)
    to= word_tokenize(text1)
    return to
    
class miHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		self.numero1 =(self.request.recv(1024))
		self.result=(resultado(self.numero1))
		self.result1=str(operacion(self.result[1],self.result))
		print "los numeros recibidos son :",self.numero1 ,"y el resultado es  :",self.result1
		self.request.send(self.result1)
def main():
	print "taller socket"
	host= "localhost"
	puerto =9998 #entre o y 10000 , por los 9000 no estan usados
	server1 = SocketServer.TCPServer((host,puerto),miHandler)
	print "server corriendo"
	server1.serve_forever()
main()