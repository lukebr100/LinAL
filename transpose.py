from matrix_tests import test_MatrixVect

def transpose(A):
    if test_MatrixVect(A) == True:
        m = len(A[:])
        n = len(A[0][:])
        tA = [[A[i][j] for i in range(m)] for j in range(n)]
        return tA
