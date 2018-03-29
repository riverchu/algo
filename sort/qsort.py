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

        i = left
        j = right
        key = L[i]

        while i<j:
            while i<j and key<=L[j]:j-=1
            L[i] = L[j]
            while i<j and L[i]<=key:i+=1
            L[j] = L[i]

        L[i] = key
        self.qsort(left,i-1)
        self.qsort(i+1,right)
        return L

    def show(self):
        print self.L

if __name__ == "__main__":
    t = QuickSort(10)
    t.show()
    t.qsort(0,len(t.L)-1)
    t.show()
