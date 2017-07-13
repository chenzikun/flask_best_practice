import os

from celery import Celery
from flask import Flask
from flask_login import LoginManager

from config import config
from .database._mysql import MysqlDatabase
from .database._redis import RedisDatabase
from .database._sqlalchemy import SqlalchemyDatabase
from .database._sqlite import SQLite
from .utils.celery_util import init_celery
from .utils.mail_handler import init_mail

app_dir = os.path.join(os.path.dirname(__file__), "..")

static_path = os.path.abspath(
    os.path.join(
        app_dir, "static")
)

templates_path = os.path.abspath(
    os.path.join(
        app_dir, "templates")
)

celery = Celery()


class Database():
    def __init__(self, app=None):
        self.app = app
        self.db = SqlalchemyDatabase()
        self.redis = RedisDatabase()
        self.sqlite = SQLite()
        self.mysql = MysqlDatabase()

        if app:
            self.init_app(app)

    def init_app(self, app):
        """
        初始化数据库配置
        """
        self.db.init_app(app)
        # self.redis.init_app(app)
        # self.mysql.init_app(app)
        # self.sqlite.init_app(app)


database = Database()


login_manager = LoginManager()
login_manager.session_protection = "strong"


class Application(Flask):
    def __init__(self, environment):
        # TODO LOG,db,
        super(Application, self).__init__(__name__, static_folder=static_path, template_folder=templates_path)
        self.config.from_object(config[environment])
        # self.db = Database(self.config)

        #: celery
        init_celery(self, celery)

        #: mail
        init_mail(self)

    def _init_blueprint(self, *blueprints):
        """
        注册蓝图
        :param blueprints(list): 蓝图 
        """
        for blueprint in blueprints:
            self.register_blueprint(blueprint)

    def register_processors(self, *context_processors):
        """
        注册jinja上下文,在模板渲染之前运行
        :param context_processors(list): 上下文函数 
        """
        for context_processor in context_processors:
            self.context_processor(context_processor)

    def before_request_hook(self, *funcs):
        """
        请求钩子
        :param funcs(list): 请求之前注册函数 
        """
        for f in funcs:
            self.before_request(f)

    def after_request_hook(self, *funcs):
        """
        响应钩子
        :param funcs:响应之后 
        """
        for f in funcs:
            self.after_request(f)


def create_app(environment):
    app = Application(environment)
    if environment == "dev":
        app.debug = True

    #: 数据库
    database.init_app(app)

    #: 注册蓝图
    from app.apis.api import api_bp
    from app.views.homepage import homepage_bp
    from app.views.error import error_bp
    from app.views.auth import auth_bp
    blueprints = [homepage_bp, api_bp, error_bp, auth_bp]
    app._init_blueprint(*blueprints)

    #: 注册jinja上下文
    from .ctx import author_context_processor
    context_processors = [author_context_processor]
    app.register_processors(*context_processors)

    return app
