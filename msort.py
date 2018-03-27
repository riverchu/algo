#!/bin/usr/env python

import numpy as np

def msort(L):
    if len(L) <= 1:
        return L
    n = int(len(L)/2)
    left = msort(L[:n])
    right = msort(L[n:])
    return Merge(left, right)

def Merge(left,right):
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

if __name__ == "__main__":
    L = np.random.randint(0,99,10).tolist()
    print(L)
    L = msort(L)
    print(L)

