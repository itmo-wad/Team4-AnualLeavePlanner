from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# Taken from https://stackoverflow.com/questions/54992412/flask-login-usermixin-class-with-a-mongodb
class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username

    @property
    def id(self):
        return self.username

    @staticmethod
    def generate_password(password):
        return generate_password_hash(password)

    @staticmethod
    def check_password(password_hash, password):
        return check_password_hash(password_hash, password)
