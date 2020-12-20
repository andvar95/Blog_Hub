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
    titulo = StringField("titulo",validators=[DataRequired(message="No dejar vacío")], render_kw={"placeholder": "Elige un título"})
    body_blog = TextAreaField("body_blog",validators=[DataRequired(message="No dejar vacío")])
    visibilidad = RadioField("visibilidad", choices=['Público','Privado'])
    categoria = RadioField("categoria", choices=['Deportes','Cocina','Tecnología','Música','Hogar','Política'])
    publicacion = DateTimeField("Fecha",validators=[DataRequired(message="No dejar vacío")])
    comentarios = RadioField("Comentarios", choices=[('value','Permitido'),('value_two','No permitido')])

class formComentarios(FlaskForm):
    cuerpo = StringField("Cuerpo",validators=[DataRequired(message="No dejar vacío")])
    enviar = SubmitField("Comentar")

class formRecuperar(FlaskForm):
    clave1 = PasswordField("clave1",validators=[DataRequired(message="No dejar vacío")],render_kw={"placeholder":"Escriba su contraseña"})
    clave2= PasswordField("clave2",validators=[DataRequired(message="No dejar vacío")],render_kw={"placeholder":"Repita Contraseña"})
    nombre = StringField("nombre",validators=[DataRequired(message="No dejar vacío")], render_kw={"placeholder": "Elige un título"})
    enviar = SubmitField("Cambiar Contraseña")
