#!/usr/bin/python3

#Advanced binary search- Interviewbit
#Question: Search index of a number in a rotated sorted array. Eg- [4,6,7,1,2,3]


def search(A, B):
    start = 0
    end = len(A)-1
    while(start<=end):
        mid = int((start+end)/2)
        l,m,r = A[start], A[mid], A[end]
        if (m == B):
            return mid
        elif (l<=B<m) or (l>m and not(m<B<=r)):
            end = mid-1
        else:
            start = mid+1
    return -1


#If elements aren't distinct, linear search might be better

if __name__ == '__main__':
    arr = [int(x) for x in input('Enter integer array in single line(space separated): ').split()]
    num = int(input('Element to be found: '))
    print(search(arr, num))
