# Código principal de la aplicación Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Hola Flask!'

if __name__== '__main__':
    app.run(debug=True)

# app.py - Ejemplo de código básico de Flask

from flask import Flask, render_template  #Importa la clase Flask desde el framework

app = Flask(__name__) #Crea una instancia de la aplicación

@app.route('/')  #Define una ruta para la URL raíz del sitio, es decir, que sucede cuando accedemos al sitio web.
def inicio():
    return render_template('index.html')  # carga una plantilla HTML ubicada en la carpeta templates.

if __name__ == '__main':
    app.run(debug=True)  # Inicia el servidor local y activa el modo debug (recarga la app ante cada cambio y muestra errores detallados)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola, mundo desde Flask!'

if __name__ == '__main__':
    app.run(debug=True)
