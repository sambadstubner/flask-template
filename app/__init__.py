from flask import Flask

from config import Config
from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.blueprint import bp as blueprint_bp

    app.register_blueprint(blueprint_bp)

    @app.route("/test")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    return app
