import pymysql


class MysqlDatabase(object):
    def __init__(self, setting):
        self.setting = setting

    def create_conn(self):
        return pymysql.connect(self.setting)

    def add(self, sql, value):
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
