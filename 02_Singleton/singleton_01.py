# /usr/bin/env python3
# -*- coding: utf-8 -*-


class singleton(object):

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            org = super(singleton, cls)
            cls._instance = org.__new__(cls, *args, **kw)
        return cls._instance


# test code
if __name__ == '__main__':
    class MyClass(singleton):
        def __init__(self, name):
            self.name = name

    a = MyClass('a')
    b = MyClass('b')
    print(a.name)
    print(b.name)
