#!/usr/bin/python3

#Interviewbit-Binary search
#Question: Find square root of a number in O(logn) time without using sqrt() from math

def sqrt(A):
    if (A is 0 or A is 1):
        return A
    start = 1
    end = A
    while(start<=end):
        mid = (start+end) // 2
        if ((mid*mid) == A):
            return mid
        if (mid*mid<A):
            start = mid+1
            sol = mid
        else:
            end = mid-1
    return sol

if __name__ == '__main__':
    num = int(input("Enter number: "))
    print(sqrt(num))


