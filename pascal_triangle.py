#!/usr/bin/python3

def pascal_triangle(n):
    l = []
    for i in range(n):
        l.append([])
        l[i].append(1)
        for j in range(1,i):
            l[i].append(l[i-1][j-1]+l[i-1][j])
        if (i != 0):
            l[i].append(1)
    return l[-1]

if __name__ == '__main__':
    n = int(input("No of rows"))
    print(pascal_triangle(n+1))
