#!/usr/bin/env python3

from numpy import *

n=4
c=8
w=[0,2,3,4,5]
v=[0,3,4,5,6]
V=zeros([5,9],int8)

def findMax():
    for i in range(1,n+1):
        for j in range(1,c+1):
            if j<w[i]:
                V[i][j] = V[i-1][j]
            else:
                V[i][j] = max(V[i-1][j],V[i-1][j-w[i]]+v[i])

findMax()
print(V)
