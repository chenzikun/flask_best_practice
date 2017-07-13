import pymysql
from app.exceptions import ConfigError

from flask import _app_ctx_stack as _ctx_stack


class MysqlDatabase(object):
    """原生MySQL"""
    def __init__(self,  app=None):
        self.setting = None
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        mysql_config = app.config.get("MYSQL_CONFIG")
        if not mysql_config:
            raise  ConfigError("未找到MYSQL_CONFIG")
        self.setting = mysql_config

        if hasattr(app, 'teardown_appcontext'):
            self.app.teardown_request(self.teardown_request)

    def create_conn(self):
        return pymysql.connect(self.setting)

    def add(self, sql, value):
        """
        单个写入或一次写入多个数据
        :param sql: int, 原生sql语句
        :param value: tuple or list 
        :return: 
        """
        conn = self.create_conn()
        with conn.cursor() as cursor:
            if isinstance(value, tuple):
                cursor.execute(sql, value)
            elif isinstance(value, list):
                cursor.executemany(sql, value)
            else:
                raise ValueError
            conn.commit()

    def insert(self, sql, value):
        """单个写入数据，返回写入数据的id"""
        conn = self.create_conn()
        with conn.cursor() as cursor:
            if isinstance(value, tuple):
                cursor.execute(sql, value)
            else:
                raise ValueError
            conn.commit()
            return cursor.lastrowid

    def query(self, sql):
        with self.create_conn().cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def teardown_request(self, exception):
        ctx = _ctx_stack.top
        if hasattr(ctx, "mysql_db"):
            ctx.mysql_db.close()

    def get_db(self):
        ctx = _ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, "mysql_db"):
                ctx.mysql_db = self.create_conn()
            return ctx.mysql_db

