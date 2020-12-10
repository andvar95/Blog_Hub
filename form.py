from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
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
    