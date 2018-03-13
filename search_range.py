#!/usr/bin/python3
from bisect import bisect_left, bisect_right
#Question(interviewbit-search): Search for a range of a given number in a list. Return Start and End index. O(logn)

def search_range(A, B):
    start = end = -1
    l = 0
    r = len(A) - 1
    while(l<=r):
        mid = int((l+r)/2)
       # print('mid=', mid)
        if (A[mid] == B and (A[mid-1] != B or mid == 0)):
            start = mid
            break
        if A[mid]<B:
            l = mid+1
        else:
            r = mid-1
    l = 0
    r = len(A) - 1
    while(l<=r):
        mid = int((l+r)/2)
        if (A[mid] == B and (mid == len(A)-1 or A[mid+1] != B)):
            end = mid
            break
        if A[mid]<=B:
            l = mid+1
        else:
            r = mid-1
    return [start,end]

#Using bisect function
def search_range_bisect(A,B):
    l, r = bisect_left(A,B), bisect_right(A,B)
    if l == r:
        return [-1,-1]
    else:
        return [l, r-1]

if __name__ == '__main__':
    l = [int(x) for x in input().split()]
    n = int(input('Enter number to get range: '))
    print(search_range(l, n))
