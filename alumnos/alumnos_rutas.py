from flask import Flask , render_template, request,url_for,redirect, Blueprint
from flask_material import Material

#proteccion de referencias cruzadas
from flask_wtf.csrf import CSRFProtect
#importamos la clase y la conexion a la base de datos
from config import DevelopmentConfig
#es una variable que nos permiten trabajar con variables globales, para pasar parametros entre rutas
from flask import g
#manda a llamar la clase que contiene las tablas y el modelo de la bd
from models import Alumnos
#manda a llamar la clase que contiene las tablas y el modelo de la bd
from models import Maestros
#Manda mensajes cuando se genera una peticion 
from flask import flash
#Madamos a llamar el objeto de bd que nos ayudara a hacer las transacciones
from models import db
#importa los formularios 
import forms

#creamos el objeto que nos generara la ruta a nuestro modulo usando flask
alumnos=Blueprint('alumnos',__name__,url_prefix='/alumnos')


@alumnos.route("/ABC_alumnos")
def ABC_alumnos():
    #crea el objeto a partir del modelado antes diseñado
    create_forms=forms.UserForm2(request.form)
    alumno=Alumnos.query.all()
    return render_template('ABC_alumnos.html',form=create_forms,alumno=alumno)

@alumnos.route("/modificar",methods=['GET','POST'])
def modificar():

    alum_form=forms.UserForm2(request.form)

    #Revisa si le das al boton para recibir los parametros, si no le mandas nada simplemente ejecuta la ventana
    if request.method=='GET':
        #toma el id del registro y lo manda a una variable
        id=request.args.get('id')
        #alumn1=select*from alumnos where id==id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        #Guarda el id y lo envia a la caja de texto
        alum_form.id.data=request.args.get('id')
        #toma los datos almacenados en la variable alum1 y los manda a las variables del objeto alum_form
        alum_form.nombre.data=alum1.nombre
        alum_form.apaterno.data=alum1.apaterno
        alum_form.amaterno.data=alum1.amaterno
        alum_form.email.data=alum1.email

    #Revisa se envio la instruccion a traves de un boton
    if request.method=='POST':
        id=alum_form.id.data
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum1.nombre=alum_form.nombre.data
        alum1.apaterno=alum_form.apaterno.data
        alum1.amaterno=alum_form.amaterno.data
        alum1.email=alum_form.email.data
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for('alumnos.ABC_alumnos'))
    #en cuanto da click al boton lo enviar a eliminar
    return render_template('modificar.html',form=alum_form)

@alumnos.route("/eliminar", methods=['GET','POST'])
def eliminar():
    #manda a llamar la plantilla de los formularios y lo almacena en la variable
    alum_form=forms.UserForm2(request.form)

    #Revisa si le das al boton para recibir los parametros, si no le mandas nada simplemente ejecuta la ventana
    if request.method=='GET':
        #toma el id del registro y lo manda a una variable
        id=request.args.get('id')
        #alumn1=select*from alumnos where id==id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        #Guarda el id y lo envia a la caja de texto
        alum_form.id.data=request.args.get('id')
        #toma los datos almacenados en la variable alum1 y los manda a las variables del objeto alum_form
        alum_form.nombre.data=alum1.nombre
        alum_form.apaterno.data=alum1.apaterno
        alum_form.amaterno.data=alum1.amaterno
        alum_form.email.data=alum1.email

    #Revisa se envio la instruccion a traves de un boton
    if request.method=='POST':
        id=alum_form.id.data
        alum=Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('alumnos.ABC_alumnos'))
    #en cuanto da click al boton lo enviar a eliminar
    return render_template('eliminar.html',form=alum_form)
