from flask import Flask
from celery import Celery
from .utils.celery_util import init_celery
from .utils.mail_handler import init_mail

import os

static_path = os.path.abspath(
    os.path.join(
        os.path.join(
            os.path.dirname(__file__), ".."), "static")
)

celery = Celery()


class Application(Flask):
    def __init__(self, environment):
        # TODO LOG,db,
        super(Application, self).__init__(__name__, static_folder=static_path)

        #: celery配置
        self.config.update(
            CELERY_BROKER_URL='redis://127.0.0.1:6379',
            CELERY_RESULT_BACKEND='redis://127.0.0.1:6379'
        )
        init_celery(self, celery)

        # mail
        init_mail(self)

    def _init_blueprint(self, *blueprints):
        for blueprint in blueprints:
            self.register_blueprint(blueprint)

    def register_processors(self, *context_processors):
        for context_processor in context_processors:
            self.context_processor(context_processor)


def create_app(environment):
    app = Application(environment)
    if environment == "dev":
        app.debug = True

    from app.views.homepage import homepage_bp
    from app.apis.api import api_bp
    blueprints = [homepage_bp, api_bp]
    app._init_blueprint(*blueprints)

    from .ctx import user_context_processor
    context_processors = [user_context_processor]
    # app.register_processors(*context_processors)



    return app
