from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import math
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# published as XML-RPC methods (in this case, just 'div','sum').
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
		
	
	

server.register_instance(MyFuncs())
# Run the server's main loop
server.serve_forever()

    
	

