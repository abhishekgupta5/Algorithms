#!/usr/bin/python3
from re import sub

#Interviewbit- strings
#Question link: https://www.interviewbit.com/problems/zigzag-string/

def convert(A, B):
    A = sub('\.','',A)
    if (B == 1):
        return A
    size = len(A)
    l = []
    row = 0
    down = True
    for i in range(B):
        l.append([])
    for i in range(size):
        l[row].append(str(A[i]))
        if (row == B-1):
            down = False
        elif (row == 0):
            down = True
        if down:
            row += 1
        else:
            row -= 1
    return (''.join([j for i in l for j in i]))

if __name__ == '__main__':
    a = '...............P..........A........Y..P...A...L....I.....S....H...I...R...I...N...G...'
    b = 3
    print(convert(a,b))
