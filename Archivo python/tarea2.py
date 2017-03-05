from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/tarea2')
def tarea2():
	param = request.args.get('parametro', 'no contiene este parametro')
	return 'el parametro es: {}'.format(param) + " Jhonatan Lopez 201325583"

@app.route('/')
def tarea():
	return 'Bienvenido'

if __name__ == '__main__':
	app.run(debug=True)