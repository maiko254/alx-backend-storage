#!/usr/bin/env python3
"""Module implementing a redis cache"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """Cache class for storing data in redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Type-annotated function storing data in redis and returning a key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """Get data from Redis and apply an optional function."""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Returns string data from redis"""
        return self._redis.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: int) -> int:
        """Returns integer data from redis"""
        return self._redis.get(key, fn=int)
