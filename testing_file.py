### testing files in LinAl folder
from matrix_tests import test_VectNum, test_MatrixVect
from column_i import column
from row_i import row
from print_matrix import print_matrix
from rowops import rowscale_0, rowswap, rowadd
from dot_pr_and_matrix_mult import dot_product, matrix_mult
from gaussian_elim import gaussian_elim, gaussian_elim_w_b, ge_incon_ID
from rank_col_space_basis import rank, piv_pos, col_space_basis
from row_space2ways import row_space_std, row_space_t
from transpose import transpose



### matrix_tests          
N = []
print('N')
print(N)
print(test_VectNum(N), 'N test_VectNum')
print(test_MatrixVect(N), 'N test_MatrixVect')


M = [[1, 2, 3], [3, 4]]
print('M')
print_matrix(M)
print(test_VectNum(M), 'M vecnum_test: not a vector of numbers')
print(test_MatrixVect(M), 'M not a matrix')


A = [[1, 0], [0, 1]]
print_matrix(A)
print('A')
print(test_VectNum(A), 'A not a vector')
print(test_MatrixVect(A), 'A is a matrix')

B = [1, 2, 3, 4]
print(B)
print('B')
print(test_VectNum(B), 'B test_VectNum')
print(test_MatrixVect(B), 'B test_MatrixVect')

C = [[1], [2], [3]]
print_matrix(C)
print('C')
print(test_VectNum(C), 'C test_VectNum')### FIX
print(test_MatrixVect(C), 'C test_MatrixVect')


D = [[[1, 0],0], [0, 1]]
print(D, 'D')
print(test_VectNum(D), 'D test_VectNum')
print(test_MatrixVect(D), 'D test_MatrixVect')



### column
A = [[1, 2], 
     [3, 4]]
print('A')
print_matrix(A)
print(column(A, 0), 'first column of A')
print(column(A, 1), 'second column of A')



### row
A = [[3, 5], 
     [4, 6]]
print('A')
print_matrix(A)
print(row(A, 0), 'first row of A')  
print(row(A, 1), 'second row of A')



### transpose
B = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print('B')
TB = transpose(B)
print('transpose of B')
print_matrix(TB)




### DP//matrix multiplcation 
A = [[1, 1], [0, 1]]
B = [[1, 2], [3, 4]]
print('A')
print_matrix(A)
print('B')
print_matrix(B)
C = matrix_mult(A, B)
print('C = A*B')
print_matrix(C)
x = [1, 1]
print(x, 'x')
y = [5, 3]
print(y, 'y')
print(dot_product(x, y), '= x*y')



### rowops 
A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
print('A')
print_matrix(A)
print(rowscale_0(A, 0, -6), 'rowscale_0(A, 0, -6)')
print(rowadd(A, 0, 1, -6), 'rowadd(A, 0, 1, -6)')
print(rowswap(A, 0, 1), 'rowswap(A, 0, 1)')
print_matrix(A)
print('A again check: GOOD')



### GE
A = [[1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]]
print_matrix(A)
print('A')
tildeA = gaussian_elim(A)
print('REF of A')
print_matrix(tildeA)
A = [[1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]]
b = [10, 11, 12]
print('A')
print_matrix(A)
print(b, 'b')
tildeA = ge_incon_ID( A, b )
print(tildeA[0])
print('REF of A')
print_matrix(tildeA[1])
print_matrix(A)
print('A again: GooD')

C = [[1, 2, 3], [4, 5, 6], [7,8, 9], [10, 11, 12]]
c = [1, 1, 1, 1]
print('C')
print_matrix(C)
print(c, 'c')
tildeC = gaussian_elim_w_b( C, c )
print(tildeC[0])
print('REF of C')
print_matrix(tildeC[1])

E = [[0, 0, 0], [1, 1, 1], [1, 2, 3]]
b = [4, 5, 2]
print('E')
print_matrix(E)
print(b, 'b')
tildeE = ge_incon_ID( E, b )
print(tildeE[0])   
print('REF of E')
print_matrix(tildeE[1])



### rank, piv_pos, column space
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [1, 2, 3]
print('A')
print_matrix(A)
print(b, 'b')
print(rank(A), 'rank')

print(piv_pos(A), 'piv_pos')
print(col_space_basis(A), 'col space basis')




### row space
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(row_space_std(A), 'std rowspace')
print(row_space_t(A), 'transpose rowspace')