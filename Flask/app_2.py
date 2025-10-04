# Estructura mínima de código

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola, mundo desde Flask!'

if __name__ == '__main__':
    app.run(debug=True)

# Ejemplo básico de ruta

@app.route('/')
def inicio():
    return 'Bienvenido a mi sitio web'

# Rutas con parámetros

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'Hola, {nombre}!'

