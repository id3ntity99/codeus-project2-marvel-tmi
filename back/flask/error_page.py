from flask import render_template
from flask import Response
from flask import Blueprint
from core import limiter
import json

error_bp = Blueprint("error", __name__)
limiter.limit("120/hour")(error_bp)


@error_bp.route("/")
def main_page():
    return render_template("index.html")


@error_bp.errorhandler(404)
def page_not_found(e):
    err_msg = {"success": False, "message": "요청하신 페이지를 찾을 수 없습니다", "code": 404}
    return Response(
        response=json.dumps(err_msg), status=404, mimetype="application/json"
    )
