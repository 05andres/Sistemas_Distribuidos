
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import math

    

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9993),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs():
	def raiz(self,x,y):
		exp=(1/(x))
		return y**exp


server.register_instance(MyFuncs())
# Run the server's main loop
server.serve_forever()