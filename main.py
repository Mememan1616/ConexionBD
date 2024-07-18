from flask import Flask , render_template, request,url_for
from flask_material import Material

import forms

app=Flask(__name__)
Material(app)

@app.route("/")#Rutas
def index():
    titulo ="index de Titulo"
    lista=["alex","martin","Luz"]
    return render_template("index.html", titulo=titulo , lista=lista)


@app.route("/saludo")
def hello():
    return "<h1>Hello my world</h1>"

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


@app.route("/formulario1")
def formulario1():
    return render_template("formulario1.html")

@app.route("/formulario2")
def formulario2():
    return render_template("formulario2.html")


@app.route("/formulario3", methods=['GET','POST'])
def formulario3():
    num1=0
    num2=0
    if request.method=='POST':
        num1= int (request.form.get('num1'))
        num2= int (request.form.get('num2'))
       
        return render_template("formulario3.html",num1=num1,num2=num2)

    return render_template("formulario3.html",num1=num1,num2=num2)
    
        

    








@app.route("/imprime", methods=['post'])
def imprime():
    nom=request.form.get("nom")
    password=request.form.get("password")
    return render_template("imprime.html", nom=nom, password=password)


if __name__=="__main__":
    app.run(debug=True)