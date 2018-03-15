#!/usr/bin/python3

#InterviewBit - Binary search
#Question - Find x^n%d in O(logb) time

#Binary modular exponentiation

def pow(x, n, d):
    if (x == 0):
        return 0
    sol = 1
    x = x%d
    while(n>0):
        if ((n&1) == 1):
            sol = (sol*x) % d
        n = n>>1
        x = (x*x) % d
    return sol

if __name__ == '__main__':
    x = int(input('Enter base: '))
    n = int(input('Enter exponent: '))
    d = int(input('Enter modulo: '))
    print(pow(x,n,d))

