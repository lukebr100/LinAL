from matrix_tests import test_VectNum, test_MatrixVect

def row(A, i):
    B = A.copy()
    if test_VectNum(B)[0] == True and i == 0:
        return B[:]
    elif test_MatrixVect(B) == True and i < len(B[:]):
        return B[i][:]
    else:
        return False
        
def rowscale_0(A, i, c):
    if i < len(A) and c != 0:
        # Create a new matrix B with the same values as A
        Ri = row(A, i)
        for j in range(len(Ri)):
            Ri[j] = c * Ri[j]
        return Ri
    else:
        return 'invalid row or scalar'

def rowscale_1(A, i, c):
    if i < len(A) and c != 0:
        # Create a new matrix B with the same values as A
        B = [row[:] for row in A]
        Ri = B[i]
        for j in range(len(Ri)):
            Ri[j] = c * Ri[j]
        return Ri
    else:
        return 'invalid row or scalar'

#input, matrix A rows i, j and nonzero c
#output, c * Ri + Rj \rightarrow Rj, the second Rj in this expressesion
def rowadd(A, i, j, c):
    B = A[:]
    Ri = rowscale_0(B, i, c)
    Rj = row(B, j)
    n = len(Ri)
    for k in range(n):
        Rj[k] = Ri[k] + Rj[k]
    B[j] = Rj
    return B 

def rowswap(A, i, j):
    B = A[:]
    Ri = row(B, i)
    Rj = row(B, j)
    
    t = Rj
    B[j] = Ri
    B[i] = t
    return B
