#!/usr/bin/python3

def diffk(A, k):
    if (k == 0):
        if len(set(A)) != len(A):
            return 1
        else:
            return 0
    A = list(set(A))
    A.sort()
    count = 0
    for i in range(len(A)):
        start = 1
        end = len(A)-1
        while(start<=end):
            mid = (start+end) // 2
            if (A[i] + k == A[mid]):
                count += 1
            if (A[i]+k > A[mid]):
                start = mid+1
            else:
                end = mid-1
    return count

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8]
    k = 3
    print(diffk(l,k))
