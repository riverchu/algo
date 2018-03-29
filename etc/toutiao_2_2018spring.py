#!/usr/bin/env python

class CalcStep(object):
    def __init__(self):
        pass

    def min_operates(self,n):
        operate = 0
        for i in xrange(int(n**0.5),1,-1):
            if i>n:continue
            if not self.is_prime(i):continue
            while n%i == 0:
                n /= i
                operate += i-1
        return operate + n - 1

    def is_prime(self,n):
        for i in xrange(2,int(n**0.5)+1):
            if n%i == 0 :return False
        return True

if __name__ == "__main__":
    i = CalcStep()
    print i.min_operates(12)
