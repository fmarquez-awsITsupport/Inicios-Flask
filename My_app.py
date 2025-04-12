from flask import Flask, render_template

app = Flask(__name__) 



@app.route('/')
@app.route('/index')
def index():
    name = 'Fabio'
    friends = ['Camilo', 'Kevin', 'Andres','Luis', 'Diegos']
    return render_template('index.html', name=name, friends=friends )



@app.route('/My_app')
@app.route('/My_app/<name>')
@app.route('/My_app/<name>/<int:age>')#/<strin:name> es una variable y podemos definir el tipo de dato ene sta caso string
def aplication(name = None, age= None): # Se asigna un valor nulo para hacer las comparaciones
    if name == None and age == None:
        return '<h1>Hola Mundo</h1>'
    elif age == None:
        return f'<h1>Hola, {name}</h1>'
    else:
        return f'<h1>Hola, {name}! y tu edad es {age * 20}</h1>'

from markupsafe import escape
@app.route('/code/path:<code>')#Permite ejecutar codigo
def code(code):
    return f'<code>{escape(code)}</code>'#escape - sirve para convertir codigo en texto plano por ejemplo un alert de js no se ejecutaria solo seria un texto plano