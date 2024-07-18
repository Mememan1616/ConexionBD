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

