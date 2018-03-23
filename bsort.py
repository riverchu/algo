#! /usr/bin/env python

import numpy as np

def bsort(L):
    for i in range(0,len(L)):
        for j in range(0,len(L)-i-1):
            k = j+1
            if L[j]>L[k]:
                L[j],L[k]=L[k],L[j]

if __name__ == "__main__":
    L = np.random.randint(0,99,10)
    print L
    bsort(L)
    print L
