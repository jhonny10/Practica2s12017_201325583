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
		#print("simple")

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
		#print("cola")

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
		#print("Pila")

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
			nodotemp = self.inicio
			temp = self.fin
			self.fin.abajo = Nodo_D(dato_n)
			self.fin = self.fin.abajo
			self.fin.y = self.y
			self.y = self.y + 1
			self.fin.arriba = temp
			return str("agregado en y")

	def buscarLetraAbajo(self, dato_n):
		temp = self.inicio
		varDato = ord(dato_n)

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

#----------------------------------------------------------------Lateral Dispersa pos y-------------------------------------------------------------------------
class MatrizDispersa():

	def __init__(self):
		#print("Matriz Dispersa")
		self.enx = Horizontal_Dispersa()
		self.eny = Vertical_Dispersa()
		self.digraph = "digraph ejemplo{"

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

	def agregarDispersa(self, dominio, palabra):
		letra = palabra[0]
		tempx = self.enx.buscarH(dominio)
		tempy = self.eny.buscarLetraAbajo(letra)

		if tempy == None: #verifica no se encontro la letra especificada
			self.eny.agregarV(letra) #agrega la letra
			tempy = self.eny.buscarLetraAbajo(letra) #como ya se ingreso 1 entonces se vuelve a buscar no tiene que ser None

		if tempx == None: #verifica si se encontro el dominio especificado
			self.enx.agregarH(dominio) #agrega el dominio
			tempx = self.enx.buscarH(dominio) #como ya se ingreso 1 entonces se vuelve a buscar no tiene que ser None
		
		nodoNuevo = Nodo_D(palabra)#es el nuevo nodo a ingresar
		#ahora verificar si el dominio esta vacio
		#print(tempy)
		nodobusqueda = self.verificarExiste(tempx, tempy.y, letra)

		if nodobusqueda != None:

			while nodobusqueda.atras != None:
				nodobusqueda = nodobusqueda.atras

			nodoNuevo.z = nodobusqueda.z + 1
			nodoNuevo.x = nodobusqueda.x
			nodoNuevo.y = nodobusqueda.y
			nodoNuevo.enfrente = nodobusqueda
			nodobusqueda.atras = nodoNuevo
			#print("nodo busqueda es != None")
		else:
			nodoNuevo.x = tempx.x
			nodoNuevo.y = tempy.y

			nodoEncima = self.verificarNodoEncima(tempx, tempy.y)
			nodoAbajo = self.verificaNodoAbajo(tempx, tempy.y)
			nodoizq = self.verificarNodoIzq(tempy, tempx.x)
			nodoDer = self.verificarNodoDer(tempy, tempx.x)

			if nodoEncima != None:
				nodoNuevo.arriba = nodoEncima
				nodoEncima.abajo = nodoNuevo
			else:
				nodoNuevo.arriba = tempx
				tempx.abajo = nodoNuevo

			if nodoAbajo != None:
				nodoNuevo.abajo = nodoAbajo
				nodoAbajo.arriba = nodoNuevo

			if nodoDer != None:
				nodoNuevo.der = nodoDer
				nodoDer.izq = nodoNuevo

			if nodoizq != None:
				nodoNuevo.izq = nodoizq
				nodoizq.der = nodoNuevo
			else:
				nodoNuevo.izq = tempy
				tempy.der = nodoNuevo
			#print(nodoEncima)
			#print(nodoAbajo)
			#print(nodoizq)
			#print(nodoDer)
		return "Nodo Agregado" #self.retorno(nodoNuevo)

	def verificarExiste(self, dominio, poxy, letra):#verifica si existe un nodo en el dominio con la letra especificada
		nodotemp = dominio.abajo
		while nodotemp != None:
			if nodotemp.dato[0] == letra:
				break
			nodotemp = nodotemp.abajo
		return nodotemp

	def verificarNodoEncima(self, dominio, posy):#si no existe un nodo encima entoces enlazar directamente con el nodo
		nodotemp = dominio#.abajo
		cont = posy - 1
		while nodotemp.abajo != None:
			#if nodotemp.abajo != None:
			if nodotemp.abajo.y > cont:
				return nodotemp
			nodotemp = nodotemp.abajo
		return nodotemp

	def verificaNodoAbajo(self, dominio, posy):#si no existe entonces ingresar nodo como si no tuviera un nodo abajo
		nodoEncima = self.verificarNodoEncima(dominio, posy)
		cont = posy + 1
		if nodoEncima != None:
			while nodoEncima != None:
				if nodoEncima.y >= cont:
					break
					#verificar
				nodoEncima = nodoEncima.abajo
			return nodoEncima
		else:
			nodoEncima = dominio
			while nodoEncima != None:
				if nodoEncima.y >= cont:
					break
					#verificar
				nodoEncima = nodoEncima.abajo
			return nodoEncima

	def verificarNodoIzq(self, tempy, posx): #verifica desde la nodo de la letra
		nodotemp = tempy
		cont = posx - 1
		while nodotemp.der != None:
			#if nodotemp.der != None:
			if nodotemp.der.x > cont:
				return nodotemp
			nodotemp = nodotemp.der
		return nodotemp

	def verificarNodoDer(self, tempy, posx):
		nodo = self.verificarNodoIzq(tempy, posx)
		cont = posx + 1
		if nodo != None:
			while nodo != None:
				if nodo.x >= cont:
					break
					#verificar
				nodo = nodo.der
			return nodo
		else:
			nodo = tempy
			while nodo != None:
				if nodo.x >= cont:
					break
					#verificar
				nodo = nodo.der
			return nodo

	def recorrido(self, dato):
		var2 = self.recorrerEny()
		var1 = self.recorrerEnx()
		
		return self.digraph + var1 + var2 + "}"

	def recorrerEnx(self):#inicia el recorrido desde vertical y  y recorre de derecha a izquierda
		var = ""
		tempy = self.eny.inicio

		while tempy != None:
			nodoAbajo = tempy.abajo

			if nodoAbajo != None:
				var = var + "\n" + str(tempy.dato) + "->" + str(nodoAbajo.dato) + ";"
				var = var + "\n" + str(nodoAbajo.dato) + "->" + str(tempy.dato) + ";"

			nodoy = tempy

			while nodoy != None:
				nodoDer = nodoy.der

				if nodoDer != None:
					var = var + "\n" + str(nodoy.dato) + "->" + str(nodoDer.dato) + ";"
					var = var + "\n" + str(nodoDer.dato) + "->" + str(nodoy.dato) + ";"

				nodoz = nodoy

				while nodoz != None:
					nodoAtras = nodoz.atras
					nodoEnfrente = nodoz.enfrente

					if nodoAtras != None:
						var = var + "\n" + str(nodoz.dato) + "->" + str(nodoAtras.dato) + ";"
						var = var + "\n" + str(nodoAtras.dato) + "->" + str(nodoz.dato) + ";"

					nodoz = nodoz.atras
				nodoy = nodoy.der
			tempy = tempy.abajo
		return var

	def recorrerEny(self):#inicia el recorrido desde horizontal x  y recorre de arriba y abajo
		var = ""
		tempx = self.enx.inicio

		while tempx != None:
			nodoDer = tempx.der

			if nodoDer != None:
				var = var + "\n" + str(tempx.dato) + "->" + str(nodoDer.dato) + ";"
				var = var + "\n" + str(nodoDer.dato) + "->" + str(tempx.dato) + ";"

			nodox = tempx

			while nodox != None:
				nodoAbajo = nodox.abajo

				if nodoAbajo != None:
					var = var + "\n" + str(nodox.dato) + "->" + str(nodoAbajo.dato) + ";"
					var = var + "\n" + str(nodoAbajo.dato) + "->" + str(nodox.dato) + ";"
				nodox = nodox.abajo
			tempx = tempx.der
		return var

	def buscarLetra(self, letra):
		tempy = self.eny.inicio

		while tempy != None:
			if tempy.dato == letra:
				return tempy
			tempy = tempy.abajo
		return tempy

	def buscarDominio(self, dominio):
		tempx = self.enx.inicio

		while tempx != None:
			if tempx.dato == dominio:
				return tempx
			tempx = tempx.der
		return tempx

	def recorridoPorLetra(self, letra):
		var = ""
		nodoTemp = self.buscarLetra(letra)
		while nodoTemp != None:
			nodoDer = nodoTemp.der
			if nodoDer != None:
				var = var + "\n" + str(nodoTemp.dato) + "->" + str(nodoDer.dato) + ";"
				var = var + "\n" + str(nodoDer.dato) + "->" + str(nodoTemp.dato) + ";"
				nodoZ = nodoDer

				while nodoZ != None:
					nodoAtras = nodoZ.atras
					if nodoAtras != None:
						var = var + "\n" + str(nodoZ.dato) + "->" + str(nodoAtras.dato) + ";"
						var = var + "\n" + str(nodoAtras.dato) + "->" + str(nodoZ.dato) + ";"
					nodoZ = nodoZ.atras
			nodoTemp = nodoTemp.der
		return self.digraph + "rankdir = LR;" + var + "}"

	def recorridoPorLetraLista(self, letra):
		var = ""
		nodoTemp = self.buscarLetra(letra)

		while nodoTemp != None:
			nodoz = nodoTemp
			while nodoz != None:
				var = var + str(nodoz.dato) + ","
				nodoz = nodoz.atras
			nodoTemp = nodoTemp.der
		return var

	def recorridoPorDominioLista(self, dominio):
		var = ""
		nodoTemp = self.buscarDominio(dominio)

		while nodoTemp != None:
			nodoz = nodoTemp
			while nodoz != None:
				var = var + str(nodoz.dato) + ","
				nodoz = nodoz.atras
			nodoTemp = nodoTemp.abajo
		return var

	def recorridoPorDominio(self, dominio):
		var = ""
		nodoTemp = self.buscarDominio(dominio)
		while nodoTemp != None:
			nodoAbajo = nodoTemp.abajo
			if nodoAbajo != None:
				var = var + "\n" + str(nodoTemp.dato) + "->" + str(nodoAbajo.dato) + ";"
				var = var + "\n" + str(nodoAbajo.dato) + "->" + str(nodoTemp.dato) + ";"
			nodoTemp = nodoTemp.abajo
			nodoZ = nodoTemp

			while nodoZ != None:
				nodoAtras = nodoZ.atras
				if nodoAtras != None:
					var = var + "\n" + str(nodoZ.dato) + "->" + str(nodoAtras.dato) + ";"
					var = var + "\n" + str(nodoAtras.dato) + "->" + str(nodoZ.dato) + ";"
				nodoZ = nodoZ.atras
		return self.digraph + "rankdir = LR;" + var + "}"

	def eliminarCorreo(self, dominio, palabra):
		nodoDom = self.buscarDominio(dominio)
		if nodoDom != None:
			nodoPalabra = self.existePalabra(nodoDom.abajo, palabra)
			print(nodoPalabra)
			if nodoPalabra != None:
				nodoArriba = nodoPalabra.arriba
				nodoAbajo = nodoPalabra.abajo
				nodoIzq = nodoPalabra.izq
				nodoDer = nodoPalabra.der
				nodoEnfrente = nodoPalabra.enfrente
				nodoAtras = nodoPalabra.atras

				print(nodoArriba)
				print(nodoAbajo)
				print(nodoIzq)
				print(nodoDer)
				print(nodoEnfrente)
				print(nodoAtras)

				if nodoArriba == None and nodoAbajo == None and nodoIzq == None and nodoDer == None:
					if nodoEnfrente != None:
						nodoEnfrente.atras = nodoAtras
					if nodoAtras != None:
						nodoAtras.enfrente = nodoEnfrente
					return "nodo en la posicion z ha sido eliminado"
				else:
					if nodoAtras != None:
						nodoArriba.abajo = nodoAtras
						nodoAtras.arriba = nodoArriba

						nodoAtras.izq = nodoIzq
						nodoIzq.der = nodoAtras

						if nodoAbajo != None:
							nodoAbajo.arriba = nodoAtras
							nodoAtras.abajo = nodoAbajo

						if nodoDer != None:
							nodoDer.izq = nodoAtras
							nodoAtras.der = nodoDer
						nodoAtras.enfrente = nodoEnfrente
						self.reiniciarZ(nodoAtras)
						return "nodo en la primera posicion ha sido eliminido nuevo nodo es el de atras"
					else:
						nodoArriba.abajo = nodoAbajo
						nodoIzq.der = nodoDer
						if nodoAbajo != None:
							nodoAbajo.arriba = nodoArriba
						if nodoDer != None:
							nodoDer.izq = nodoIzq
							return "nodo esta en la primera pos en z"
				return "correo existe"
			else:
				return "correo no existe"
		else:
			return "dominio no existe"

	def existePalabra(self, dominio, palabra):
		nodotemp = dominio
		while nodotemp != None:
			nodoz = nodotemp
			while nodoz != None:
				if nodoz.dato == palabra:
					return nodoz
				nodoz = nodoz.atras
			nodotemp = nodotemp.abajo
		return nodotemp

	def reiniciarZ(self, nodotemp):
		z = 1
		nodo = nodotemp
		while nodo != None:
			nodo.z = z
			nodo = nodo.atras
			z = z + 1

