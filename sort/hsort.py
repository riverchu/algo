#!/usr/bin/env python
__author__ = 'indigo'

import numpy as np

class HeapSort(object):
    def __init__(self,n):
        self.L = np.random.randint(0,99,n)

    def swap(self,L,m,n):
        L[m]^=L[n]
        L[n]^=L[m]
        L[m]^=L[n]

    def adjust(self,L,length,index):
        left = 2*index+1
        right = 2*index+2
        maxIdx = index

        if left<length and L[left]>L[maxIdx]:
            maxIdx = left
        if right<length and L[right]>L[maxIdx]:
            maxIdx = right

        if maxIdx != index:
            self.swap(L,index,maxIdx)
            self.adjust(L,length,maxIdx)

    def heapsort(self):
        L = self.L
        length = len(L)
        for i in range(length/2-1,-1,-1):
            self.adjust(L,length,i)

        for i in range(length-1,0,-1):
            self.swap(L,i,0)
            self.adjust(L,i,0)

    def show(self):
        print self.L

if __name__ == "__main__":
    t = HeapSort(10)
    t.show()
    t.heapsort()
    t.show()
