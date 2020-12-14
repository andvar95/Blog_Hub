from flask import Flask,render_template,flash,request,redirect, url_for,session
import os
import yagmail as yg
import utils
from markupsafe import escape
from form import formLogueo, formRegistro
import hashlib
import sqlite3

app = Flask(__name__)
app.secret_key = os.urandom(24)

#variabless globales para  reenviar correo
global username1
global email1
username1 = ""
email1 = ""


#ventana Registro
@app.route('/registro', methods=["GET","POST"])
def registro():
    try:
        if request.method=="POST":
            # Ahora se actualizan los métodos de llamado a wtf
            form = formRegistro()
            global username1
            global email1
            # user_name = escape(request.form['usuario'])
            user_name = form.usuario.data 
            # username1 = escape(request.form['usuario'])
            username1 = form.usuario.data
            # e_mail = escape(request.form['correo'])
            # email1 = escape(request.form['correo'])
            e_mail = form.correo.data
            email1 = form.correo.data
            # pass_word = escape(request.form['clave'])
            pass_word = form.clave.data
            e = hashlib.md5(pass_word.encode())
            en = e.hexdigest()
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
            try:
                with sqlite3.connect('BlogHubDB.db') as con:
                    cur = con.cursor()
                    cur.execute('INSERT INTO Usuarios(email,username,password) VALUES(?,?,?)',(e_mail,user_name,en)) #Cuando son varios, es con paréntesis
                    con.commit()
                    return render_template('Vista_Registro_Exitoso.html')
            except:
                con.rollback()
        return render_template('Vista_Registro.html')
    except :
        form = formRegistro()
    return render_template('Vista_Registro.html',form=form)



#ventana de LOGIN
@app.route('/')
def login():
    form = formLogueo()
    if (form.validate_on_submit()):
        print("valido")
    return render_template('login.html',form= form)


@app.route('/',methods=["POST","GET"])
def verificarusuario():
    frm = formLogueo()
    if request.method == "POST":
        usr = escape(frm.usuario.data)
        pwd = escape(frm.clave.data)
        e = hashlib.md5(pwd.encode())
        en = e.hexdigest()
        with sqlite3.connect('BlogHubDB.db') as con:
            con.row_factory = sqlite3.Row #recibir bien la lista
            cur = con.cursor()
            #cur.execute("Select * FROM Usuario WHERE nombre = '"+user+"' AND clave= '"+pas+"';")
            print(usr)
            print(en)
            cur.execute("Select * FROM usuarios WHERE username = ? AND password=?",(usr,en))
          
            if cur.fetchall():
               
        
                session['user'] = usr
                
                return render_template("inicio.html",form=frm)
            else:
                form = formLogueo()
                flash("Usuario o contraseña erróneas")
                return render_template('login.html',form=form)
        
    else:
        frm = formLogueo()
        return render_template('login.html')
    
@app.route("/logout")
def logout():
    frm = formLogueo()
    if "user" in session:
        session.pop("user",None)
        return render_template("login.html",form=frm)
    else:
        return "Ya se cerró la sesión"

    


@app.route('/inicio',methods=["POST","GET"])
def inicio():
    frm = formLogueo()
    if "user" in session:
        print(frm.usuario.data)
        return render_template('inicio.html',form=frm)
    else:
        return "Acción no permitida <a href='/'>login</a>"



@app.route('/perfil')
def perfil():
    
    if "user" in session:
        datos = [session['user']]
        return render_template('perfil.html',datos=datos)
    else:
        return "Acción no permitida <a href='/'>login</a>"

@app.route('/BlogPropio')
def BlogPropio():
<<<<<<< HEAD
    if "user" in session:
        return render_template('Vista_Blog_Propio.html')
    else:
        return "Acción no permitida <a href='/'>login</a>"
=======
    return render_template('Vista_Blog_Propio.html')

@app.route('/CrearBlog')
def CrearBlog():
    return render_template('Vista_Crear_Blog.html')
>>>>>>> 8de896c03763898ce6fec160d477cd64205e0ca4

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



