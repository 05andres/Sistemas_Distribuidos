from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
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
		return x - y
	def div(self, x, y):
		return x / y
	def sum(self,x,y):
		return x + y
	def mult(self,x,y):
		return x * y
	def exp(self,x,y):
		return pow(x,y)
	def raiz(self,x,y):
		exp=(1/(x))
		return y**exp
	def log(self,x,y):
		return math.log(x,y)
	
	

server.register_instance(MyFuncs())
# Run the server's main loop
server.serve_forever()

    
	

