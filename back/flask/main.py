from views.search import search_bp
from views.error_page import error_bp
from core import limiter
from flask import Flask
from flask_cors import CORS
from models.model import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/avengers.sqlite"
    # configuration
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize sqlalchemy and flask-limiter
    db.init_app(app)
    limiter.init_app(app)

    # set CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Register blueprints
    app.register_blueprint(search_bp)
    app.register_blueprint(error_bp)

    return app
