from flask import Flask, request, Response
app = Flask(__name__)
#----------------------------------------------------------------clase simple------------------------------------------------------------------------
class Simple():
	"""docstring for Simple"""

	def __init__(self):
		self.raiz = None
		self.actual = None
		self.size = 0
		self.digraph = "digraph ejemplo{"
		print("simple")

	def reiniciarDigraph(self, dato):
		self.digraph = "digraph ejemplo{"
		return self.digraph

	def recorrer(self, raizs, dato):
		var = ""
		while raizs != None:
			if raizs.sig != None:
				var = var + "\n" + str(raizs.dato) + "->" + str(raizs.sig.dato)
			raizs = raizs.sig
		return str(self.digraph + var + "}")

	def agregar(self, dato):
		if self.raiz == None:
			self.raiz = Nodo(dato, None)
			self.actual = self.raiz
			self.size = self.size + 1
			return str(self.size)
		else:
			self.actual.sig = Nodo(dato, None)
			self.actual = self.actual.sig
			self.size = self.size + 1
			return str(self.size)

	def buscar(self, dato):
		cont = 0
		temp = self.raiz
		while temp != None:
			if temp.dato == dato:
				return str(cont)
			temp = temp.sig
			cont = cont + 1
		return str(None)

	def remove(self, index):
		temp = self.raiz   
		"""temp el que se va a eliminar"""
		cont = 0
		if(index < self.size):
			while temp != None and cont < index:
				temp = temp.sig
				cont = cont + 1
		
			aux = self.raiz    
			""" aux para comparar y eliminar"""
			if aux != None:
				if aux != temp:
					while aux.sig != None:
						if aux.sig == temp:
							aux.sig = temp.sig
							self.size = self.size - 1
							if temp == self.actual:
								if aux.sig != None:
									self.actual = aux.sig
								else:
									self.actual = aux
							return str(temp.dato)
						aux = aux.sig
				else:
					self.raiz = self.raiz.sig
					self.size = self.size - 1
					return str(temp.dato)
		return str(None)

#---------------------------------------------------------------clase Cola-------------------------------------------------------------------------
class Cola():
	"""docstring for Cola"""
	def __init__(self):
		self.raiz = None
		self.actual = None
		self.size = 0
		self.digraph = "digraph ejemplo{"
		print("cola")

	def reiniciarDigraph(self, dato):
		self.digraph = "digraph ejemplo{"

	def recorrer(self, raizs, dato):
		var = ""
		while raizs != None:
			if raizs.sig != None:
				var = var + "\n" + str(raizs.dato) + "->" + str(raizs.sig.dato)
			raizs = raizs.sig
		return str(self.digraph + var + "}")

	def add(self, dato):
		if self.raiz == None:
			self.raiz = Nodo(dato, None)
			self.actual = self.raiz
			self.size = self.size + 1
			return str(self.size)
		else:
			self.actual.sig = Nodo(dato, None)
			self.actual = self.actual.sig
			self.size = self.size + 1
			return str(self.size)

	def desencolar(self, dato):
		temp = self.raiz
		if self.raiz != None:
			temp = self.raiz
			self.raiz = self.raiz.sig
			self.size = self.size - 1
			if temp == self.actual:
				self.actual = self.raiz
			return str(temp.dato)
		else:
			return str("NO SE ENCONTRO EL DATO")

#----------------------------------------------------------------Clase pila-------------------------------------------------------------------------
class Pila():
	"""docstring for Pila"""
	def __init__(self):
		self.raiz = None
		self.actual = None
		self.size = 0
		self.digraph = "digraph ejemplo{"
		print("Pila")

	def recorrer(self, raizs, dato):
		var = ""
		while raizs != None:
			if raizs.sig != None:
				var = var + "\n" + str(raizs.dato) + "->" + str(raizs.sig.dato)
			raizs = raizs.sig
		return str(self.digraph + var + "}")

	def pushsPila(self, dato):
		if self.raiz == None:
			self.raiz = Nodo(dato, None)
			self.actual = self.raiz
			self.size = self.size + 1
			return str(self.size)
		else:
			self.actual.sig = Nodo(dato, None)
			self.actual = self.actual.sig
			self.size = self.size + 1
			return str(self.size)

	def popsPila(self, dato):
		temp = self.raiz
		if temp != None:
			if temp.sig != None:
				while temp.sig != None:
					if temp.sig == self.actual:
						aux = temp.sig
						self.actual = temp
						temp.sig = None
						self.size = self.size - 1
						return str(aux.dato)
					temp = temp.sig
			else:
				aux = self.raiz
				self.size = self.size - 1
				self.raiz = None
				return str(aux.dato)
		return str(None)

