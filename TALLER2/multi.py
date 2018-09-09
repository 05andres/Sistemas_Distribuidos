import socket
import SocketServer
from nltk.tokenize import word_tokenize
def resultado(cade1):
    text1 = str(cade1)
    to= word_tokenize(text1)
    return to

class miHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.numero1 =(self.request.recv(1024))
        self.array=resultado(self.numero1)
        self.result1=str(int(self.array[0])*int(self.array[1]))
        print "los numeros recibidos son :",self.numero1 ,"y el resultado es  :",self.result1
        self.request.send(self.result1)
		

def main():
	print "taller socket"
	host= "localhost"
	puerto =9995 #entre o y 10000 , por los 9000 no estan usados
	server1 = SocketServer.TCPServer((host,puerto),miHandler)
	print "server corriendo"
	server1.serve_forever()
	
						

main()