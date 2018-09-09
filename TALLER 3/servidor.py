import SocketServer
import socket
from nltk.tokenize import word_tokenize
import math

def operacion(operacion,numeros):
	array=numeros[0]+","+numeros[2]
	if operacion == "+":
		res="9997,localhost"+","+array
		return res
	elif operacion == "-":
		res="9996,localhost"+","+array
		return res
	elif operacion == "*":
		res="9995,localhost"+","+array
		return res
	elif operacion == "/":
		res="9994,localhost"+","+array
		return res
	elif operacion == "E":
		res="9993,localhost"+","+array
		return res
	elif operacion == "raiz":
		res="9992,localhost"+","+array
		return res
		#exp=float(1/(float(numero1)))
		#return float(numero2)**exp
	elif operacion == "log":
		res="9991,localhost"+","+array
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