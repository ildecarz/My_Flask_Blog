from flask import Flask 
from flask import render_template 
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'prueba'

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/calculadora')
def Calc():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug = True)


