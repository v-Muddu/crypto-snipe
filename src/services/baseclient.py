import ratelimiter
import requests

class BaseClient: 
    def __init__(self):
        self._limiter = ratelimiter(300, 60)

    def get(self, url, **kwargs):
        with self._limiter:
            r = requests.get(url, kwargs)

        return r.json()
