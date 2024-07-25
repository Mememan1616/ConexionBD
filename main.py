from flask import Flask , render_template, request,url_for,redirect
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

app=Flask(__name__)
#Invocamos nuestra clase Decvelopment config para hacer referencia a la base de datos
app.config.from_object(DevelopmentConfig)

Material(app)
#Creamos una variable que almacene el CSRF
csrf=CSRFProtect()

@app.route("/")#Rutas
def index():
    titulo ="index de Titulo"
    lista=["alex","martin","Luz"]
    return render_template("index.html", titulo=titulo , lista=lista)


@app.route("/ABC_alumnos")
def ABC_alumnos():
    #crea el objeto a partir del modelado antes diseñado
    create_forms=forms.UserForm2(request.form)
    alumno=Alumnos.query.all()
    return render_template('ABC_alumnos.html',form=create_forms,alumno=alumno)

@app.route("/ABC_maestros")
def ABC_maestros():
    #manada a llamar al objeto de  maestros y usar l
    create_forms=forms.MaestrosForm(request.form)
    #hacemos la consulta de todos los datos en la tabla maestros
    maestros=Maestros.query.all()
    #manda a llamar al modulo y las variables que necesitara para funcionar
    return render_template('ABC_maestros.html',form=create_forms,maestros=maestros)



@app.route("/alumnos",methods=['GET','POST'])
def alumnos():
    alum_form=forms.UserForm2(request.form)

    #Revisa si le das al boton para recibir los parametros, si no le mandas nada simplemente ejecuta la ventana
    if request.method=='POST':
        #se manada a llamar los datos del formulario, se crea una variable y se manda a llamar el campo con su respectiva informacion nombre.data
        alum=Alumnos(nombre=alum_form.nombre.data,
                    apaterno=alum_form.apaterno.data,
                    amaterno=alum_form.amaterno.data,
                    email=alum_form.email.data)

        #Lo que hace la funcion add es añadir la informacion que ya obtuvo el objeto y lo manda a la base de datos
        db.session.add(alum)
        #Guarda la informacion de ese insert que fue creada con ese objeto y la guarda
        db.session.commit()
        mensaje='Registro Nuevo'
        flash(mensaje)
        return redirect(url_for('ABC_alumnos'))  
    return render_template('alumnos.html',form=alum_form)

@app.route("/maestros",methods=['GET','POST'])
def maestros():
    #crea una variable forms para almacenar los datos de las cajas de texto
    maestros_form=forms.MaestrosForm(request.form)

    #revisa si es que se le dio click al boton para hacer el registro
    if request.method=='POST':
        #Para insertar un registro en la base de datos, es necesario, primero, contar con la instancia que se desea añadir. A continuación, agregarlo a la sesión de la base de datos y completar la acción con un commit.
        #esa instancia manda a llamar la clase con la base de datos de que se encuentra en models
        masters=Maestros(matricula=maestros_form.matricula.data,
                        nombre=maestros_form.nombre.data,
                        apaterno=maestros_form.apaterno.data,
                        amaterno=maestros_form.amaterno.data,
                        email=maestros_form.email.data,
                        tel=maestros_form.tel.data,
                        sueldo=maestros_form.sueldo.data)
        #Lo que hace la funcion add es añadir la informacion que ya obtuvo el objeto y lo manda a la base de datos
        db.session.add(masters)
        #Guarda la informacion de ese insert que fue creada con ese objeto y la guarda
        db.session.commit()
        mensaje='Registro Nuevo'
        flash(mensaje)
    
    return render_template('maestros.html',form=maestros_form)


    

@app.route("/eliminar",methods=['GET','POST'])
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
        return redirect(url_for('ABC_alumnos'))
    #en cuanto da click al boton lo enviar a eliminar
    return render_template('eliminar.html',form=alum_form)

@app.route("/maestros_eliminar",methods=['GET','POST'])
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
        return redirect(url_for('ABC_maestros'))

    return render_template('maestros_eliminar.html',form=maestro_form)


   


@app.route("/modificar",methods=['GET','POST'])
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
        return redirect(url_for('ABC_alumnos'))
    #en cuanto da click al boton lo enviar a eliminar
    return render_template('modificar.html',form=alum_form)

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
        return redirect(url_for('ABC_maestros'))
        
    return render_template('maestros_modificar.html',form=maestro_form)



       

@app.route("/usuarios",methods=['GET','POST'])
def usuarios():
    alum_form=forms.UserForm(request.form)

    #Revisa si le das al boton para recibir los parametros, si no le mandas nada simplemente ejecuta la ventana
    if request.method=='POST':
        alum_form=forms.UserForm(request.form)
        matricula=alum_form.matricula.data
        email=alum_form.email.data 
        return render_template("usuarios.html",form=alum_form,email=email,matricula=matricula)
        
    return render_template('usuarios.html',form=alum_form)

if __name__=="__main__":
    #metemos nuestra aplicamos en el csrf como seguridad
    csrf.init_app(app)
    #hace referencia al objeto db en models que maneja la base de datos
    db.init_app(app)
    #se crean las tablas que esten en models si es que no han sido creadas 
    with app.app_context():
         db.create_all()
    #le decimos que corra la aplicacion
    app.run()