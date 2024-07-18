from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FormField, SelectField, RadioField,TelField,EmailField,IntegerField

class UserForm(Form):
    matricula=IntegerField('Matricula')
    nombre= StringField('Nombre')
    apaterno=StringField('Apaterno')
    email=EmailField('Correo')
    materias=SelectField(choices=[('ESP','Español'),('MAT','Matematicas'),('ING','Ingles')])
    radios=RadioField('cursos' , choices=[('1','UNO'),('2','DOS'),('3','TRES')])

class UserForm2(Form):
    id=IntegerField('id')
    nombre= StringField('Nombre', [
        validators.DataRequiere(message='El nombre es requerido')
    ])
    apaterno=StringField('Apaterno' , [
        ivalidators.DataRequiere(message='El apellido es requerido')
    ])
    amaterno=StringField('Amaterno' , [
        validators.DataRequiere(message='El apellido es requerido')
    ])
    email=EmailField('Correo' , [
        validators.DataRequiere(message='El correo es requerido'),
        validators.email(message='Ingrese un correo valido')
    ])
   
    


