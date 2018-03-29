#! /usr/bin/env python
__author__ = 'indigo'

import numpy as np

class BubbleSort(object):
    def __init__(self,n):
        self.L = np.random.randint(0,99,n)

    def bsort(self):
        L = self.L
        for i in range(0,len(L)):
            for j in range(0,len(L)-i-1):
                k = j+1
                if L[j]>L[k]:
                    L[j],L[k]=L[k],L[j]

    def show(self):
        print self.L

if __name__ == "__main__":
    t = BubbleSort(10)
    t.show()
    t.bsort()
    t.show()
