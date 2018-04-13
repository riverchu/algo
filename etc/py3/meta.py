#!/usr/bin/env python3
# coding=utf-8

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        print('cls',cls)
        print('name',name)
        print('base',bases)
        print('attrs',attrs)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L=MyList()
