import os

from flask import Blueprint, render_template, url_for

template_path = os.path.abspath(
    os.path.join(
        os.path.join(
            os.path.join(
                os.path.dirname(__file__), ".."), ".."), "templates")
)

# html加上homepage.index
homepage_bp = Blueprint("homepage", __name__, template_folder=template_path)


@homepage_bp.route("/")
def index():
    return render_template("homepage.html")


@homepage_bp.route("/Introduction")
def introduction():
    return "Introduction!"
