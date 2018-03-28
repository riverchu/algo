#!/usr/bin/env python

import numpy as np

def swap(L,m,n):
    L[m]^=L[n]
    L[n]^=L[m]
    L[m]^=L[n]

def adjust(L,length,index):
    left = 2*index+1
    right = 2*index+2
    maxIdx = index

    if left<length and L[left]>L[maxIdx]:
        maxIdx = left
    if right<length and L[right]>L[maxIdx]:
        maxIdx = right

    if maxIdx != index:
        swap(L,index,maxIdx)
        adjust(L,length,maxIdx)

def heapsort(L):
    length = len(L)
    for i in range(length/2-1,-1,-1):
        adjust(L,length,i)

    for i in range(length-1,0,-1):
        swap(L,i,0)
        adjust(L,i,0)

if __name__ == "__main__":
    L = np.random.randint(0,99,10)
    print L
    heapsort(L)
    print L
