from flask import Flask,render_template,flash,request,redirect, url_for
import os



app = Flask(__name__)
app.secret_key= os.urandom(24)


#ventana de LOGIN
@app.route('/')
def login():
    return render_template('login.html')




#ventana Registro
@app.route('/registro')
def registro():
    return render_template('Vista_Registro.html')



@app.route('/inicio', methods=["POST","GET"])
def inicio():
    if request.method == "POST":
        
        user = request.form["usuario"]
        password = request.form["password"]
        
        if user == "Andres" and password=="12345":
            return render_template('inicio.html')

        else:
            flash("Usuario no existe")
            return render_template('login.html')



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



