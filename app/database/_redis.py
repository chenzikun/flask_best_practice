import redis
import json

class RedisDatabase(object):
    def __init__(self, setting):
        """
        :param setting:  'redis://192.168.1.25:6379'
        """
        self.setting = setting

    def create_conn(self):
        conn = redis.StrictRedis.from_url(self.setting)
        return conn

    def dump(self, key, data):
        conn = self.create_conn()
        s = json.dumps(data)
        conn.set(key, s)

    def load(self, key):
        conn = self.create_conn()
        s = conn.get(key)
        if s:
            return json.loads(s)
