import SocketServer
import os

def operacion(op,nombre):
	if op == 1:
		group(nombre)
		return "grupo creado"
	if op == 2:
		delete_grupo(nombre)
		return " grupo eliminado"
	else:
		return " ingrese una operacion valida"

def consultar_grupo():
	path = 'C:/Users/Administrador/Documents/GitHub/Sistemas_Distribuidos/TALLER13'
	#Lista vacia para incluir los ficheros
	lstFiles = []
	#Lista con todos los ficheros del directorio:
	lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
	#Crea una lista de los ficheros txt que existen en el directorio y los incluye a la lista.
	for root, dirs, files in lstDir:
		for fichero in files:
			(nombreFichero, extension) = os.path.splitext(fichero)
			if(extension == ".txt"):
				lstFiles.append(nombreFichero+extension)
	consul= lstFiles
	str1=','.join(str(e) for e in consul)
	str2=str1.replace(".txt","")
	texto= "los grupos existentes son : " + str2 
	return texto
	

def group(nombre):
	a = open(nombre+".txt","a")
	grupo=["grupo:","localhost","9998"]
	txt='\n'.join(grupo) 
	f=open(nombre+".txt","r+") 
	f.write(txt) 
	f.close()
def delete_grupo(nombre):
	os.remove(nombre+".txt")

class miHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		self.numero1 =(self.request.recv(1024))
		self.numero2= self.numero1.split(" ")
		#de a 1024 datos se va a recivir
		if len(self.numero2)==2:
			self.result1=str(operacion(int(self.numero2[0]),self.numero2[1]))
			print "creando o eliminado grupo"
		else:
			print "Consultando grupos"
			self.result1=str(consultar_grupo())

		self.request.send(self.result1)
		

def main():
	print "taller socket"
	host= "localhost"
	puerto =9998 #entre o y 10000 , por los 9000 no estan usados

	server1 = SocketServer.TCPServer((host,puerto),miHandler)
	print "server corriendo"
	server1.serve_forever()
	
						

main()