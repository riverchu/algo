#!/usr/bin/env python
__author__ = 'indigo'

import numpy as np

class QuickSort(object):
    def __init__(self,n):
        self.L = np.random.randint(0,99,n)

    def qsort(self,left,right):
        L = self.L
        if(left >= right):
            return L

        l = left
        r = right
        key = L[l]

        while l<r:
            while l<r and key<=L[r]:r-=1
            L[l] = L[r]
            while l<r and L[l]<=key:l+=1
            L[r] = L[l]

        L[l] = key
        self.qsort(left,l-1)
        self.qsort(l+1,right)
        return L

    def show(self):
        print self.L

if __name__ == "__main__":
    t = QuickSort(10)
    t.show()
    t.qsort(0,len(t.L)-1)
    t.show()
