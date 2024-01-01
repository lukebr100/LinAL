from matrix_tests import test_MatrixVect
from rowops import rowadd, rowswap, rowscale_0, row
from print_matrix import print_matrix

def gaussian_elim(A):
    m = len(A)
    # store number of rows
    if  test_MatrixVect(A) == True:
        n = len(A[0])
        # store the number of columns of A
        C = [ [0 for _ in range(n)] for _ in range(m) ]
        # initailizes matrix of cofactors[sic?]
        B = [row(A, i) for i in range(m)]
        for i in range(n):
            # arbitrary column       
            k = 0
            # counter
            
            for j in range(i, m - 1):
                # row from i, i + 1, ..., m - 2
                
                if B[j - k][i] != 0 and B[j + 1][i] != 0:
                    # the pivot position is non-zero // j - k is constant in this loop   
                    t = B[j - k][i]
                    # store pivot
                    C[j + 1][i] = - (B[j + 1][i] / t)
                    # calculate factor
                    B = rowadd( B, j - k, j + 1, C[j + 1][i])
                    # perform row op
                    k = k + 1
                    # add to counter
                elif B[j - k][i] == 0 and B[j + 1][i] != 0:
                    #  handles if a pivot position is zero, swaps zero in pivot spot w/ a nonzero entry  
                    B = rowswap(B, j - k, j + 1)
                    # rowswap of rows j - k and j + 1 in B
                    return gaussian_elim(B)
                    # run this algorithm on the result, the new element in the pivot is non-zero!
        return B
    else:
        return False

def gaussian_elim_w_b(A, b):
    m = len(A)
    # store number of rows
    if  test_MatrixVect(A)== True and len(b) == m:
        n = len(A[0])
        # store the number of columns of A
        C = [ [0 for _ in range(n)] for _ in range(m) ]
        # initailizes matrix of cofactors[sic?]
        B = [row(A, i) for i in range(m)]
        for i in range(n):
            # arbitrary column       
            k = 0
            # counter
            
            for j in range(i, m - 1):
                # row from i, i + 1, ..., m - 2
                
                if B[j - k][i] != 0 and B[j + 1][i] != 0:
                    # the pivot position is non-zero // j - k is constant in this loop   
                    t = B[j - k][i]
                    # store pivot
                    C[j + 1][i] = - (B[j + 1][i] / t)
                    # calculate factor
                    b[j + 1] = C[j + 1][i] * b[j - k] + b[j + 1]
                    B = rowadd( B, j - k, j + 1, C[j + 1][i])
                    # perform row op
                    k = k + 1
                    # add to counter
                elif B[j - k][i] == 0 and B[j + 1][i] != 0:
                    #  handles if a pivot position is zero, swaps zero in pivot spot w/ a nonzero entry  
                    B = rowswap(B, j - k, j + 1)
                    s = b[j - k]
                    b[j - k] = b[j + 1]
                    b[j + 1] = s
                    # rowswap of rows j - k and j + 1 in B
                    return gaussian_elim_w_b(B, b)
                    # run this algorithm on the result, the new element in the pivot is non-zero!
        return B, b
    else:
        return False

def ge_incon_ID(A, b):
    tildeA = gaussian_elim_w_b(A, b)
    # call GE function, output REF version of A, corresponding b
    n = len(A[0])
    # number of columns
    m = len(A[:])
    # number of rows 
    Zrow = [j for j in range(m) if tildeA[0][j] == [0 for i in range(n)]]
    # IDs ROW of ZEORS in REF of A, returns the ROW INDEX of MATRIX where this occurs
    for k in Zrow:
        # for each ROW of ZEROS
        if b[k] != 0:
            # IF RHS is NON-ZERO and LHS is ZERO -> INCONSISTENT
            # e.g. 0 * x + 0 * y + 0 * z = 2
            # return string("INCONSISTENT"), REF Ax=b
            return 'inconsistent', tildeA
    return 'consistent', tildeA
    # if we get through all ROW of ZEROS and there is NO 0*x + 0*y + 0*z = 2
    # then return "CONSISTENT', REF of AX=b
