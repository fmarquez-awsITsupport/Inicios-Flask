from flask import Flask, render_template

app = Flask(__name__) 

# Filtros personalizados
@app.add_template_filter #Funcion decoradora para las plantillas
def today(date):
    return date.strftime('%d-%m-%Y')

#funcion personalizada
@app.add_template_global
def repeat(s, n):
    return s * n

from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    name = 'Fabio'
    friends = ['Camilo', 'Kevin', 'Andres','Luis', 'Diegos']
    date = datetime.now()
    return render_template(
        'index.html', 
        name=name, 
        friends=friends, 
        date=date,
        
    )



@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
@app.route('/hello/<name>/<int:age>/<email>')#/<strin:name> es una variable y podemos definir el tipo de dato ene sta caso string
def aplication(name = None, age= None, email=None): # Se asigna un valor nulo para hacer las comparaciones
    my_data = {
        'name': name,
        'age': age,
        'email': email
    }
    return render_template('hello.html', data=my_data)

from markupsafe import escape

@app.route('/code/path:<code>')#Permite ejecutar codigo
def code(code):
    return f'<code>{escape(code)}</code>'#escape - sirve para convertir codigo en texto plano por ejemplo un alert de js no se ejecutaria solo seria un texto plano