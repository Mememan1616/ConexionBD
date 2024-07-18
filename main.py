from flask import Flask , render_template, request,url_for
from flask_material import Material

#proteccion de referencias cruzadas
from flask_wtf.csrf import CSRFProtect
#importamos la clase y la conexion a la base de datos
from config import DevelopmentConfig
#es una variable que nos permiten trabajar con variables globales, para pasar parametros entre rutas
from flask import g
#manda a llamar la clase que contiene las tablas y el modelo de la bd
from models import Alumnos
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

        #le decimos que envie la informacion a la base de datos a trabes del objeto, guardamos los cambios 
        db.session.add(alum)
        db.session.commit()

       
        
    return render_template('alumnos.html',form=alum_form)


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