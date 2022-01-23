from models.model import Avengers
from models.model import db
from flask import Flask, request, Response, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import json


def jsonify(data):
    temp = []
    for row in data:
        temp_dict = {
            "success": True,
            "id": row.id,
            "url": row.url,
            "name": row.name,
            "appearances": row.appearances,
            "gender": row.gender,
            "year": row.year,
            "years_since_joining": row.years_since_joining,
            "description": row.note if row.note != "NA" else None,
        }
        temp.append(temp_dict)
    return json.dumps(temp)


# Flask App
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/avengers.sqlite"
    db.init_app(app)

    # load .env
    load_dotenv(verbose=True)

    # set rate limit
    limiter = Limiter(app, key_func=get_remote_address, default_limits=["120 per hour"])

    # set CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # load api key from .env
    API_KEY = os.getenv("API_KEY")
    AVG_DB_URL = "./db/avengers.sqlite"

    @app.route("/")
    @limiter.limit("120/hour")
    def main_page():
        return render_template("index.html")

    @app.route("/api/avengers/all")
    @limiter.limit("120/hour")
    def search_all():
        request_api_key = request.headers.get("X-API-key")
        if request_api_key == API_KEY:
            data = Avengers.query.all()
            data = jsonify(data)
            print(data)
            return Response(response=data, status=200, mimetype="application/json")
        elif request_api_key is None:
            err_msg = {
                "success": False,
                "message": "API key를 요청 헤더에 포함시켜야 합니다.",
            }
            return Response(
                response=json.dumps(err_msg), status=400, mimetype="application/json"
            )
        else:
            err_msg = {
                "success": False,
                "message": "잘못된 API key 입니다.",
            }
            return Response(
                response=json.dumps(err_msg), status=400, mimetype="application/json"
            )

    @app.route("/api/avengers")
    @limiter.limit("30/hour")
    def search_by_name():
        request_api_key = request.headers.get("X-API-key")
        if request_api_key == API_KEY:
            keyword = request.args.get("search")
            query_keyword = "%{}%".format(keyword)
            # Query the database
            data = (
                db.session.query(Avengers)
                .filter(Avengers.name.like(query_keyword))
                .all()
            )
            # 데이터베이스 검색 결과가 없으면 아래 메시지를 리턴
            if not data:
                print("there're no data")
                err_msg = {"success": False, "message": "요청하신 데이터를 찾을 수 없습니다"}
                return Response(
                    response=json.dumps(err_msg),
                    status=200,
                    mimetype="application/json",
                )
            # 데이터베이스 검색 결과가 존재하면 JSON 포맷으로 리턴
            data = jsonify(data)
            return Response(response=data, status=200, mimetype="application/json")
        elif request_api_key is None:
            err_msg = {
                "success": False,
                "message": "API key를 요청 헤더에 포함시켜야 합니다.",
                "code": 400,
            }
            return Response(
                response=json.dumps(err_msg), status=400, mimetype="application/json"
            )
        else:
            err_msg = {"success": False, "message": "잘못된 API key 입니다.", "code": 400}
            return Response(
                response=json.dumps(err_msg), status=400, mimetype="application/json"
            )

    @app.errorhandler(404)
    def page_not_found(e):
        err_msg = {"success": False, "message": "요청하신 페이지를 찾을 수 없습니다", "code": 404}
        return Response(
            response=json.dumps(err_msg), status=404, mimetype="application/json"
        )

    return app
