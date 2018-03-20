#!/usr/bin/python3

def maxone(A, B):
    i = 0
    j = 0
    sum_0 = 0
    ans_i = ans_j = 0
    while(i<len(A)):
        if (A[i] == 0):
            sum_0 += 1
        i += 1

        if sum_0>B:
            while(sum_0>B):
                if A[j]==0:
                    sum_0 -= 1
                j += 1
        if  i-j> ans_i-ans_j:
            ans_i = i
            ans_j = j
    return [k for k in range(ans_j,ans_i)]


if __name__ == '__main__':
    A = [1,0,1,0,1,1,0,0,0,1,0]
    B = 2
    print(maxone(A, B))