#----------------------------------------------------------------Clase nodo-------------------------------------------------------------------------
class Nodo():
	def __init__(self, dato_n, sig_n):
		self.dato = dato_n
		self.sig = sig_n

#----------------------------------------------------------------Clase nodo_D-------------------------------------------------------------------------
class Nodo_D():
	def __init__(self, dato_n):
		self.dato = dato_n
		self.arriba = None
		self.abajo = None
		self.izq = None
		self.der = None
		self.atras = None
		self.enfrente = None
		self.x = 0
		self.y = 0
		self.z = 0

#----------------------------------------------------------------inclinada Dispersa pos z-------------------------------------------------------------------------
class Vertical_Dispersa():
	def __init__(self):
		self.inicio = None
		self.fin = None
		self.y = 1
		#self.enz = InclinadaDispersa()

	def agregarV(self, dato_n): #agregando ...se utiliza solo los nodos arriba y abajo
		if self.inicio == None:
			self.inicio = Nodo_D(dato_n)
			self.inicio.y = self.y
			self.y = self.y + 1
			self.fin = self.inicio
			return str("agregado en y")
		else:
			temp = self.fin
			self.fin.abajo = Nodo_D(dato_n)
			self.fin = self.fin.abajo
			self.fin.y = self.y
			self.y = self.y + 1
			self.fin.arriba = temp
			return str("agregado en y")

	def buscarLetraAbajo(self, dato_n):
		temp = self.inicio
		while temp != None:
			if temp.dato == dato_n:
				return temp
			temp = temp.abajo
		return None

	def recorrerLetraAbajo(self, dato_n):# retorna el string del recorrido
		var = ""
		temp = self.inicio
		while temp != None:
			if temp.dato == dato_n:
				var = var + "\n" + str(temp.dato)
			temp = temp.abajo
		return var

	def recorrerDerecha(self, dato_n):#recorre toda la letra para la derecha
		var = ""
		encontrado = buscarLetraAbajo(dato_n) #recorrer para abajo hasta encontrar la letra
		if encontrado != None:
			while encontrado != None:
				if encontrado.dato == dato_n:
					var = var + "\n" + str(encontrado.dato)
				encontrado = encontrado.der
		return var

#----------------------------------------------------------------inclinada Dispersa pos z-------------------------------------------------------------------------
class Horizontal_Dispersa():
	def __init__(self):
		self.inicio = None
		self.fin = None
		self.x = 1

	def agregarH(self, dato):
		if self.inicio == None:
			self.inicio = Nodo_D(dato)
			self.inicio.x = self.x
			self.x = self.x + 1
			self.fin = self.inicio
			return str("agregado en x")
		else:
			temp = self.fin
			self.fin.der = Nodo_D(dato)
			self.fin = self.fin.der
			self.fin.x = self.x
			self.x = self.x + 1
			self.fin.izq = temp
			return str("agregado en x")


	def buscarH(self, dato_n):
		temp = self.inicio
		while temp != None:
			if temp.dato == dato_n:
				return temp
			temp = temp.der
		return None

	def recorrerDer(self, dato_n):
		var = ""
		temp = self.inicio
		while temp != None:
			if temp.dato == dato_n:
				var = var + "\n" + str(temp.dato)
			temp = temp.der
		return var

