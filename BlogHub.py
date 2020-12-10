from flask import Flask,render_template,flash,request,redirect, url_for
import os
import yagmail as yg
import utils
from markupsafe import escape
from form import formLogueo, formRegistro

app = Flask(__name__)
app.secret_key= os.urandom(24)


#ventana de LOGIN
@app.route('/')
def login():
    form = formLogueo()
    if (form.validate_on_submit()):
        print("valido")
    return render_template('login.html',form= form)


#ventana Registro
@app.route('/registro', methods=["GET","POST"])
def registro():
    try:
        if request.method=="POST":
            print("entre asa")
            user_name = escape(request.form['usuario'])
            e_mail = escape(request.form['correo'])
            pass_word = escape(request.form['clave'])
            error = None
            if not utils.isUsernameValid(user_name):
                error = "El usuario debe ser alfanumérico"
                flash(error)
                print("Erro nombre")
                return render_template('Vista_Registro.html')
            if not utils.isEmailValid(e_mail):
                error = "Email no válido"
                flash(error)
                print("email")
                return render_template('Vista_Registro.html')
            if not utils.isPasswordValid(pass_word):
                error = "La contraseña contiene caracteres no válidos"
                flash(error)
                print("contraseá")
                return render_template('Vista_Registro.html')
            yag = yg.SMTP('bloghub2@gmail.com','BlogHub1234**')
            yag.send(to=e_mail,subject="Activa tu cuenta",contents="Bienvenido a BlogHub"+ user_name)
            print("llegue")
            return render_template('Vista_Registro_Exitoso.html')
        return render_template('Vista_Registro.html')
    except :
        form = formRegistro()
        return render_template('Vista_Registro.html',form=form)



@app.route('/',methods=["POST","GET"])
def verificarusuario():

    if request.method == "POST":
        usr = escape(request.form["usuario"])
        pwd = escape(request.form["clave"])
        if usr == "Andres" and pwd == "12345":
            return render_template("inicio.html")
        else:
            form = formLogueo()
            flash("Usuario o contraseña errorneas")
            return render_template('login.html',form=form)
        
    else:
        nrfm =formLogueo()
        return render_template('login.html')
    


@app.route('/inicio')
def inicio():
    return render_template('inicio.html')
 



@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/BlogPropio')
def BlogPropio():
    return render_template('Vista_Blog_Propio.html')


@app.route('/BlogPublico')
def BlogPublico():
    return render_template('blog_publico.html')

@app.route('/Preview')
def Preview():
    return render_template('Vista_Previa.html')

if __name__ == '__main__':
    app.run(debug=True)



