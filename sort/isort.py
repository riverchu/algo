#! /usr/bin/env python
__author__ = 'indigo'

import numpy as np

class InsertSort(object):
    def __init__(self,n):
        self.L = np.random.randint(0,99,n)

    def isort(self):
        L = self.L
        for i in range(1,len(L)):
            j = i
            k = L[i]
            while j>0 and L[j-1]>k:
                L[j] = L[j-1]
                j-=1
                L[j] = k

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
        print list(self.L)

if __name__ == "__main__":
    t = InsertSort(10)
    t.show()
    #t.isort()
    #t.show()
    print t.rec_isort(list(t.L))
