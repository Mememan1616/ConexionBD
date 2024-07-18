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
    app.run(debug=True)