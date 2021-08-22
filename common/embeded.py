# 由于部署只有一台机器，直接用内存伪造 Redis。做成适配器模式
import os

class BaseCache(object):

    def get(self, key):
        pass

    def set(self, key, value):
        pass

class EmbededRedis(BaseCache):
    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache.get(key, None)

    def set(self, key, value):
        self.cache[key] = value


embeded_redis = EmbededRedis()
PF_SIGN_CACHE_CONFIG = 'PF_SIGN_CACHE_CONFIG'
MEMORY = "MEMORY"

class CacheFactory(object):

    @classmethod
    def get_cache(cls):
        cahce_config = os.environ.get(PF_SIGN_CACHE_CONFIG, MEMORY)
        if cahce_config == MEMORY:
            return embeded_redis
        return embeded_redis