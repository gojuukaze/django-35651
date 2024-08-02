from djangoProject.settings import *

CACHES = {
    "default": {
        "BACKEND": "debug_cache.debug.DebugRedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}