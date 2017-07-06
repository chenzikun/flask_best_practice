import redis
import json

class RedisDatabase(object):
    def __init__(self, setting):
        """
        :param setting:  'redis://192.168.1.25:6379'
        """
        self.conn = self._redis_conn(setting)

    def _redis_conn(self, setting):
        conn = redis.StrictRedis.from_url(setting)
        return conn

    def dump(self, key, data):
        s = json.dumps(data)
        self.conn.set(key, s)

    def load(self, key):
        s = self.conn.get(key)
        if s:
            return json.loads(s)