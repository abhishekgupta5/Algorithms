#!/usr/bin/python3
from math import sqrt, ceil

def factors(n):
    root = ceil(sqrt(n))
    lis=[]
    for i in range(1,root):
        if (n%i == 0):
            lis.append(int(i))
            if (i != root):
                lis.append(int(n/i))
    lis.sort()
    print(lis)

n = int(input('Enter number: '))
factors(n)
