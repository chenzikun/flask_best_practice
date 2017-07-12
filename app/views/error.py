from flask import Blueprint, render_template
from . import templates_path
import os

error_templates =os.path.abspath(
    os.path.join(templates_path, "errors")
)

error_bp = Blueprint("errors", __name__, template_folder=error_templates)


@error_bp.app_errorhandler(404)
def handle_404(err):
    return render_template("404.html", err=err), 404


@error_bp.app_errorhandler(500)
def handle_404(err):
    return render_template("500.html", err=err), 500