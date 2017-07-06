from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

class SqlalchemyDatabase():
    """sqlalchemy"""

    def __init__(self, url):
        """
        :param url:  "mysql+pymysql://chenzikun:ppwchenzikun@192.168.1.253:20002/xw?charset=utf8"
        """
        self.engine = create_engine(url)
        self.meta = self.create_session()
        self.session = self.create_meta()

    def create_meta(self):
        """
        创建meta
        :return: meta
        """
        metadata = MetaData(bind=self.engine)
        metadata.reflect()
        return metadata

    def create_session(self):
        """
        创建会话
        :return: 会话
        """
        Session = sessionmaker(bind=self.engine)
        return Session()

    def query(self, table_name):
        """
        获取数据
        :param table_name: 表名
        :return: [{},{}]columns的字典列表
        """
        table = self.meta.tables[table_name]
        result = self.session.query(table).all()
        return [{key: value for key, value in zip(table.c.keys(), values)} for values in result]

    def add(self, table_name, value):
        """
        数据同步
        :param table_name 表名
        :param value [{}] or {} value类型：字典或者包含字典的列表
        """
        table = self.meta.tables[table_name]
        self.session.execute(table.insert(), value)
        self.session.commit()

    def insert(self, table_name, value):
        """
        :param table_name:
        :param value: [{}, {}],对象字典、
        :return:  插入数据的id
        """
        table = self.meta.tables[table_name]
        cur = self.session.execute(table.insert(), value)
        self.session.commit()
        return cur.lastrowid