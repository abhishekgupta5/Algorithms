#!/usr/bin/python3

def wave_array(A):
    size = len(A)
    A.sort()
    for i in range(size-1):
        if (i%2 == 0):
            if (A[i]<A[i+1]):
                A[i],A[i+1] = A[i+1],A[i]
        else:
            if (A[i]>A[i+1]):
                A[i],A[i+1] = A[i+1],A[i]
    return A

if __name__ == '__main__':
    l = [int(x) for x in input().split()]
    print(wave_array(l))

