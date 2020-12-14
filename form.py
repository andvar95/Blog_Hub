from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, DateTimeField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


#Foormularios Logueo


class formLogueo(FlaskForm):
    usuario = StringField("usuario",validators=[DataRequired(message="No Dejar vacío")], render_kw={"placeholder": "Usuario"})
    clave = PasswordField("clave",validators=[DataRequired(message="No Dejar vacío")],render_kw={"placeholder": "Contraseña"})
    recordar = BooleanField("Recordar Usuario")
    enviar = SubmitField("Iniciar Sesión")
    

class formRegistro(FlaskForm):
    usuario = StringField("usuario",validators=[DataRequired(message="No Dejar vacío")], render_kw={"placeholder": "Usuario"})
    clave = PasswordField("clave",validators=[DataRequired(message="No Dejar vacío")],render_kw={"placeholder": "Contraseña"})
    correo =  EmailField("Email",validators=[DataRequired(message="No Dejar vacío")],render_kw={"placeholder": "Correo Electrónico"})
    enviar = SubmitField("Registrarse")

class formCrearBlog(FlaskForm):
    titulo = StringField("Título",validators=[DataRequired(message="No dejar vacío")], render_kw={"placeholder": "Elige un título"})
    cuerpo = TextAreaField("Cuerpo",validators=[DataRequired(message="No dejar vacío")])
    visibilidad = RadioField("Visibilidad", choices=[('value','Permitido'),('value_two','No permitido')])
