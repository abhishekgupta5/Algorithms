#!/usr/bin/python3

def factors(n):
    if n==1:
        print(1)
        return
    root = int((n**(0.5)+1))
    lis=[]
    for i in range(1,root):
        if (n%i == 0):
            lis.append(i)
            if (i != n**0.5):
                lis.append(int(n/i))
    #lis.sort()
    lis.sort()
    print(lis)

n = int(input('Enter number: '))
factors(n)
