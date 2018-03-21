#!/usr/bin/python3

#Interviewbit
#Question link: https://www.interviewbit.com/problems/numrange/
#O(n) solution

def numrange(A,lo,hi):
    start = end = 0
    size = len(A)
    count = 0
    for i in range(size):
        if (A[i]>=lo and A[i]<=hi):
            count += 1
            print(A[start:end+1])
            end = i+1
        elif (A[i]>hi):
            start = i+1
            end = i+1
            continue
        else:
            end = start+1
        sum_se = sum(A[start:end+1])
        while (sum_se<=hi and end<size):
            if (sum_se>=lo and sum_se<=hi):
                count += 1
                print(A[start:end+1])
                end += 1
            else:
                end += 1
            sum_se = sum(A[start:end+1])
        start += 1
    return count



if __name__ == '__main__':
    #A = [10, 5, 1, 0, 2]
    #A = [2,5,1,1,2,2,3,4,8,2]
    #A = [ 76, 22, 81, 77, 95, 23, 27, 35, 24, 38, 15, 90, 19, 46, 53, 6, 77, 96, 100, 85, 43, 16, 73, 18, 7, 66 ]
    A = [ 9, 91, 73, 89, 36, 14, 93, 29, 63 ]
    B = 20
    C = 60
    print(numrange(A,B,C))
