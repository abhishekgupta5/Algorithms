#!/usr/bin/python3
from random import randint

def merge(lis1, lis2):
    lis3 = []
    i, j = (0, 0)
    while i < len(lis1) and j < len(lis2):
        if lis1[i] <= lis2[j]:
            lis3.append(lis1[i])
            i += 1
        else:
            lis3.append(lis2[j])
            j += 1
    if lis1[i:]: lis3.extend(lis1[i:])
    if lis2[j:]: lis3.extend(lis2[j:])
    return lis3

def mergesort(lis):
    n = len(lis)
    if n <= 1:
        return lis
    l1 = mergesort(lis[:n/2])
    l2 = mergesort(lis[n/2:])
    return merge(l1, l2)

if __name__ == '__main__':
    lis=[]
    for i in range(50):
        lis.append(randint(50, 1000))
    print(lis)
    print("\n")
    print(mergesort(lis))
