#!/usr/bin/env python3
# coding=utf-8

from enum import Enum,unique

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

for name,member in Month.__members__.items():
    print (name,'=>',member,',',member.value)

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

bart = Student('Bart',Gender.Male)
if bart.gender == Gender.Male:
    print("测试成功")
else:
    print("测试失败")
