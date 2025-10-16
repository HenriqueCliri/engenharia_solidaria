from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = '893f5f60-2ca8-4285-8af0-51b9fd9d43f7'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.instance_path}/database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app