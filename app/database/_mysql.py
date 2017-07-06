import pymysql


class MysqlDatabase(object):
    def __init__(self):
        pass

    @staticmethod
    def mysql_conn():
        return pymysql.connect()

    def add(self, sql, value):
        conn = self.mysql_conn()
        with conn.cursor() as cursor:
            if isinstance(value, tuple):
                cursor.execute(sql, value)
            elif isinstance(value, list):
                cursor.executemany(sql, value)
            else:
                raise ValueError
            conn.commit()

    def insert(self, sql, value):
        conn = self.mysql_conn()
        with conn.cursor() as cursor:
            if isinstance(value, tuple):
                cursor.execute(sql, value)
            else:
                raise ValueError
            conn.commit()
            return cursor.lastrowid

    def query(self, sql):
        with self.mysql_conn().cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
