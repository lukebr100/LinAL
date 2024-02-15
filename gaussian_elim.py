def rowscale(A, i, c):
    # inputs: matrix A, row i, non-zero scalar c
    # output: matrix A after scaling row i by c
    # NOTe: indexing starts @ zero
    n = len(A[0])
    for j in range(n):
        A[i][j] = c * A[i][j]
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rowscale(A, 0, 5)
print(A)
def rowadd(A, i, j, c):
    # inputs: matrix A, row i, row j, non-zero c
    # output: matrix A after performing (c) * Ri + Rj -> Rj
    n = len(A[0])
    for k in range(n):
        A[j][k] = c * A[i][k] + A[j][k]
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rowadd(A, 0, 1, -4)
print(A)

def rowswap(A, i, j):
    n = len(A[0])
    for k in range(n):
        t = A[i][k]
        A[i][k] = A[j][k]
        A[j][k] = t
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rowswap(A, 0, 1)
print(A)

def gaussian_elim(A):
    m = len(A) # number of rows
    n = len(A[0]) # number of columns
    for i in range(n): # for every column
        k = 0 # intialize counter k
        for j in range(i, m - 1): # for fixed column, every row from i to m - 2
            t = A[j - k][i] # store pivot ### subtracting k and iterating j by one means that j - k is constant
            s = A[j + 1][i]
            if t != 0 and s != 0:
                C = - s / t # this is the factor while will eliminate A[j + 1][i]
                rowadd(A, j - k, j + 1, C) # perform row addition of A, j - k, j + 1, C, producing A[j + 1][i] == 0 is True
                k = k + 1 # add to counter to keep pivot position fixed
            elif t == 0 and s != 0: # if pivot postion is zero (to avoid divide by zero in line 41)
                rowswap(A, j - k, j + 1) # swap rows j - k and j + 1
                gaussian_elim(A) # call this function 
    return A
