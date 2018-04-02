#! /usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'indigo'

import numpy as np

class InsertSort(object):
    def __init__(self,n):
        self.L = list(np.random.randint(0,99,n))

    def isort(self):
        L = self.L
        for i in range(1,len(L)):
            for j in range(i,0,-1):
                if L[j-1]<=L[i]:
                    L.insert(j,L[i])
                    break
                elif j==1:
                    L.insert(j-1,L[i])
            L.pop(i+1)

    #递归式写法
    def rec_isort(self,L):
        if len(L)<=1:
            return L
        T = self.rec_isort(L[1:])
        for i in xrange(len(T)):
            if L[0] <= T[i]:
                return T[:i]+[L[0]]+T[i:]
        return T+[L[0]]

    def show(self):
        print self.L

if __name__ == "__main__":
    t = InsertSort(10)
    t.show()
    t.isort()
    t.show()
    #print t.rec_isort(t.L)
