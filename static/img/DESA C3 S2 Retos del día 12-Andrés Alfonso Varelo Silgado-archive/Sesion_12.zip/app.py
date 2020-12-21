from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('login.html')


@app.route('/forgot')
def forgot():
    return render_template('forgot.html')



if __name__ == '__main__':
    app.run(debug=True)


