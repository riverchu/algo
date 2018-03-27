#!/usr/bin/env python

import numpy as np

MAX = 100

def countsort(L):
    T = np.zeros(MAX,int)

    for i in range(0,len(L)):
        T[L[i]]+=1

    j=0
    for i in range(0,MAX):
        while T[i]>0:
            L[j] = i
            j+=1
            T[i]-=1

if __name__ == "__main__":
    L = np.random.randint(0,99,10)
    print L
    countsort(L)
    print L
