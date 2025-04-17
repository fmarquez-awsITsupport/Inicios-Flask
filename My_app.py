from flask import Flask, render_template, url_for, request

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
    print(url_for('index')) #Url FOR sirve para crear enlaces y rutas como accesos a traves de NAV en HTML e integracion de archivos estaticos JS, CSS, IMG
    print(url_for('aplication', name ='Fabio', age = '25'))
    print(url_for('code', code = 'print("Hola")'))
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
@app.route('/hello/<name>/<int:age>/<email>')#/<string:name> es una variable y podemos definir el tipo de dato ene sta caso string
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

#Registrar Usuario
@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']#Captutrando el nombre de usuario
        password = request.form['password']

        if len(username) >= 4 and len(username) <= 25 and len(password) >= 6 and len(password) <=40:
            return f"Nombre de usuario: {username}, Contraseña: {password}"
        else:
            error = """Nombre de usuario debe tener caracteres y la contraseña debe tener caracteres"""
            return render_template('auth/registrer.html', error = error)
    return render_template('auth/registrer.html')