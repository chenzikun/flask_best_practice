import os

app_dir = os.path.join(
    os.path.dirname(__file__), ".."
)

data_dir = os.path.abspath(
    os.path.join(
        app_dir, "scheme"
    )
)


class Config(object):
    #: celery配置
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379',
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'


class DevelopmentConfig(Config):
    DATABASE_URI = ''
    DEBUG = True
    MYSQL_CONFIG = {
        ""
    }
    REDIS_url = ""
    SQLITE_DATABASE = ""
    SQLALCHEMY_DATABASE_URL = "sqlite:///" + os.path.join(data_dir, "data.sqlite")


class TestingConfig(Config):
    DATABASE_URI = ''
    TESTING = True
    MYSQL_CONFIG = ""
    SQLALCHEMY = ""
    REDIS = ""
    SQLITE = ""


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    DEBUG = False
    MYSQL_CONFIG = ""

    REDIS = ""
    SQLITE = ""


config = {
    "default": DevelopmentConfig,
    "product": ProductionConfig,
    "test": TestingConfig,
    "dev": ProductionConfig,
}
