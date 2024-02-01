from flask_app import app
from flask_app.models.order import Order
from flask import render_template , redirect , request

@app.route('/orders/create/<int:id>')
def create_page(id):
    return render_template("create_order.html" , burger_id = id)

@app.route('/orders/create' , methods=['POST'])
def create():
    data = request.form
    Order.create(data)
    return redirect('/')