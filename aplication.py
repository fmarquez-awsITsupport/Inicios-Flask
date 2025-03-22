from flask import Flask

app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    return '<h1>PAGINA DE INICIO</h1>'

@app.route('/aplication/<name>')#/<name> es una variable
def aplication(name):
    return f'<h1>Hola, {name}!</h1>'