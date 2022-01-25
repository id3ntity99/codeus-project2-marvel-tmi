from flask import Blueprint
from flask import request
from flask import Response
from dotenv import load_dotenv
from pathlib import Path
from core import limiter
from modules.to_json import jsonify
from models.model import Avengers
from models.model import db
import json
import os


search_bp = Blueprint("search", __name__, url_prefix="/api")
limiter.limit("120/hour")(search_bp)

load_dotenv(verbose=True)
API_KEY = os.getenv("API_KEY")


@search_bp.route("/avengers/all")
def search_all():
    request_api_key = request.headers.get("X-API-key")
    if request_api_key == API_KEY:
        data = Avengers.query.all()
        data = jsonify(data)
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


@search_bp.route("/avengers")
def search_by_name():
    request_api_key = request.headers.get("X-API-key")
    if request_api_key == API_KEY:
        keyword = request.args.get("search")
        query_keyword = "%{}%".format(keyword)
        # Query the database
        data = (
            db.session.query(Avengers).filter(Avengers.name.like(query_keyword)).all()
        )
        # 데이터베이스 검색 결과가 없으면 아래 메시지를 리턴
        if not data:
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
