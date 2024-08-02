# Reproduce [#35651](https://code.djangoproject.com/ticket/35651)

## Steps to Reproduction

```shell
pip install -r requirements.txt

docker run --name redis -d -p 6379:6379 redis

daphne djangoProject.asgi:application
```

After running the service you can reproduce the problem by requesting the test page (http://127.0.0.1:8000/test).

To get the number of redis connections you can enter the redis container and use `CLIENT list` command. You can observe that a new connection is created every time the test page is requested.
```shell
docker exec -it redis redis-cli

# in docker container
# 127.0.0.1:6379> CLIENT list
```

You can also use `async_request.py` to batch request the test page.
```shell
python async_request.py
```

## debug_cache

I wrote a debug cache for watching the connection pool, which you can use via settings2.

```shell
DJANGO_SETTINGS_MODULE=djangoProject.settings2 daphne djangoProject.asgi:application
```

Requesting the test page again, you can see that `len(pool)` is always empty

