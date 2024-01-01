from gaussian_elim import gaussian_elim
from transpose import transpose
# MAKE colops.py, MOVE column there, ADD three column operations, DO NOT import colswap, coladd, colscale 
from colops import column
from rowops import row

def rank(A):
    # rank function: determines rank of a matrix <->  # of non-zero rows in REF, # of vectors in column space/row space, # of pivots
    # input: matrix
    # output: rank, REF of matrix A
    tildeA = gaussian_elim(A)
    if tildeA == False:
        # happens if A is not a matrix
        return False
    # reduce A and store into var tildeA
    mA = len(tildeA[:])
    # total number of rows
    j = 0
    # counter
    for i in range(mA):
        # arbitrary row of tildeA
        rowtildeA_i = row(tildeA, i)
        if rowtildeA_i.count(0) == len(A[0]):
            # if the number of zero in ith row of A ==  number of columns of A
            j = j + 1
            # add one to counter (counting zero rows)
    return mA - j, tildeA
        # return total number of rows minus number of zero rows, ie, num of nonzero rows

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(rank(A)[0])
# print(rank(A)[1])
# test, rank(A)[0] == 2
# rank(A)[1] REF form of A

def piv_pos(A):
    Ar = rank(A)
    r = Ar[0]
    tildeA = Ar[1]
    m = len(tildeA)
    n = len(tildeA[0])
    J = [0 for i in range(r)]
    for i in range(r):
        for j in range(n):
            if tildeA[i][j] != 0:
                J[i] = j
                break
    return J, r, tildeA

def col_space_basis(A):
    Jr = piv_pos(A)
    J = Jr[0]
    r = Jr[1]
    return [column(A, i) for i in J]


### taking TRANSPOSE, then computing COL_SPACE_BASIS is equivalent to BASIS for ROWSPACE
### ADD justifcation
def row_space_t(A):
    tA = transpose(A)
    return col_space_basis(tA)


### taking NON-ZERO ROWS of REF of A as BASIS for ROWSPACE
def row_space_std(A):
    rA = rank(A)
    r = rA[0]
    tildeA = rA[1]
    return [row(tildeA, i) for i in range(r)]

