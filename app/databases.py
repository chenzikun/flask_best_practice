from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import pymysql


class SQLAlchemyDatabase(object):
    """sqlalchemy"""

    def __init__(self, url):
        self.meta, self.session = self.create_session(url)

    def create_session(self, url):
        """
        创建meta及会话
        :param url:
        :return: meta对象和会话
        """
        engine = create_engine(url)
        metadata = MetaData(bind=engine)
        metadata.reflect()
        Session = sessionmaker(bind=engine)
        return metadata, Session()

    def query(self, table_name):
        """
        获取数据
        :param table_name: 表名
        :return: [{},{}]columns的字典列表
        """
        table = self.meta.tables[table_name]
        result = self.session.query(table).all()
        return result

    def query_dict(self, table_name):
        """
        获取数据
        :param table_name: 表名
        :return: [{},{}]columns的字典列表
        """
        table = self.meta.tables[table_name]
        result = self.session.query(table).all()
        return [row._asdict() for row in result]

    def add(self, table_name, value):
        """
        数据同步
        :param table_name 表名
        :param value [{}] or {} value类型：字典或者包含字典的列表
        """
        try:
            table = self.meta.tables[table_name]
            self.session.execute(table.insert(), value)
            self.session.commit()
        except:
            self.session.rollback()

    def insert(self, table_name, value):
        """
        :param table_name:
        :param value: [{}, {}],对象字典、
        :return:  插入数据的id
        """
        try:
            table = self.meta.tables[table_name]
            cur = self.session.execute(table.insert(), value)
            self.session.commit()
            return cur.lastrowid
        except:
            self.session.rollback()


class MysqlDatabase(object):
    def __init__(self, config):
        self.config = config

    def mysql_conn(self):
        return pymysql.connect(self.config)

    def insert(self, sql, value):
        conn = self.mysql_conn()
        with conn.cursor() as cursor:
            cursor.execute(sql, value)
        conn.commit()

    def query(self, sql):
        with self.mysql_conn().cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

