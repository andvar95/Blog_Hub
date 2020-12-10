from flask import Flask,render_template,flash,request,redirect, url_for
import os
import yagmail as yg
import utils


app = Flask(__name__)
app.secret_key= os.urandom(24)

global username1
global email1
username1 = ""
email1 = ""
#ventana de LOGIN
@app.route('/')
def login():
    return render_template('login.html')


#ventana Registro
@app.route('/registro', methods=['GET','POST'])
def registro():
    try:
        if request.method=="POST":
            global username1
            global email1
            user_name = request.form['user']
            username1 = request.form['user']
            e_mail = request.form['email']
            email1 = request.form['email']
            pass_word = request.form['password']
            error = None
            if not utils.isUsernameValid(user_name):
                error = "El usuario debe ser alfanumérico"
                flash(error)
                return render_template('Vista_Registro.html')
            if not utils.isEmailValid(e_mail):
                error = "Email no válido"
                flash(error)
                return render_template('Vista_Registro.html')
            if not utils.isPasswordValid(pass_word):
                error = "La contraseña contiene caracteres no válidos"
                flash(error)
                return render_template('Vista_Registro.html')
            yag = yg.SMTP('bloghub2@gmail.com','BlogHub1234**')
            yag.send(to=e_mail,subject="Activa tu cuenta",contents="Bienvenido a BlogHub "+user_name)
            return render_template('Vista_Registro_Exitoso.html')
        return render_template('Vista_Registro.html')
    except :
        return render_template('Vista_Registro.html')



@app.route('/verificarusuario',methods=["POST","GET"])
def verificarusuario():
   if request.method == "POST":
        
        user = request.form["usuario"]
        password = request.form["password"]
        
        if user == "Andres" and password=="12345":
            return render_template('inicio.html')

        else:
            flash("Usuario no existe")
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

@app.route('/reenviar',methods=['GET','POST'])
def reenviar_codigo():
    # try:
        global email1
        global username1
        yag = yg.SMTP('bloghub2@gmail.com','BlogHub1234**')
        yag.send(to=email1,subject="Activa tu cuenta",contents="Bienvenido a BlogHub "+username1)
        return render_template('Vista_Registro_Exitoso.html')
    # except :
    #     return render_template('Vista_Registro_Exitoso.html')

if __name__ == '__main__':
    app.run(debug=True)



