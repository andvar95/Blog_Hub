from flask import Flask,render_template



app = Flask(__name__)

#ventana de LOGIN
@app.route('/')
def login():
    return render_template('login.html')



#ventana Registro
@app.route('/registro')
def registro():
    return render_template('Vista_Registro.html')



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

if __name__ == '__main__':
    app.run(debug=True)



