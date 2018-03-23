#! /usr/bin/env python

import numpy as np

def ssort(L):
    for i in range(0,len(L)):
        min_ = i
        for j in range(i+1, len(L)):
            if L[j] < L[min_]:
                min_ = j
        if min_ != i:
            L[min_],L[i]=L[i],L[min_]

if __name__ == "__main__":
    print "[+]start..."
    L = np.random.randint(0,99,10)
    print L
    ssort(L)
    print L
