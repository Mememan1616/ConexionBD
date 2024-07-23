from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FormField, SelectField, RadioField,TelField,EmailField,IntegerField,FloatField,DecimalField
from wtforms import validators


class UserForm(Form):
    #primera parte es el nombre que tendra el campo, despues es el tipo y por ultimo el nombre de la etiqueta que va arriba del input
    #campo=tipodecampo('Etiqueta')
    matricula=IntegerField('Matricula')
    nombre= StringField('Nombre')
    apaterno=StringField('Apaterno')
    email=EmailField('Correo')
    materias=SelectField(choices=[('ESP','Español'),('MAT','Matematicas'),('ING','Ingles')])
    radios=RadioField('cursos' , choices=[('1','UNO'),('2','DOS'),('3','TRES')])

class UserForm2(Form):
    #primera parte es el nombre que tendra el campo, despues es el tipo y por ultimo el nombre de la etiqueta que va arriba del input
    #campo=tipodecampo('Etiqueta')
    id=IntegerField('id')

    nombre= StringField('Nombre', [
        validators.DataRequired(message='El nombre es requerido')
    ])
    apaterno=StringField('Apaterno' , [
        validators.DataRequired(message='El apellido es requerido')
    ])
    amaterno=StringField('Amaterno' , [
        validators.DataRequired(message='El apellido es requerido')
    ])
    email=EmailField('Correo' , [
        validators.DataRequired(message='El correo es requerido'),
        validators.email(message='Ingrese un correo valido')
    ])

class MaestrosForm(Form):
    #primera parte es el nombre que tendra el campo, despues es el tipo y por ultimo el nombre de la etiqueta que va arriba del input
    #campo=tipodecampo('Etiqueta')
    matricula=StringField('Matricula',[
        validators.DataRequired(message='El nombre es requerido')
    ])
    nombre= StringField('Nombre',[
        validators.DataRequired(message='El nombre es requerido')
    ])
    apaterno=StringField('Apellido paterno',[
        validators.DataRequired(message='El apaterno es requerido')
    ])
    amaterno=StringField('Apellido materno',[
        validators.DataRequired(message='El amaterno es requerido')
    ])
    email=EmailField('Correo',[
        validators.DataRequired(message='El correo es requerido'),
        validators.email(message='Ingrese un correo valido')
    ])
    tel=StringField('Telefono',[
        validators.DataRequired(message='El telefono es requerido')
    ])
    sueldo=DecimalField('Sueldo',[
        validators.DataRequired(message='El sueldo es requerido')
    ])

   
    


