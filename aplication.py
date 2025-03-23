from flask import Flask

app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    return '<h1>PAGINA DE INICIO</h1>'



@app.route('/aplication')
@app.route('/aplication/<name>')
@app.route('/aplication/<name>/<int:age>')#/<strin:name> es una variable y podemos definir el tipo de dato ene sta caso string
def aplication(name = None, age= None):
    if name == None and age == None:
        return '<h1>Hola Mundo</h1>'
    elif age == None:
        return f'<h1>Hola, {name}</h1>'
    else:
        return f'<h1>Hola, {name}! y tu edad es {age * 20}</h1>'