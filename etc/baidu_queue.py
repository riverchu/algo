#!/usr/bin/env python
# coding:utf-8

def A(n):
    return n*A(n-1) if n>0 else 1

def C(n,m):
    return A(n)/(A(n-m)*A(m)) if m>0 else 1

def mod(n):
    return n%1000000007

def calc(i,n,s):
    if i==0:
        return A(n)*C(n,0)

    sum = A(n+i)*C(n,i)
    for j in range(i):
        sum -= s[j]*C(n-j,i-j)*pow(2,i-j)

    return sum

def queue(n):
    s = [0]*int(1e5)
    sum = 0
    for i in range(n+1):
        sum = C(n,i)*A(n+i) - sum
        #s[i] = calc(i,n,s)
        #sum += s[i]
    k=1
    for i in range(n):
        k = mod(k*120)
    #print s[:n+10]

    return mod(mod(k)*mod(sum))

n = raw_input('input n:')
print queue(int(n))
