__author__ = "Mac"

#Si mientras trabajan en Python alguna vez les arroja un "IndentationError" es porque en alguna linea, los tabs al inicio de la sentencia estan erroneos, por ejemplo:
#Esto es valido:
#class Usuario():
#	def __init__(self, nombre):
#		self.nombre = nombre
#		self.password = password
#Esto NO es valido y arroja un "IndentationError":
#class Usuario():
#	def __init__(self, nombre):
#		self.nombre = nombre
#	   self.password = password
#	   ^
#	   Esto no deberia de estar ahi, sino que tiene que estar igual de indentado que las demas sentencias.
#
#
#Recomiendo Sublime Text como IDE
#

from flask import Flask, request, Response
app = Flask("__name__")

#Ejemplo de una clase, todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
class Usuario():
    def __init__(self, password, correo, nombre):
        self.nombre = nombre
        self.password = password
        self.correo = correo

@app.route('/metodoWeb',methods=['POST']) 
def hello():
	parametro = str(request.form['dato'])
	dato2 = str(request.form['dato2'])
	return "Hola " + str(parametro) + "!"

@app.route("/e")
def hellof():
	return "Hello World2!"

app.run(debug=True)