from flask import Flask, request, Response
app = Flask(__name__)
#----------------------------------------------------------------clase simple------------------------------------------------------------------------
class Simple():
	"""docstring for Simple"""

	def __init__(self):
		self.raiz = None
		self.actual = None
		self.size = 0
		print("simple")

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
		print("cola")

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
			self.raiz = self.raiz.sig
			self.size = self.size - 1
			return str(temp.dato)
		else:
			return str("NO SE ENCONTRO EL DATO")

#----------------------------------------------------------------Clase nodo-------------------------------------------------------------------------
class Pila():
	"""docstring for Pila"""
	def __init__(self):
		self.raiz = None
		self.actual = None
		self.size = 0
		print("Pila")

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
#----------------------------------------------------------------fin clases-------------------------------------------------------------------------
simple = Simple()
cola = Cola()
pila = Pila()


@app.route('/agregarSimple',methods=['POST']) 
def addSimple():
	dato = str(request.form["dato"])
	aux = simple.agregar(dato)
	return dato + " " + aux

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

if __name__ == '__main__':
	app.run(debug=True)
