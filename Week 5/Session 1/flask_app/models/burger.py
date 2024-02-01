from flask_app.config.mysqlconnection import connectToMySQL , DB

class Burger:
    def __init__(self , data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # CRUD
    # GET DATA (READ)
    # GET BY ID
    @classmethod
    def get_by_id(cls , data):
        """
            data = {
                'id': 1
            }
        """
        query = "SELECT * FROM burgers WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)

        burger = None

        if result != []:
            burger = cls(result[0])
        
        return burger

    # GET ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers;"
        results = connectToMySQL(DB).query_db(query)
        burgers = []
        for row in results:
            """
                row = {
                    'id': 1, 
                    'name': 'Burger 1', 
                    'bun': 'Bun 1', 
                    'meat': 'Meat 1', 
                    'calories': 500, 
                    'created_at': datetime.datetime(2024, 1, 30, 19, 37, 12), 
                    'updated_at': datetime.datetime(2024, 1, 30, 19, 37, 12)
                }
            """
            burger = cls(row)
            burgers.append(burger)

        return burgers
    
    # INSERT DATA (CREATE)
    @classmethod
    def create(cls , data):
        query = "INSERT INTO burgers (name , bun , meat , calories) VALUES (%(name)s , %(bun)s , %(meat)s , %(calories)s);"
        return connectToMySQL(DB).query_db(query , data)

    # MODIFY DATA (UPDATE)
    
    # DELETE DATA (DELETE)