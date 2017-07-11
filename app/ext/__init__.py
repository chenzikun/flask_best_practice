from flask import current_app

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

class Extension(object):
    def __init__(self, app=None):
        self._app = app
        if app:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions.update({'extension': self, })

    @property
    def app(self):
        return self._app or current_app

    def config(self, key, default=None):
        key = 'EXTENSION_{}'.format(key.upper())
        if default:
            return self.app.config.get(key, default)
        return self.app.config[key]

    @property
    def namespace(self):
        return self.config('namespace', 'extension')
