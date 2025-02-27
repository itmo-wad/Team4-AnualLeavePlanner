from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
import os
from .models import User

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.static_folder = 'static'
    app.config['SECRET_KEY'] = 'secret'
    mongo_host = os.getenv('MONGO_HOST', 'localhost')
    mongo_port = int(os.getenv('MONGO_PORT', 27017))
    mongo_db_name = os.getenv('MONGO_DB_NAME', 'app')

    app.config["MONGO_URI"] = f"mongodb://{mongo_host}:{mongo_port}/{mongo_db_name}"
    mongo.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    @login_manager.user_loader
    def load_user(username):
        u = mongo.db.users.find_one({'username': username})
        if not u:
            return None
        return User(username=u['username'], email=u.get('email', ''), isManager=u.get('isManager', False))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
