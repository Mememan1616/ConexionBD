from flask_sqlalchemy import SQLAlchemy

import datetime
db=SQLAlchemy()

#se crean las tablas desde aqui 
class Alumnos(db.Model):
    __tablename__='alumnos'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(100))
    apaterno=db.Column(db.String(100))
    amaterno=db.Column(db.String(100))
    email=db.Column(db.String(100))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)

class Maestros(db.Model):
    __tablename__='maestros'
    matricula=db.Column(db.String(5),primary_key=True)
    nombre=db.Column(db.String(100))
    apaterno=db.Column(db.String(100))
    amaterno=db.Column(db.String(100))
    email=db.Column(db.String(100))
    tel=db.Column(db.String(100))
    sueldo=db.Column(db.DECIMAL)






