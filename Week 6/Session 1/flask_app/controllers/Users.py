from flask_app import app
from flask_app.models.user import User
from flask import render_template , request , redirect , session


@app.route('/')
def login_registration_page():
    return render_template('login_registration.html')

@app.route('/register' , methods=['POST'])
def register():
    data = request.form


    if User.validate_register(data):
        User.create(data)

    return redirect('/')

@app.route('/login' , methods = ['POST'])
def login():
    data = request.form
    if User.validate_login(data):
        session['logged_user_email'] = data['email']
        return redirect('/dashboard')
    
    return redirect('/')



@app.route('/dashboard')
def dashboard():
    if not 'logged_user_email' in session:
        return redirect('/')
    return "Welcome to dashboard"