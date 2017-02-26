from flask import Flask, request, Response
app = Flask(__name__)

class Simple:
	def __init__(self):
		self.size = 0       #size tamaño
		self.raiz = None    #Nodo Raiz
		self.actual = None  #Nodo actual


@app.route("/metodoAdd", methods=['POST'])
	def add(self, dato):

		if self.raiz == None:
			self.raiz = self.actual = Nodo(dato)
			self.size = self.size + 1
			return True
		else:
			self.actual.sig = Nodo(dato)
			self.actual = actual.sig
			self.size = self.size + 1
			return True

@app.route("/metodoRemove", methods=['POST'])
	def remove(self, index):
		temp = self.raiz   # temp el que se va a eliminar
		cont = 0

		while temp != None and cont < index:
			temp = temp.sig
			cont = cont + 1

		aux = self.raiz    # aux para comparar y eliminar

		if aux != None:
			if aux != temp:
				while aux.sig != None:
					if aux.sig == temp:
						aux.sig = temp.sig
						self.size = self.size - 1
						return temp

					aux = aux.sig
			else:
				self.raiz = self.raiz.sig
				self.size = self.size - 1
				return temp
		return None

@app.route("/metodoSearch", methods=['POST'])
	def search(self, dato):
		temp = self.raiz

		while temp != None:
			if temp.dato == dato:
				return temp.dato
			temp = temp.sig
		return None

@app.route("/metodoPrint", methods=['POST'])
	def imprimir(self):
		dato = ""
		temp = self.raiz

		while temp != None:
			dato = dato + temp.dato + "->"
			temp = temp.sig
			
		return dato



if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

class  Nodo:
	def __init__(self):
		self.dato = None #string del nombre
		self.sig = None  #None es como null
		