import os

from flask import Blueprint, render_template, url_for, current_app, redirect, abort

# html加上homepage.index
homepage_bp = Blueprint("homepage", __name__)


@homepage_bp.route("/")
def index():
    return render_template("homepage.html")


@homepage_bp.route("/Introduction/")
def introduction():
    return "Introduction"


@homepage_bp.errorhandler(404)
def handle_404(err):
    return "404"


