#! /usr/bin/env python

import numpy as np

def isort(L):
    for i in range(1,len(L)):
        for j in range(i,0,-1):
            k = j-1
            if L[k]>L[j]:
                L[k],L[j]=L[j],L[k]

if __name__ == "__main__":
    L = np.random.randint(0,99,10)
    print L
    isort(L)
    print L
