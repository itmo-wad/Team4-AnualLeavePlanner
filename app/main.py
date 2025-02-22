from flask import render_template, redirect, request, Blueprint, flash
from flask_login import login_user, login_required, logout_user, current_user
from . import mongo

main = Blueprint('main', __name__)

# We probably want to reder main page at /, maybe dynamic page depending on user type
@main.route('/')
@login_required
def index():
    user = mongo.db.users.find_one({'username': current_user.username})
    return render_template('index.html', user=user)
    # if current_user.is_authenticated:
    #     return redirect('/profile')
    # return redirect('/login')