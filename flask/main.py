from modules.DBHandler.handler import MyDatabase
from models.avengers import Avengers
from flask import Flask, request, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["120 per hour"])
AVG_DB_URL = "./db/avengers.sqlite"


@app.route("/api/avengers/all")
@limiter.limit("120/hour")
def search_all():
    database = MyDatabase()
    database.connect_db(AVG_DB_URL)
    data = database.select_all(Avengers)
    return Response(response=data, status=200, mimetype="application/json")


@app.route("/api/avengers")
@limiter.limit("30/hour")
def search_by_name():
    keyword = request.args.get("search")
    database = MyDatabase()
    database.connect_db(AVG_DB_URL)
    data = database.select_where_name_is(Avengers, keyword)
    return Response(response=data, status=200, mimetype="application/json")
