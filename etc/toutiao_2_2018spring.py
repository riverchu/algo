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

'''
初始定义s=1, m=1
定义两个操作A和B：
A. m = s, s = s + s
B. s = s + m
输入 n, 输出所需要的最小的操作次数，使得 s = n.

解法：分解质因数
'''
