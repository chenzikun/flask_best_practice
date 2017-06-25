from flask import Flask


class Application(Flask):
    def __init__(self):
        super(Application, self).__init__(__name__)

    def _init_blueprint(self, *blueprints):
        for blueprint in blueprints:
            self.register_blueprint(blueprint)


def create_app():
    app = Application()

    from app.homepage.view import homepage_bp
    blueprints = [homepage_bp]
    app._init_blueprint(*blueprints)
    return app
