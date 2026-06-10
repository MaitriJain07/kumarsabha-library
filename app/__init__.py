from pathlib import Path
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from app.extensions import db, login_manager
from config import Config

csrf = CSRFProtect()
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    instance_path = Path(app.instance_path)
    instance_path.mkdir(parents=True, exist_ok=True)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from app import models
    from app.admin import init_admin
    from app.auth import auth_bp
    from app.blueprints.books import books_bp
    from app.blueprints.main import main_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(auth_bp)

    init_admin(app)
    with app.app_context():
        db.create_all()
    return app
