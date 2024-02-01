from flask_app.models.burger import Burger
from flask_app.config.mysqlconnection import connectToMySQL , DB

class Order:
    def __init__(self , data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.quantity = data['quantity']
        self.order_date = data['order_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.burger = None

    # Get burger by id
    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM orders JOIN burgers ON orders.burger_id = burgers.id WHERE orders.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query , data)
        # Initialize the attributes of the order instance (Using constructor)
        # Create an instance of the burger class
        # Set the burger attribute of the order instance equal to the burger instance
        order = None
        if results != []:
            burger_data = {
                'id': results[0]['burgers.id'],
                'name': results[0]['name'],
                'bun': results[0]['bun'],
                'meat': results[0]['meat'],
                'calories': results[0]['calories'],
                'created_at': results[0]['burgers.created_at'],
                'updated_at': results[0]['burgers.updated_at'],
            }
            burger = Burger(burger_data)
            order = cls(results[0])
            order.burger = burger
        return order
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders JOIN burgers ON orders.burger_id = burgers.id;"
        results = connectToMySQL(DB).query_db(query)

        orders = []
        for item in results:
            burger_data = {
                'id': item['burgers.id'],
                'name': item['name'],
                'bun': item['bun'],
                'meat': item['meat'],
                'calories': item['calories'],
                'created_at': item['burgers.created_at'],
                'updated_at': item['burgers.updated_at'],
            }
            order = cls(item)
            order.burger = Burger(burger_data)
            orders.append(order)
        return orders
    
    @classmethod
    def create(cls , data):
        query = "INSERT INTO orders (customer_name , quantity , order_date , burger_id) VALUES (%(customer_name)s , %(quantity)s , %(order_date)s , %(burger_id)s);"
        return connectToMySQL(DB).query_db(query , data)
    
    @classmethod
    def update(cls ,data):
        query = "UPDATE order SET customer_name = %(customer_name)s , quantity = %(quantity)s , order_date =%(order_date)s , burger_id = %(burger_id)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)
    

    @classmethod
    def delete(cls , data):
        query = "DELETE FROM orders WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)

        