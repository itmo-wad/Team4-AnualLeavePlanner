from flask import render_template, redirect, request, Blueprint, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import mongo

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    # Check for fields
    if not username or not password:
        return redirect('/login')
    user = mongo.db.users.find_one({'username': username, 'password': password})
    if user:
        login_user(User(username=user['username']))
        return redirect('/')
    else:
        flash('Invalid username or password')
        return redirect('/login')


@auth.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@auth.route('/register', methods=['POST'])
def register_post():
    role = request.form.get('role')
    username = request.form.get('username')
    password = request.form.get('password')
    # Check for fields
    if not role or not username or not password:
        return redirect('/login')
    # TODO: check if user exists, password length, password hashing

    mongo.db.users.insert_one({'isManager': role, 'username': username, 'password': password})
    flash('User registered successfully')
    return redirect('/login')