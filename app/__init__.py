from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .routes.auth import auth_bp
    from .routes.dashboard import dashboard_bp
    from .routes.superadmin import superadmin_bp
    from .routes.invoice import invoice_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(superadmin_bp, url_prefix="/superadmin")
    app.register_blueprint(invoice_bp, url_prefix="/invoice")

    return app
