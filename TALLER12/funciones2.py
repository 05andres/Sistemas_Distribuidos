import xmlrpclib
import math

def operacion(numero1,operacion,numero2):
    s = xmlrpclib.ServerProxy('http://localhost:10009')
    if operacion == "+":
      return s.sum()
    elif operacion == "-":
      return s.rest()
    elif operacion == "*":
      return s.mult()
    elif operacion == "/":
      return s.div()
    elif operacion == "E":
      return  s.exp()
    elif operacion == "raiz":
        return  s.raiz()		
    elif operacion == "log":
        return  s.log()	
    else:
		return "ingrese una operacion valida"
#comunicacion con el servidor de operacion
def resultado(numero1,operacion,numero2,puerto):
  s = xmlrpclib.ServerProxy('http://localhost:'+puerto)
  if operacion == 'rest':
    return s.rest(float(numero1),float(numero2))
  if operacion == "sum":
      return s.sum(int(numero1),int(numero2))
  elif operacion == "mult":
    return s.mult(int(numero1),int(numero2))
  elif operacion == "div":
    return s.div(float(numero1),float(numero2))
  elif operacion == "exp":
    return  s.exp(float(numero1),float(numero2))
  elif operacion == "raiz":
      return  s.raiz(float(numero1),float(numero2))		
  elif operacion == "log":
      return  s.log(float(numero1),float(numero2))	
  else:
    return "ingrese una operacion valida"