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
server.register_instance(MyFuncs())
# Run the server's main loop
server.serve_forever()

    
	

