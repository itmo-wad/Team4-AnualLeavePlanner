from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import string
import random 

# Taken from https://stackoverflow.com/questions/54992412/flask-login-usermixin-class-with-a-mongodb
class User(UserMixin):
    def __init__(self, username, email, isManager=False):
        self.username = username
        self.email = email
        self.isManager = isManager

    def get_id(self):
        return self.username

    @property
    def id(self):
        return self.username

    @staticmethod
    def generate_password(password):
        return generate_password_hash(password)
    
    @staticmethod
    def generate_employee_password():
        """Generates a secure random password"""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(10))
   
    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)
    
    @staticmethod
    def check_password(password_hash, password):
        return check_password_hash(password_hash, password)
