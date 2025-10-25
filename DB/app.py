from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mibase.db'
db = SQLAlchemy(app)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    precio = db.Column(db.Float, nullable=False)

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    clave = db.Column(db.String(120), nullable=False)

db.create_all()

# agregar
p1 = Producto(nombre='Mouse', precio=3500)
db.session.add(p1)
db.session.commit()

# agregar
p1 = Producto(nombre='Monitor', precio=150000)
db.session.add(p1)
db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)


    with app.app_context():
        db.create_all()