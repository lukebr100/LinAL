from matrix_tests import test_VectNum, test_MatrixVect
from transpose import transpose


### do row ops on transposed matrices 
def colswap(A, i, j):
    B = transpose(A)
    B = rowswap(B, i, j)
    B = transpose(B)
    return B
def colscale(A, i, c):
    B = transpose(A)
    B = rowsscale_0(B, i, c)
    B = transpose(B)
    return B

def coladd(A, i, j, c):
    B = trasnpose(A)
    B = rowadd(B, i, j, c)
    B = transpose(B)
    return B
    

### do same algorithms as in rowops.py, but with column(A, i), column(A, j) below

# function, input: A matrix column to access
# output: ith column of A
def col(A, i):
    if test_VectNum(A)[0] == True:
        return [A[i]]
    if test_MatrixVect(A) == True and i < len(A[0]):
        return [row[i] for row in A]
    else:
        return False

def colscale_0(A, i, c):
    if i < len(A) and c != 0:
        # Create a new matrix B with the same values as A
        Ci = col(A, i)
        for j in range(len(Ci)):
            Ci[j] = c * Ci[j]
        return Ci
    else:
        return 'invalid row or scalar'

#input, matrix A rows i, j and nonzero c
#output, c * Ri + Rj \rightarrow Rj, the second Rj in this expressesion
def coladd_0(A, i, j, c):
    B = A[:]
    Ci = colscale_0(B, i, c)
    Cj = col(B, j)
    n = len(Ci)
    for k in range(n):
        Cj[k] = Ci[k] + Cj[k]
    B[j] = Cj
    return B 

def rowswap(A, i, j):
    B = A[:]
    Ci = col(B, i)
    Cj = col(B, j)
    
    t = Cj
    B[j] = Ci
    C[i] = t
    return B
