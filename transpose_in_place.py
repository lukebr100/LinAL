# transpose in-place 
# input a rectangular matrix
# output the transpose matrix
# rows swapped with columns
# if A = (a)_{ij} for all i, j, then
# A^T = (a)_{ji}



from matrix_tests import test_MatrixVect


def made_square(A):
    if test_MatrixVect(A) == True:
        m = len(A[:]) # rows
        n = len(A[0][:]) # cols
        p = max(m , n) # max row or col
    if m < p: # number of rows smaller than number of columns
        diff = n - m
        for v in range(diff): # for the difference in rows from cols
            A.append([0 for u in range(n)]) # add a list of zeros to the end
            # A is now square
        return A
    if n < p: # number of cols smaller than number of rows
        diff = m - n 
        for v in range(m): 
            for u in range(diff):
                A[v].append(0)
        return A
    
    
def transpose_in_place_square(A):
    m = len(A)
    k = 1
    for i in range(m):
        for j in range(k, m):
            A[i][j], A[j][i] = A[j][i], A[i][j]
        k = k + 1
    return A
       
    
def transpose_in_place_rect(A):
    a = len(A)
    b = len(A[0])
    if a == b:
        A = transpose_in_place_square(A)
    else:
        A = made_square(A)
        A = transpose_in_place_square(A)
        if a < b:
            for j in range(b):
                for i in range(b - a):
                    A[j].pop(-1)
            return A
        if b < a:
            for i in range(a - b):
                A.pop(-1)
            return A
        
    
    print(A)