#!/usr/bin/env python
# coding:utf-8

def A(n):
    return n*A(n-1) if n>0 else 1

def C(n,m):
    return A(n)/(A(n-m)*A(m)) if m>0 else 1

def mod(n):
    return n%1000000007

#3
def calc(i,n,s):
    if i==0:
        return A(n)*C(n,0)

    sum = A(n+i)*C(n,i)
    for j in range(i):
        sum -= s[j]*C(n-j,i-j)*pow(2,i-j)

    return sum

def queue(n):
    #3
    s = [0]*int(1e5)
    sum=0
    for i in range(n+1):
        #1
        sum = C(n,i)*A(n+i) - sum

        #2
        #if i%2==1:
        #    sum -= A(2*n-i)*C(n,n-i)
        #else:
        #    sum += A(2*n-i)*C(n,n-i)

        #3
        #s[i] = calc(i,n,s)
        #sum += s[i]

    k=1
    for i in range(n):
        k = mod(k*120)

    return mod(mod(k)*mod(sum))

if __name__ == "__main__":
    n = raw_input('input n:')
    print queue(int(n))
