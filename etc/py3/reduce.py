#!/bin/usr/env python3
from functools import reduce

DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str2float(s):
    def char2num(c):
        return DIGITS[c]

    n=s.find('.')
    return reduce(lambda x,y:x*10+y,map(char2num,s[:n])) + 0.1*reduce(lambda x,y:x*0.1+y,list(map(char2num,s[n+1:]))[::-1])

print(str2float('123.456'))
