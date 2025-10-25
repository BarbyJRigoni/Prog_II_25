from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("formulario.html")

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form['nombre']
    edad = request.form['edad']
    return render_template("resultado.html", nombre=nombre, edad=edad)

if __name__ == '__main__':
    app.run(debug=True)