#----------------------------------------------------------------Cabeza Dispersa pos x------------------------------------------------------------------------
class InclinadaDispersa():
	def __init__(self):
		self.inicio = None
		self.fin = None
		self.z = 1

	def agregarZ(self, dato):
		if self.inicio == None:
			self.inicio = Nodo_D(dato)
			self.inicio.z = self.z
			self.z = self.z + 1
			self.fin = self.inicio
			return str("agregado en z")
		else:
			temp = self.fin
			self.fin.atras = Nodo_D(dato)
			self.fin = self.fin.atras
			self.fin.z = self.z
			self.z = self.z + 1
			self.fin.enfrente = temp
			return str("agregado en z")

	def buscarAtras(self, dato_n):
		temp = self.inicio
		while temp != None:
			if temp.dato == dato_n:
				return temp
			temp = temp.atras
		return None

	def recorrerAtras(self, dato_n):
		var = ""
		temp = self.inicio
		while temp != None:
			if temp.dato == dato_n:
				var = var + "\n" + str(temp.dato)
			temp = temp.atras
		return var

#----------------------------------------------------------------Lateral Dispersa pos y-------------------------------------------------------------------------
class MatrizDispersa():

	def __init__(self):
		print("Matriz Dispersa")
		self.enx = Horizontal_Dispersa()
		self.eny = Vertical_Dispersa()

	def retorno(self, nodo):
		var = ""
		if nodo.arriba != None:
			var = var + "\n" + str(nodo.dato) + "->" + str(nodo.arriba.dato)
		else:
			var = var + "\n" + str(nodo.dato) + "->None"

		if nodo.abajo != None:
			var = var + "\n" + str(nodo.dato) + "->" + str(nodo.abajo.dato)
		else:
			var = var + "\n" + str(nodo.dato) + "->None"

		if nodo.enfrente != None:
			var = var + "\n" + str(nodo.dato) + "->" + str(nodo.enfrente.dato)
		else:
			var = var + "\n" + str(nodo.dato) + "->None"

		if nodo.atras != None:
			var = var + "\n" + str(nodo.dato) + "->" + str(nodo.atras.dato)
		else:
			var = var + "\n" + str(nodo.dato) + "->None"

		if nodo.der != None:
			var = var + "\n" + str(nodo.dato) + "->" + str(nodo.der.dato)
		else:
			var = var + "\n" + str(nodo.dato) + "->None"

		if nodo.izq != None:
			var = var + "\n" + str(nodo.dato) + "->" + str(nodo.izq.dato)
		else:
			var = var + "\n" + str(nodo.dato) + "->None"

		return var

	def ingresoDato(self, dominio, palabra):
		letra = palabra[0]
		tempx = self.enx.buscarH(dominio)
		tempy = self.eny.buscarLetraAbajo(letra) #verifica si hay una letra "L" de la palabra
		#tempz = self.enz.buscarZ(palabra)

		if tempy == None: #por que no existe le letra especificada
			self.eny.agregarV(letra) #agrega la letra en vertical
			auxy = self.eny.buscarLetraAbajo(letra) #busca letra vertical y se obtiene para uso
			if tempx == None: #por que no existe el dominio
				self.enx.agregarH(dominio) #se agrega el dominio
				auxx = self.enx.buscarH(dominio) #se vuelve a buscar el dominio

				while auxx.abajo != None: #revisar si se encuentra la palabra para abajo del dominio
					auxx = auxx.abajo
				auxx.abajo = Nodo_D(palabra)
				tempAux = auxx
				auxx = auxx.abajo
				auxx.arriba = tempAux
				auxx.izq = auxy
				auxy.der = auxx
				#var = str(auxx.dato)+ "->"+str(auxx.arriba.dato)+ "\n"+ str(auxx.dato) + "->" + str(auxx.abajo.dato) + "\n" + str(auxx.dato) + "->" + str(auxx.izq.dato) + " " + str(aux.dato) + "->" + str(aux.der.dato)
				return self.retorno(auxx)
			else: #si existe el dominio
				auxx = tempx #buscar el dominio

				while auxx.abajo != None: #revisar si se encuentra la palabra para abajo del dominio
					auxx = auxx.abajo
				auxx.abajo = Nodo_D(palabra)
				tempAux = auxx
				auxx = auxx.abajo
				auxx.arriba = tempAux
				auxx.izq = auxy
				auxy.der = auxx
				return self.retorno(auxx)
		else: #si existe la letra especificada
			auxy = self.eny.buscarLetraAbajo(letra)
			if tempx == None:
				self.enx.agregarH(dominio) #se agrega el dominio
				auxx = self.enx.buscarH(dominio) #se vuelve a buscar el dominio

				while auxx.abajo != None: #revisar si se encuentra la palabra para abajo del dominio
					auxx = auxx.abajo

				while auxy.der != None:
					auxy = auxy.der

				auxx.abajo = Nodo_D(palabra)
				tempAux = auxx
				auxx = auxx.abajo
				auxx.arriba = tempAux
				auxx.izq = auxy
				auxy.der = auxx
				return self.retorno(auxx)
			
			else:
				auxDom = tempx.abajo
				nodoTemp = None
				while auxDom != None: #buscar hasta encontrar la primera letra de la palabra
					if auxDom.dato[0] == letra:
						break
					nodoTemp = auxDom
					auxDom = auxDom.abajo
				#si auxDom no existe
				if auxDom != None:
					#ahora recorrer hacia atras
					while auxDom.atras != None:
						auxDom = auxDom.atras

					auxTemp = auxDom
					auxDom.atras = Nodo_D(palabra)
					auxDom = auxDom.atras
					auxDom.enfrente = auxTemp
					return self.retorno(auxDom)
				else:
					if nodoTemp != None:
						nodoT1 = tempy.der #nodoT1 es el nodo que esta mas a la derecha
						nodoTemp.abajo = Nodo_D(palabra)
						nodoT2 = nodoTemp #nodoT2 es el nodo de actual del nodoTemp antes de pasar al de abajo
						nodoTemp = nodoTemp.abajo
						nodoTemp.arriba = nodoT2
						nodoTemp.der = nodoT1
						nodoT1.izq = #visualizar bien esto falta en medio de datos

				"""cuando existe el dominio y la letra"""
			#recorrer en para la der
