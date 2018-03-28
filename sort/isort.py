#! /usr/bin/env python

import numpy as np

def isort(L):
    for i in range(1,len(L)):
        j = i
        k = L[i]
        while j>0 and L[j-1]>k:
            L[j] = L[j-1]
            j-=1
        L[j] = k

if __name__ == "__main__":
    L = np.random.randint(0,99,10)
    print L
    isort(L)
    print L
