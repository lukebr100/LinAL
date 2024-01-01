from matrix_tests import test_VectNum, test_MatrixVect
from row_i import row
from column_i import column

def dot_product(x, y):
    # function (dot/scalar product): input number vectors x, y
    # output: scalar given by Euclidean inner product
    # store length of x into var a
    z = 0
    # set counter
    s = test_VectNum(x)
    t = test_VectNum(y)
    if s[0] == True and t[0] == True and s[1] == t[1]:
        a = s[1]
        for i in range(a):
        # for i ranging over all indices of x, y
            z = z + x[i] * y[i]
            # overwrite z w/ trhe previous value of z and the product of x[i], y[i]
        return z
        # after the loop, return z, x[i]*y[i] for all i
    else:
        return False
        # dimension of vectors needs to be the same 

    

def matrix_mult(A, B):
    # matrix multiplcation
    if test_MatrixVect(A) == True and test_MatrixVect(B) == True:
        mA = len(A[:])
        # rows of A
        nA = len(A[0][:])
        # cols of A
        
        mB = len(B[:])
        # rows of B
        nB = len(B[0][:])
        # cols of B
        
        if nA == mB: # cols of A == rows of B (compatible)
            C = [[0 for k in range(nB)] for l in range(mA)]
            # intialize product C w/ rows of A and cols of B
            
            for i in range(mA):
                # row of A
                for j in range(nB):
                    # col of B
                    A_rowi = row(A, i)
                    # store row i of A into var A_rowi
                    B_colj = column(B, j)
                    # store col j of B into var B_colj
                    C[i][j] = dot_product(A_rowi, B_colj)
                    # the ith row, jth col of C is given by the dot product of A_rowi, B_colj
            return C
            # after nest for loops, print matrix C
        else:
            return 'incompatible matrices'
            # number of cols of A == number of rows of B 