# /usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import wraps


def singleton(cls):
    _instance = {}

    @wraps(cls)
    def get_instance(*args, **kw):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kw)
        return _instance[cls]
    return get_instance


# test
if __name__ == '__main__':
    @singleton
    class MyClass(object):
        def __init__(self, name):
            self.name = name

    a = MyClass('a')
    b = MyClass('b')
    print(a.name)
    print(b.name)
