from jsonrpc import dispatcher, JSONRPCResponseManager

from flask import Blueprint, request, Response

api_bp = Blueprint("demo_api", __name__, url_prefix="/api/")


@api_bp.route('', methods=["POST"])
def json_api():
    response_ = JSONRPCResponseManager.handle(request.data, dispatcher)
    response = Response(response=response_.json, mimetype="application/json", content_type="application/json")
    return response


@dispatcher.add_method
def show(**kwargs):
    return {"name": "陈子坤"}
