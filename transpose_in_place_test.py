from transpose_in_place import transpose_in_place_rect, transpose_in_place_square
from print_matrix import print_matrix

two = [[1, 2], [3, 4]]
print('A = ')
print_matrix(two)
print('A^T = ')
print_matrix(transpose_in_place_square(two))


row_heavy = [[1, 2], [5, 6], [7, 8],[9, 10]]
print('B = ')
print_matrix(row_heavy)
print('B^T = ')
print_matrix(transpose_in_place_rect(row_heavy))


col_heavy = [[1, 2, 3, 4],[5, 6, 7, 8]]
print('C = ')
print_matrix(col_heavy)
print('C^T = ')
print_matrix(transpose_in_place_rect(col_heavy))
