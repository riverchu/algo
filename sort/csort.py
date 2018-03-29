#!/usr/bin/env python
__author__ = 'indigo'

import numpy as np

class CountSort(object):
    MAX = 100

    def __init__(self,n):
        self.L = np.random.randint(0,99,n)

    def csort(self):
        L = self.L
        T = np.zeros(CountSort.MAX,int)

        for i in range(0,len(L)):
            T[L[i]]+=1

        j=0
        for i in range(0,CountSort.MAX):
            while T[i]>0:
                L[j] = i
                j+=1
                T[i]-=1

    def show(self):
        print self.L

if __name__ == "__main__":
    t = CountSort(10)
    t.show()
    t.csort()
    t.show()
