#!/usr/bin/pyhton2

#Gives TLE
#Optimized solution exist. Instead of using a list of tuple, store the info in first row and first column of A

def setZeroes(A):
    temp = []
    size_A = len(A)
    for i in range(size_A):
        size_A_in = len(A[i])
        for j in range(size_A_in):
            if (A[i][j] == 0):
                temp.append((i,j))

    for tup in temp:
        for i in range(size_A_in):
            A[tup[0]][i] = 0
        for j in range(size_A):
            A[j][tup[1]] = 0
    #print(temp)
    return A




if __name__ == '__main__':
    l = [[1,0,1],[1,1,1],[1,1,0],[1,1,1]]
    print(setZeroes(l))
