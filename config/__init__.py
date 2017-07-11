class Config(object):
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379',
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    DEBUG = False
    MYSQL_CONFIG = ""
    SQLALCHEMY = ""
    REDIS = ""
    SQLITE = ""


class DevelopmentConfig(Config):
    DATABASE_URI = ''
    DEBUG = True
    MYSQL_CONFIG = ""
    SQLALCHEMY = ""
    REDIS = ""
    SQLITE = ""


class TestingConfig(Config):
    DATABASE_URI = ''
    TESTING = True
    MYSQL_CONFIG = ""
    SQLALCHEMY = ""
    REDIS = ""
    SQLITE = ""


config = {
    "default": DevelopmentConfig,
    "product": ProductionConfig,
    "test": TestingConfig,
    "dev": ProductionConfig,
}
