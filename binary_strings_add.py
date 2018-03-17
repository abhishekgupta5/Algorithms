#!/usr/bin/python3
from collections import deque

def add_strings(A,B):
    len_A = len(A)-1
    len_B = len(B)-1
    carry = 0
    d = deque()
    while(len_A>=0 and len_B>=0):
        comp = int(A[len_A]) + int(B[len_B]) + carry
        if (comp > 1):
            if (comp == 2):
                d.appendleft('0')
            else:
                d.appendleft('1')
            carry = 1
        else:
            d.appendleft(str(comp))
            carry = 0
        len_A -= 1
        len_B -= 1

    while(len_A>=0):
        comp = int(A[len_A]) + carry
        if (comp > 1):
            if (comp == 2):
                d.appendleft('0')
            else:
                d.appendleft('1')
            carry = 1
        else:
            d.appendleft(str(comp))
            carry = 0
        len_A -= 1

    while(len_B>=0):
        comp = int(B[len_B]) + carry
        if (comp > 1):
            if (comp == 2):
                d.appendleft('0')
            else:
                d.appendleft('1')
            carry = 1
        else:
            d.appendleft(str(comp))
            carry = 0
        len_B -= 1
    if carry == 1:
        d.appendleft('1')

    return ''.join(list(d))

if __name__ == '__main__':
    a = input('Enter first string: ')
    b = input('Enter second string: ')
    print(add_strings(a,b))