#----------------------------------------------------------------fin clases-------------------------------------------------------------------------
simple = Simple()
cola = Cola()
pila = Pila()
matriz = MatrizDispersa()

"""print(matriz.agregarDispersa("g", "a1"))
print(matriz.agregarDispersa("f", "c1"))
print(matriz.agregarDispersa("y", "a2"))
print(matriz.agregarDispersa("y", "c2"))
print(matriz.agregarDispersa("g", "m1"))
print(matriz.agregarDispersa("g", "m2"))
print(matriz.agregarDispersa("y", "m3"))
print(matriz.agregarDispersa("y", "m3"))
print(matriz.agregarDispersa("g", "c28"))
print(matriz.agregarDispersa("f", "a29"))
print(matriz.agregarDispersa("f", "m34"))

print(matriz.recorridoPorLetra("m"))"""
"""print(matriz.agregarDispersa("hola", "hola1"))
print(matriz.agregarDispersa("hola", "hola2"))

print(matriz.recorrido("datonulo"))"""
"""var = ""
var = chr(66)

var1 = "A"
print(ord(var1))"""
@app.route('/eliminar',methods=['POST'])
def eliminar():
	dato = str(request.form["dato"])#dominio
	dato2 = str(request.form["dato2"])#palabra

	aux = matriz.eliminarCorreo(dato, dato2)
	return aux

@app.route('/recorrerDominio',methods=['POST'])
def recorrerDominio():
	dato = str(request.form["dato"])
	aux = matriz.recorridoPorDominio(dato)
	return aux

@app.route('/recorrerDominioLista',methods=['POST'])
def recorrerDominioLista():
	dato = str(request.form["dato"])
	aux = matriz.recorridoPorDominioLista(dato)
	return aux

@app.route('/recorrerLetraLista',methods=['POST'])
def recorrerLetraLista():
	dato = str(request.form["dato"])
	aux = matriz.recorridoPorLetraLista(dato)
	return aux

@app.route('/recorrerLetra',methods=['POST'])
def recorrerLetra():
	dato = str(request.form["dato"])
	aux = matriz.recorridoPorLetra(dato)
	return aux

@app.route('/recorrerMatriz',methods=['POST'])
def recorrerMatriz():
	dato = str(request.form["dato"])
	aux = matriz.recorrido(dato)
	return aux

@app.route('/agregarDispersa',methods=['POST'])
def agregarDispersa():
	dato = str(request.form["dato"])#dato = dominio
	dato2 = str(request.form["dato2"])#dato2 = palabra
	aux = matriz.agregarDispersa(dato, dato2)
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