from modules.DBHandler.handler import MyDatabase
from models.avengers import Avengers
from flask import Flask, request, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import os
import json


app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["120 per hour"])
AVG_DB_URL = "./db/avengers.sqlite"
load_dotenv(verbose=True)
API_KEY = os.getenv("API_KEY")


@app.route("/api/avengers/all")
@limiter.limit("120/hour")
def search_all():
    request_api_key = request.headers.get("X-API-key")
    if request_api_key == API_KEY:
        database = MyDatabase()
        database.connect_db(AVG_DB_URL)
        data = database.select_all(Avengers)
        return Response(response=data, status=200, mimetype="application/json")
    elif request_api_key is None:
        err_msg = {"success": False, "message": "API key를 요청 헤더에 포함시켜야 합니다."}
        return Response(
            response=json.dumps(err_msg), status=200, mimetype="application/json"
        )
    else:
        err_msg = {"success": False, "message": "잘못된 API key 입니다."}
        return Response(
            response=json.dumps(err_msg), status=400, mimetype="application/json"
        )


@app.route("/api/avengers")
@limiter.limit("30/hour")
def search_by_name():
    request_api_key = request.headers.get("X-API-key")
    if request_api_key == API_KEY:
        keyword = request.args.get("search")
        database = MyDatabase()
        database.connect_db(AVG_DB_URL)
        data = database.select_where_name_is(Avengers, keyword)
        return Response(response=data, status=200, mimetype="application/json")
    elif request_api_key is None:
        err_msg = {"success": False, "message": "API key를 요청 헤더에 포함시켜야 합니다."}
        return Response(
            response=json.dumps(err_msg), status=200, mimetype="application/json"
        )
    else:
        err_msg = {"success": False, "message": "잘못된 API key 입니다."}
        return Response(
            response=json.dumps(err_msg), status=400, mimetype="application/json"
        )
