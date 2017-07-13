import redis
import json


class RedisDatabase():
    def __init__(self, app=None):
        self._redis_client = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        redis_url = app.config.get(
            "REDIS_URL", 'redis://localhost:6379/0'
        )
        self._redis_client = self.create_conn(redis_url)

    def create_conn(self, redis_url, **kwargs):
        conn = redis.StrictRedis.from_url(redis_url)
        return conn

    def dump(self, key, data):
        s = json.dumps(data)
        self._redis_client.set(key, s)

    def load(self, key):
        s = self._redis_client.get(key)
        if s:
            return json.loads(s)

    def __getattr__(self, name):
        return getattr(self._redis_client, name)

    def __getitem__(self, name):
        return self._redis_client[name]

    def __setitem__(self, name, value):
        self._redis_client[name] = value

    def __delitem__(self, name):
        del self._redis_client[name]
