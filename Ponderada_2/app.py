from flask import Flask, render_template, request, redirect

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta y una función para manejar esa ruta
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():

    user = request.form['user']
    password = request.form['password']
    
    return 

# Ejecuta la aplicación si este script es el programa principal
if __name__ == '__main__':
    app.run()
