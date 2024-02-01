from flask_app import app
from flask import render_template , redirect , request 
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

# Handle Deleting a burger
@app.route('/burgers/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    Burger.delete(data)
    return redirect('/')


# Handle Taking us to a page where we can update a burger
@app.route('/burgers/update/<int:id>')
def update_page(id):
    data = {
        'id': id
    }
    burger = Burger.get_by_id(data)
    return render_template("update_burger.html" , burger = burger)

# Handle updating the burger
@app.route('/burgers/update' , methods=['POST'])
def update():
    Burger.update(request.form)
    return redirect('/')


# Handle taking us to a page that displays the burger's data
@app.route('/burgers/view/<int:id>')
def display(id):
    data = {
        'id': id
    }
    burger = Burger.get_by_id(data)
    return render_template("view_burger.html" , burger = burger)