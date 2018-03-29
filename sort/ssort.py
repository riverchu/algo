#! /usr/bin/env python
__author__ = 'indigo'

import numpy as np

class SelectSort(object):
    def __init__(self,n):
        self.L = np.random.randint(0,99,n)

    def ssort(self):
        L = self.L
        for i in range(0,len(L)):
            min_ = i
            for j in range(i+1, len(L)):
                if L[j] < L[min_]:
                    min_ = j
            if min_ != i:
                L[min_],L[i]=L[i],L[min_]

    def show(self):
        print self.L

if __name__ == "__main__":
    t = SelectSort(10)
    t.show()
    t.ssort()
    t.show()
