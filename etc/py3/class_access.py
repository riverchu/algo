#!/usr/bin/env python3
# coding=utf-8

class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self._test = 'test'#可以但不建议直接被外部引用
        self.__gender = '' #不可以直接引用，但有的编译器可以通过_Student__genger方式引用
        self.set_gender(gender)

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if gender!='male' and gender!='female':
            print('bad gender')
        else:
            self.__gender=gender

# 测试:
bart = Student('Bart', 'male')
print(bart._test)
