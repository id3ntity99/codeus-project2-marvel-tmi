import json
from search import search_bp
from core import limiter
from flask import Flask, Response, render_template
from flask_cors import CORS
from models.model import db

# Flask App
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/avengers.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    limiter.init_app(app)

    # set CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Register blueprints
    app.register_blueprint(search_bp)

    @app.route("/")
    @limiter.limit("120/hour")
    def main_page():
        return render_template("index.html")

    @app.errorhandler(404)
    def page_not_found(e):
        err_msg = {"success": False, "message": "요청하신 페이지를 찾을 수 없습니다", "code": 404}
        return Response(
            response=json.dumps(err_msg), status=404, mimetype="application/json"
        )

    return app
