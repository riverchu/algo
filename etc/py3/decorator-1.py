#!/usr/bin/env python3
# coding=utf-8

import functools
import types

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            if type(text)==str:
                print(text)
            print('[+]begin call %s' % func.__name__)
            func(*args,**kw)
            print('[+]end call %s' % func.__name__)
            return
        return wrapper

    #isinstance(text, types.FunctionType):
    return decorator if type(text)==str else decorator(text)

@log('execute')
def f():
    pass

@log
def g():
    pass

f()

g()
