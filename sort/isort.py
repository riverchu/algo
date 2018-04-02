#! /usr/bin/env python
__author__ = 'indigo'

import numpy as np

class InsertSort(object):
    def __init__(self,n):
        self.L = np.random.randint(0,99,n)

    def isort(self):
        L = self.L
        for i in range(1,len(L)):
            key = L[i]
            for j in range(i,0,-1):
                if L[j-1]>key:
                    L[j] = L[j-1]
                else:
                    break
            if L[j-1]>key:L[j-1] = key
            print key,j-1
            print L
            '''
            j = i
            k = L[i]
            while j>0 and L[j-1]>k:
                L[j] = L[j-1]
                j-=1
                L[j] = k
                '''

    def show(self):
        print self.L

if __name__ == "__main__":
    t = InsertSort(10)
    t.show()
    t.isort()
    t.show()
