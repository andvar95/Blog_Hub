from flask import Flask,render_template,flash,request,redirect, url_for,session
import os
import yagmail as yg
import utils
from markupsafe import escape
from form import formLogueo, formRegistro
import hashlib
import sqlite3
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash, check_password_hash
import random

# Función para realizar conexión a la DB
def get_db_connection():
    conn = sqlite3.connect('BlogHubDB.db')
    conn.row_factory = sqlite3.Row
    return conn
# Función para obtener id del post

def get_post(post_id):
    conn = get_db_connection()
    #posts = hawai, id = afrax
    post = conn.execute('SELECT * FROM hawai WHERE afrax = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

# def get_post_name(post_name):
#     with sqlite3.connect('BlogHubDB.db') as con:
#         cur = con.cursor()
#         cur.execute('SELECT * FROM posts WHERE id = ?',
#                         (post_id,)).fetchone()
#         post = cur.fetchone()
#         if post is None:
#             abort(404)
#         return post

app = Flask(__name__)
app.secret_key = os.urandom(24)

#variabless globales para  reenviar correo
global username1
global email1
tittle = ""
content = ""
date = ""
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
            user_name = escape(form.usuario.data)
            # username1 = escape(request.form['usuario'])
            username1 = escape(form.usuario.data)
            # e_mail = escape(request.form['correo'])
            # email1 = escape(request.form['correo'])
            e_mail = escape(form.correo.data)
            email1 = escape(form.correo.data)
            pass_word = escape(form.clave.data)
            pwd_enc = generate_password_hash(pass_word)
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
            
            number = hex(random.getrandbits(256))[2:]
            
            yag = yg.SMTP('bloghub2@gmail.com','BlogHub1234**')
        
            yag.send(to=e_mail,subject="Activa tu cuenta",contents="Bienvenido a BlogHub  "+user_name+" Su código de activación es "+url_for('activate',_external=True)+'?auth='+number)
        
            try:
                with sqlite3.connect('BlogHubDB.db') as con:
                    cur = con.cursor()
                    #usuarios = uribeparaco, email = rovin, username= luffy, password = nami
                    cur.execute('INSERT INTO uribeparaco(rovin,luffy,nami,soxo) VALUES(?,?,?,?)',(e_mail,user_name,pwd_enc,0)) #Cuando son varios, es con paréntesis
                    con.commit()
                    cur.execute('INSERT INTO validacion(codigo,estado,email) VALUES(?,?,?)',(number,0,e_mail)) #Cuando son varios, es con paréntesis
                    con.commit()
                    return render_template('Vista_Registro_Exitoso.html')
            except:
                con.rollback()
        return render_template('Vista_Registro.html')
    except :
        
        form = formRegistro()
    return render_template('Vista_Registro.html',form=form)

@app.route("/activate",methods=["GET","POST"])
def activate():
    code = request.args.to_dict()
    print(code)
    try:
        with sqlite3.connect('BlogHubDB.db') as con:
            
            cur = con.cursor()
            user = cur.execute("SELECT email FROM validacion WHERE codigo = ?",[code['auth']]).fetchone()
            print(user)
            if user:
               
                cur.execute("UPDATE uribeparaco SET soxo=? WHERE rovin=?",[1,user[0]])
                cur.execute(f"DELETE from validacion WHERE codigo = '{code['auth']}'")
                con.commit()
                return render_template("activate.html",name=user)


    except:
        return "error activando"


    
    

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
        
        with sqlite3.connect('BlogHubDB.db') as con:
            con.row_factory = sqlite3.Row #recibir bien la lista
            cur = con.cursor()
            con.row_factory = sqlite3.Row
            cur1 = con.cursor()
            cur1 = con.cursor()
            #posts = hawai
            cur1.execute("SELECT * FROM hawai") 
            row = cur1.fetchall() #para traer un solo registro. Fetchall para traer todos
            
            #cur.execute("Select * FROM Usuario WHERE nombre = '"+user+"' AND clave= '"+pas+"';")
            #print(usr)
            #print(pwd)
            #usuarios = uribeparaco, username = luffy
            user1 = cur.execute(f"Select * FROM uribeparaco WHERE luffy ='{usr}' ").fetchall()
            print(user1[0][4])
            if user1 and check_password_hash(user1[0][2],pwd) and user1[0][4] != None:
                session['user'] = usr
                
                return render_template("inicio.html",form=frm,row=row)
            elif user1 and user1[0][4] != 1:
                form = formLogueo()
                flash("Activa tu cuneta")
                return render_template('login.html',form=form)
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


@app.route('/inicio',methods=["GET","POST"])
def inicio():
    if "user" in session:
        frm = formLogueo()
        print(session['user'])
        # try:
        with sqlite3.connect('BlogHubDB.db') as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            #posts = hawai
            cur.execute("SELECT * FROM hawai") 
            row = cur.fetchall()
            return render_template('inicio.html',row = row, form=frm)
        #except: 
            # con.rollback() 
        return render_template('inicio.html',form=frm)
    else:
        return "Acción no permitida <a href='/'>login</a>"

@app.route('/perfil')
def perfil():
    
    if "user" in session:
        datos = session['user']
        with sqlite3.connect('BlogHubDB.db') as con:
            con.row_factory = sqlite3.Row
            cur1 = con.cursor()
            #email = rovin username=luffy usuarios = uribeparaco
            cur1.execute("SELECT rovin FROM uribeparaco where luffy = ?",[datos])
            email2 = cur1.fetchone()
            id_usuario=""
            for i in email2:
                id_usuario=i[:]
            cur = con.cursor()
            #posts = hawai,  id_usuario= waptro
            cur.execute("SELECT * FROM hawai where waptro = ?",[id_usuario]) 
            row = cur.fetchall()
        return render_template('perfil.html',datos=datos, row=row,email2=email2)
    else:
        return "Acción no permitida <a href='/'>login</a>"


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html',post=post)

@app.route('/edit/<int:post_id>',methods=['GET','POST'])
def edit_post(post_id):
    post = get_post(post_id)
    if "user" in session:
        datos=session['user']
        if request.method == 'POST':
            titulo = request.form['titulo']
            cuerpo = request.form['body_blog']
            if not titulo:
                flash('Se requiere título')
            elif not cuerpo:
                flash('Se requiere cuerpo')            
            else:
                conn = get_db_connection()
                conn1= get_db_connection()
                post = conn1.execute('SELECT rovin FROM uribeparaco WHERE luffy = ?',[datos]).fetchone()
                print(post[0])
                conn.execute('UPDATE hawai SET kuadno = ?, tavle = ? WHERE afrax = ?',
                            (titulo, cuerpo, post_id))
                conn.commit()
                conn.close()
                return redirect(url_for('perfil'))
    else:
        return "Acción no permitida <a href='/'>login</a>"
    return render_template('Vista_Blog_Propio.html', post=post)
    
@app.route('/BlogPropio')
def BlogPropio():
    if "user" in session:
        return render_template('Vista_Blog_Propio.html')
    else:
        return "Acción no permitida <a href='/'>login</a>"
    return render_template('Vista_Blog_Propio.html')

@app.route('/CrearBlog',methods=['GET','POST'])
def CrearBlog():
    if "user" in session:
        datos=session['user']
        if request.method == 'POST':
            titulo = request.form['titulo']
            cuerpo = request.form['body_blog']
            if not titulo:
                flash('Se requiere título')
            elif not cuerpo:
                flash('Se requiere cuerpo')            
            else:
                conn = get_db_connection()
                conn1= get_db_connection()
                #email = rovin usuarios = uribeparaco username=luffy
                post = conn1.execute('SELECT rovin FROM uribeparaco WHERE luffy = ?',[datos]).fetchone()
                print(post[0])
                #posts = hawai, titulo =kuadno, id_usuario = waptro, cuerpo= tavle, estado = mabida, fecha= moan 
                conn.execute('INSERT INTO hawai (kuadno, waptro, tavle,mabida) VALUES (?, ?, ?, ?)',
                            (titulo, post[0], cuerpo, 1))
                conn.commit()
                conn.close()
                return redirect(url_for('perfil'))
    else:
        return "Acción no permitida <a href='/'>login</a>"
    return render_template('Vista_Crear_Blog.html')


@app.route('/BlogPublico')
def BlogPublico():
    return render_template('blog_publico.html')

@app.route('/Preview/<int:post_id>')
def Preview(post_id):
    post = get_post(post_id)
    return render_template('Vista_Previa.html',post=post)

@app.route('/delete/<int:post_id>',methods=('POST','GET'))
def delete_post(post_id):
    post = get_post(post_id)
    conn = get_db_connection()
    conn.execute('DELETE FROM hawai WHERE afrax = ?', (post_id,))
    conn.commit()
    conn.close()
    flash('"{}" Fue borrado existosamente!'.format(post['kuadno']))
    return redirect(url_for('perfil'))

@app.route('/Preview/new/',methods=['GET','POST'])
def Preview_new():
    if "user" in session:
        return render_template('Vista_Previa_N.html')
    else:
        return "Acción no permitida <a href='/'>login</a>"
    return render_template('Vista_Crear_Blog.html')

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

@app.route("/cambiarpass/<int:source>",methods=["GET","POST"])
def cambiarpass(source):
    form = formRegistro()
    ventanas = ['vista_Cambiar_password.html','recuperar.html'] 
    retorno =['/perfil','/']
    if request.method =="POST":
        email = form.correo.data
        newpass = form.clave.data 
        with sqlite3.connect('BlogHubDB.db') as con:
            con.row_factory = sqlite3.Row #recibir bien la lista
            cur = con.cursor()
            #usuarios = uribeparaco, email= rovin
            user = cur.execute(f"SELECT * FROM uribeparaco WHERE  rovin= '{email}'").fetchall() 
            
            if user and  utils.isPasswordValid(newpass) :
                newpass_enc = generate_password_hash(newpass)
                #usuario = uribeparaco, password = nami , email= rovin 
                cur.execute("UPDATE  uribeparaco SET nami=? WHERE rovin=?",[newpass_enc,email])
                print(retorno[source])
                return "Cambiado con exito <a href='"+retorno[source]+"'>Volver </a>"
            else:
                flash("Contraseña con caracteres no permitidos")
                return render_template(ventanas[source],form=form,action=source)
    else: 
        return render_template(ventanas[source],form=form,action=source)

if __name__ == '__main__':
    app.run(debug=True)



