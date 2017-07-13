from flask import Blueprint, request
from flask_login import login_required

auth_bp = Blueprint("auth", __name__)

from ..models.user import User


@auth_bp.route("/login", methods=["GET", "POST"])
@login_required
def login():
    if request.form.get("submit"):
        username = request.form.get("username")
        password = request.form.get("password")


@auth_bp.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    pass


@auth_bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    pass
