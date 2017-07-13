# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy


class SqlalchemyDatabase(SQLAlchemy):
    """sqlalchemy"""

    def query(self, table_name):
        """
        获取数据
        :param table_name: 表名
        :return: [{},{}]columns的字典列表
        """
        table = self.metadata.tables[table_name]
        result = self.session.query(table).all()
        return [{key: value for key, value in zip(table.c.keys(), values)} for values in result]

    def add(self, table_name, value):
        """
        数据同步
        :param table_name 表名
        :param value [{}] or {} value类型：字典或者包含字典的列表
        """
        table = self.metadata.tables[table_name]
        self.session.execute(table.insert(), value)
        self.session.commit()

    def insert(self, table_name, value):
        """
        :param table_name:
        :param value: [{}, {}],对象字典、
        :return:  插入数据的id
        """
        table = self.metadata.tables[table_name]
        cur = self.session.execute(table.insert(), value)
        self.session.commit()
        return cur.lastrowid