from flask_app import app
from flask import render_template , redirect , request , jsonify
from flask_app.models.burger import Burger


@app.route('/')
def home():
    burgers = Burger.get_all()
    return render_template('index.html' , burgers = burgers)

@app.route('/burgers' , methods=['POST'])
def create_burger():
    # Get the data from the request.form
    data = request.form
    Burger.create(data)
    return redirect('/')