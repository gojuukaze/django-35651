import re
from django.core.cache.backends.redis import RedisCache, RedisCacheClient


class DebugRedisCacheClient(RedisCacheClient):
    def _get_connection_pool(self, write):
        print(f'len(pools)={len(self._pools)}')

        index = self._get_connection_pool_index(write)
        if index not in self._pools:
            self._pools[index] = self._pool_class.from_url(
                self._servers[index],
                **self._pool_options,
            )
        return self._pools[index]


class DebugRedisCache(RedisCache):
    def __init__(self, server, params):
        super(RedisCache, self).__init__(params)
        if isinstance(server, str):
            self._servers = re.split("[;,]", server)
        else:
            self._servers = server

        self._class = DebugRedisCacheClient
        self._options = params.get("OPTIONS", {})
