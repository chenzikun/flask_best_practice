from flask import Blueprint, request

auth_bp = Blueprint("auth", __name__)

from ..models.user import User


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.form.get("submit"):
        username = request.form.get("username")
        password = request.form.get("password")
