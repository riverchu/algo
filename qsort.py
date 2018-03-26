#!/usr/bin/env python
import numpy as np

def qsort(L,left,right):
    if(left >= right):
        return L

    i = left
    j = right
    key = L[i]

    while i<j:
        while i<j and key<=L[j]:
            j-=1
        L[i] = L[j]
        while i<j and L[i]<=key:
            i+=1
        L[j] = L[i]
    L[i] = key
    qsort(L,left,i-1)
    qsort(L,i+1,right)
    return L

if __name__ == "__main__":
    L = np.random.randint(0,99,10)
    print L
    qsort(L,0,9)
    print L
