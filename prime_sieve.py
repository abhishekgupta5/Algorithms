#!/usr/bin/python3
from math import ceil, sqrt

def sieve(n):

    lis = [True for i in range(n+1)]

    max_num = ceil(sqrt(n))
    j = 2
    for i in range(2,max_num):
        if (lis[i] == 1):
            while(i*j<=n):
                lis[i*j] = 0
                j += 1

    for i in range(2,n+1):
        if lis[i]:
            print(i, end=' ')
    print("\n")

if __name__ == '__main__':
    n = int(input("Enter number: "))
    sieve(n)

