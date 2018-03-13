#!/usr/bin/pyhton2

#Gives TLE
#Optimized solution exist. Instead of using a list of tuple, store the info in first row and first column of A(see setZeroesFast())

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


#Optimized algo
def setZeroesFast(A):
    N = len(A)
    M = len(A[0])
    del_first_row = False
    del_first_col = False

    for i in range(N):
        if A[i][0] == 0:
            del_first_row = True
            break
    for i in range(M):
        if A[0][i] == 0:
            del_first_col = True
            break

    for i in range(N):
        for j in range(M):
            if A[i][j] == 0:
                A[i][0] = 2
                A[0][j] = 2


    for i in range(1,N):
        for j in range(1,M):
            if A[i][0] == 2:
                A[i][j] = 0
            elif A[0][j] == 2:
                A[i][j] = 0
    for i in range(N):
        if A[i][0] > 1 or del_first_row:
            A[i][0] = 0
    for i in range(M): 
        if A[0][i] > 1 or del_first_col:
            A[0][i] = 0

    return A



if __name__ == '__main__':
    l = [[1,0,1],[1,1,1],[1,1,0],[1,1,1]]
    print(setZeroesFast(l))
