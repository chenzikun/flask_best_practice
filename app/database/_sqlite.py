
import sqlite3
from flask.ctx import _app_ctx_stack as stack

class SQLite(object):
    """原生sqlite"""
    def __init__(self, app=None):
        self.app = app
        self.setting = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        sqlite_url = app.config.get("SQLITE_DATABASE")
        self.setting = sqlite_url
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def connect(self):
        return sqlite3.connect(self.setting)

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'sqlite3_db'):
            ctx.sqlite3_db.close()

    @property
    def connection(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'sqlite3_db'):
                ctx.sqlite3_db = self.connect()
            return ctx.sqlite3_db