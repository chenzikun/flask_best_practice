from flask import Flask
from celery import Celery
from .utils.celery_util import init_celery
import os

static_path = os.path.abspath(
    os.path.join(
        os.path.join(
            os.path.dirname(__file__), ".."), "static")
)

class Application(Flask):
    def __init__(self, environment):
        # TODO LOG,db,
        super(Application, self).__init__(__name__, static_folder=static_path)
        self.config.update(
            CELERY_BROKER_URL='redis://127.0.0.1:6379',
            CELERY_RESULT_BACKEND='redis://127.0.0.1:6379'
        )
        self.celery = Celery()
        init_celery(self, self.celery)

    def _init_blueprint(self, *blueprints):
        for blueprint in blueprints:
            self.register_blueprint(blueprint)


def create_app(environment):
    app = Application(environment)

    from app.views.homepage import homepage_bp
    from app.apis.api import api_bp
    blueprints = [homepage_bp, api_bp]
    app._init_blueprint(*blueprints)
    return app
