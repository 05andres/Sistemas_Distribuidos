import SocketServer
from nltk.tokenize import word_tokenize
import math
def operacion(numero1,operacion,numero2):
	if operacion == "+":
		return int(numero1)+int(numero2)
	elif operacion == "-":
		return int(numero1)-int(numero2)
	elif operacion == "*":
		return int(numero1) *int(numero2)
	elif operacion == "/":
		return float(float(numero1) / float(numero2))
	elif operacion == "E":
		return int(numero1)**int(numero2)
	elif operacion == "raiz":
		exp=float(1/(float(numero1)))
		print exp 
		return float(numero2)**exp
	elif operacion == "log":
		return math.log(float(numero1),(float(numero2)))
	else:
		return "ingrese una operacion valida"
    
def resultado(cade1):
    text1 = str(cade1)
    to= word_tokenize(text1)
    return to
    
	

class miHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		self.numero1 =(self.request.recv(1024))
		#de a 1024 datos se va a recivir
		self.result=(resultado(self.numero1))
		self.result1=str(operacion(self.result[0],self.result[1],self.result[2]))
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