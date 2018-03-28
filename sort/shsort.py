#!/usr/bin/env python

import numpy as np

def shsort(L):
    if len(L)<=1:
        return

    div = len(L)/2
    while div>0:
        for i in range(0,div):
            for j in range(i+div,len(L),div):
                m = L[j]
                while j>=div and L[j-div]>m:
                    L[j] = L[j-div]
                    j-=div
                L[j] = m
        div/=2

if __name__ == "__main__":
    L = np.random.randint(0,99,10)
    print L
    shsort(L)
    print L
