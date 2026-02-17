from flask import Flask
from .config import Config
from .extensions import db
from .extensions import db, login_manager
from .models.user import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes import auth, mpesa, dashboard, mission
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(mpesa.mpesa_bp)
    app.register_blueprint(dashboard.dashboard_bp)
    app.register_blueprint(mission.mission_bp)

    return app
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes.mpesa import mpesa_bp
    from .routes.dashboard import dashboard_bp
    from .routes.mission import mission_bp

    app.register_blueprint(mpesa_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(mission_bp)

    return app
