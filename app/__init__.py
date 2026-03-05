from flask import Flask
from flask_migrate import Migrate

from .config import Config
from .extensions import db, login_manager
from mpesa_accounting.app.models import User
from .models import User, Payment, MissionGoal, Transaction  # import your models



migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # -----------------------------
    # Initialize extensions
    # -----------------------------
    db.init_app(app)

    from . import models

    Migrate(app, db) # Ensure Migrate is initialized here
    login_manager.init_app(app)
    #migrate.init_app(app, db)

    login_manager.login_view = "auth.login"

    # -----------------------------
    # User loader (Flask-Login)
    # -----------------------------
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # -----------------------------
    # Register blueprints
    # -----------------------------
    from .routes.auth import auth_bp
    from .routes.mpesa import mpesa_bp
    from .routes.dashboard import dashboard_bp
    from .routes.mission import mission_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(mpesa_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(mission_bp)

    return app
