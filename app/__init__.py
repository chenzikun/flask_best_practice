from flask import Flask
from celery import Celery
from .utils.celery_util import init_celery


class Application(Flask):
    def __init__(self):
        super(Application, self).__init__(__name__, static_folder=None)
        self.config.update(
            CELERY_BROKER_URL='redis://127.0.0.1:6379',
            CELERY_RESULT_BACKEND='redis://127.0.0.1:6379'
        )
        self.celery = self.make_celery()

    def _init_blueprint(self, *blueprints):
        for blueprint in blueprints:
            self.register_blueprint(blueprint)

    def make_celery(self):
        celery = Celery(self.import_name, broker=self.config['CELERY_BROKER_URL'])
        celery.conf.update(self.config)
        TaskBase = celery.Task

        class ContextTask(TaskBase):
            abstract = True

            def __call__(self, *args, **kwargs):
                with self.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)

        celery.Task = ContextTask
        return celery


def create_app():
    app = Application()

    from app.views.homepage import homepage_bp
    from app.apis.api import api_bp
    blueprints = [homepage_bp, api_bp]
    app._init_blueprint(*blueprints)
    return app
