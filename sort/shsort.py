#!/usr/bin/env python
__author__ = 'indigo'

import numpy as np

class ShellSort(object):
    def __init__(self,n):
        self.L = np.random.randint(0,99,n)

    def shsort(self):
        L = self.L
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

    def show(self):
        print self.L

if __name__ == "__main__":
    t = ShellSort(10)
    t.show()
    t.shsort()
    t.show()
