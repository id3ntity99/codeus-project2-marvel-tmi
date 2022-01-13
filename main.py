from modules.DBHandler.handler import MyDatabase
from models.avengers import Avengers
from flask import Flask, request, Response


app = Flask(__name__)
DB_URL = "./db/avengers.sqlite"


@app.route("/api/avengers/all")
def search_all():
    database = MyDatabase()
    database.connect_db(DB_URL)
    data = database.select_all(Avengers)
    return Response(response=data, status=200, mimetype="application/json")


@app.route("/api/avengers")
def search_by_name():
    keyword = request.args.get("search")
    database = MyDatabase()
    database.connect_db(DB_URL)
    data = database.select_where_name_is(Avengers, keyword)
    return Response(response=data, status=200, mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