#----------------------------------------------------------------fin clases-------------------------------------------------------------------------
simple = Simple()
cola = Cola()
pila = Pila()
matriz = MatrizDispersa()

verDis = Vertical_Dispersa()
horiD = Horizontal_Dispersa()
intcD = InclinadaDispersa()

print(matriz.ingresoDato("dominio1", "dato1"))
print(matriz.ingresoDato("dominio1", "dato2"))
print(matriz.ingresoDato("dominio1", "dato3"))
print(matriz.ingresoDato("dominio2", "dato0"))
print(matriz.ingresoDato("dominio2", "mesa"))
print(matriz.ingresoDato("dominio1", "melodia"))

@app.route('/agregarDispersa',methods=['POST'])
def agregarDispersa():
	dato = str(request.form["dato"])
	dato2 = str(request.form["dato2"])
	aux = matriz.ingresoDato(dato, dato2)
	return aux

@app.route('/agregarSimple',methods=['POST']) 
def addSimple():
	dato = str(request.form["dato"])
	aux = simple.agregar(dato)
	return dato + " " + aux

@app.route('/recorrerSimple',methods=['POST']) 
def recorrerSimple():
	dato = str(request.form["dato"])
	aux = simple.recorrer(simple.raiz, dato)
	return aux

@app.route("/buscarSimple", methods=['POST'])
def searchSimple():
	dato = str(request.form["dato"])
	aux = simple.buscar(dato)
	return aux

@app.route("/removeSimple", methods=['POST'])
def removeSimple():
	dato = int(request.form["dato"])
	aux = simple.remove(dato)
	return aux

@app.route("/queueCola", methods=['POST'])
def queueCola():
	dato = str(request.form["dato"])
	aux = cola.add(dato)
	return aux

@app.route("/deQueueCola", methods=['POST'])
def deQueueCola():
	dato = str(request.form["dato"])
	aux = cola.desencolar(dato)
	return aux

@app.route('/recorrerCola',methods=['POST']) 
def recorrerCola():
	dato = str(request.form["dato"])
	aux = cola.recorrer(cola.raiz, dato)
	return aux

@app.route("/pushPila", methods=['POST'])
def pushPila():
	dato = str(request.form["dato"])
	aux = pila.pushsPila(dato)
	return aux

@app.route("/popPila", methods=['POST'])
def popPila():
	dato = str(request.form["dato"])
	aux = pila.popsPila(dato)
	return aux

@app.route('/recorrersPila',methods=['POST']) 
def recorrersPila():
	dato = str(request.form["dato"])
	aux = pila.recorrer(pila.raiz, dato)
	return aux

if __name__ == '__main__':
	app.run(debug=True)
