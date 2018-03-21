#!/usr/bin/python3

#Interviewbit-Array, binary search
#Question link : https://www.interviewbit.com/problems/kth-smallest-element-in-the-array/

def smallest(A, k):
    start = min(A)
    end = max(A)
    while (start<=end):
        mid = start + (end-start) // 2
        cntl = cnteq = 0
        for i in range(len(A)):
            if (A[i]<mid):
                cntl += 1
            elif (A[i]==mid):
                cnteq += 1
            if (cntl>=k):
                break
        print('mid=', mid)
        print('countless=',cntl)
        print('counteq=',cnteq)
        if cntl<k and (cntl+cnteq)>=k:
            return mid
        elif cntl>=k:
            end = mid-1
        else:
            start = mid+1
    return -1
        #cntl = sum(j<k for j in A)
        #cnteq = sum(j==k for j in A)


if __name__ == '__main__':
    arr = (8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92)
    #arr = (10,7,12,90,1,4,0,24)
    k = 9
    print(smallest(arr, k))
