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

#se crea el objeto con bluepint
maestros=Blueprint('maestros',__name__,url_prefix='/maestros')

#ABC de maestros
@maestros.route("/ABC_maestros")
def ABC_maestros():
    #manada a llamar al objeto de  maestros y usar l
    create_forms=forms.MaestrosForm(request.form)
    #hacemos la consulta de todos los datos en la tabla maestros
    maestros=Maestros.query.all()
    #manda a llamar al modulo y las variables que necesitara para funcionar
    return render_template('ABC_maestros.html',form=create_forms,maestros=maestros)

@maestros.route("/maestros_eliminar",methods=['GET','POST'])
def maestros_eliminar():
    maestro_form=forms.MaestrosForm(request.form)

    if request.method=='GET':
        
        #toma la matricula del registro y lo manda a una variable
        matricula=request.args.get('matricula')
        #alumn1=select*from alumnos where id==id
        mat1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        #Guarda el id y lo envia a la caja de texto
        maestro_form.matricula.data=request.args.get('matricula')
        #toma los datos almacenados en la variable alum1 y los manda a las variables del objeto alum_form
        maestro_form.nombre.data=mat1.nombre
        maestro_form.apaterno.data=mat1.apaterno
        maestro_form.amaterno.data=mat1.amaterno
        maestro_form.email.data=mat1.email
        maestro_form.tel.data=mat1.tel
        maestro_form.sueldo.data=mat1.sueldo
    
    if request.method=='POST':
        #se crea una variable que obtenga la informacion de la caja de texto de la matricula
        matricula=maestro_form.matricula.data
        #se crea un objeto con los valores de la tupla o registri seleccionado de la base de datos
        mat=Maestros.query.get(matricula)
        #se manda a eliminar esa tupla o registro
        db.session.delete(mat)
        #se guarda la informacion
        db.session.commit()
        return redirect(url_for('maestros.ABC_maestros'))

    return render_template('maestros_eliminar.html',form=maestro_form)

@app.route("/maestros_modificar",methods=['GET','POST'])
def maestros_modificar():
    maestro_form=forms.MaestrosForm(request.form)

    if request.method=='GET':
        
        #toma la matricula del registro y lo manda a una variable
        matricula=request.args.get('matricula')
        #alumn1=select*from alumnos where id==id
        mat1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        #Guarda el id y lo envia a la caja de texto
        maestro_form.matricula.data=request.args.get('matricula')
        #toma los datos almacenados en la variable alum1 y los manda a las variables del objeto alum_form
        maestro_form.nombre.data=mat1.nombre
        maestro_form.apaterno.data=mat1.apaterno
        maestro_form.amaterno.data=mat1.amaterno
        maestro_form.email.data=mat1.email
        maestro_form.tel.data=mat1.tel
        maestro_form.sueldo.data=mat1.sueldo

    #se busca si se realizo una peticion post
    if request.method=='POST':
        #se obtiene la matricula de la caja de texto
        matricula=maestro_form.matricula.data
        #se crea un obejeto que busque el campo a quien corresponde esa matricula y lo almacene
        mat1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        #se manda a llamar el objeto que tiene los valores y se le envian a los nuevos de las cajas de texto
        mat1.nombre=maestro_form.nombre.data
        mat1.apaterno=maestro_form.apaterno.data
        mat1.amaterno=maestro_form.amaterno.data
        mat1.email=maestro_form.email.data
        mat1.tel=maestro_form.tel.data
        mat1.sueldo=maestro_form.sueldo.data
        #ejecuta la accion sqalchemy y modifica los valores
        db.session.add(mat1)
        #guarda los valores en la base de datos
        db.session.commit()
        #regresa al abc de maestros
        return redirect(url_for('maestro.ABC_maestros'))
        
    return render_template('maestros_modificar.html',form=maestro_form)