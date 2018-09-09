import xmlrpclib
import math

def operacion(numero1,operacion,numero2):
    s = xmlrpclib.ServerProxy('http://localhost:8000')
    if operacion == "+":
      return s.sum(int(numero1),int(numero2))
    elif operacion == "-":
      return s.rest(int(numero1),int(numero2))
    elif operacion == "*":
      return s.mult(int(numero1),int(numero2))
    elif operacion == "/":
      return s.div(float(numero1),float(numero2))
    elif operacion == "E":
      return  s.exp(float(numero1),float(numero2))
    elif operacion == "raiz":
        return  s.raiz(float(numero1),float(numero2))		
    elif operacion == "log":
        return  s.raiz(float(numero1),float(numero2))	
    else:
      return "ingrese una operacion valida"