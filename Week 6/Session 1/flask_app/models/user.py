from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.config.mysqlconnetion import DB , connectToMySQL
from flask import flash

import re

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:

    def __init__(self, data):
        self.id = data['id']
        self.fullname = data['fullname']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Registering new Users
    @classmethod
    def create(cls , data):
        """
            data = {
                'fullname': value,
                'email': value,
                'password': value
            }
        """
        print(type(data))
        encrypted_password = bcrypt.generate_password_hash(data['password'])
        # Data an immutable dictionary (We can't change the values inside of it)
        # Casting
        data = dict(data)
        # Data as a mutable dictionary
        data['password'] = encrypted_password
        print(type(data))

        query = "INSERT INTO users (fullname , email , password) VALUES(%(fullname)s , %(email)s , %(password)s);"
        return connectToMySQL(DB).query_db(query , data)

    # Registration Validation
    @staticmethod
    def validate_register(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if len(data['fullname']) <= 3:
            flash("Full name must be longer tan 3 characters.")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be longer than 8 characters.")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("The passwords must match")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email")
            is_valid = False
        if user_in_db:
            flash("A user with this email already exists.")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email")
            is_valid = False
        if not user_in_db:
            flash("No user with this email exists.")
            is_valid = False
        elif not bcrypt.check_password_hash(user_in_db.password , data['password']):
            flash("Incorrect Password")
            is_valid = False
        return is_valid

    


    @classmethod
    def get_by_email(cls , data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query , data)

        # result = [] => Falsy Value
        # result = [...] Truthy Value

        if result:
            return cls(result[0])
        
        return False