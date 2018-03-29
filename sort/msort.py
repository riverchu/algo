#!/usr/bin/env python
__author__ = 'indigo'

import numpy as np

class MergeSort(object):
    def __init__(self,n):
        self.L = np.random.randint(0,99,n).tolist()

    def msort(self,L):
        if len(L) <= 1:
            return L
        n = int(len(L)/2)
        left = self.msort(L[:n])
        right = self.msort(L[n:])
        return self.Merge(left, right)

    def Merge(self,left,right):
        r, l=0, 0
        result=[]
        while l<len(left) and r<len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        result += left[l:]
        result += right[r:]
        return result

    def setL(self,L):
        self.L = L

    def show(self):
         print self.L

if __name__ == "__main__":
    t = MergeSort(10)
    t.show()
    t.setL(t.msort(t.L))
    t.show()
