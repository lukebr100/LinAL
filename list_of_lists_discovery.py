A = [[1, 2, 3, 10],
    [4, 5, 6, 11],
    [7, 8, 9, 12]] 
# initial matrix
### Open question: what is the difference? in the following three lines
# 1
print(A)
print(A[:])
# 2
print(A[:][0])
print(A[0])
print(A[0][:])


print(A[0][1])          # specific entry // 1st entry of 0th list


B = [[1, 2],
    [3, 4], 
    [5]]            
# not a matrix

C = [1]             
# one-by-one matrix

C1 = []             
# empty list not a matrix

E = [['a', 1, 2],        
    [True, 5, 5],       
    ["dog", "cat", "fish"]]
# matrix ??? you decide
# E present here would fail vector_matrix_test(E)

F = [[[1, 1], 0],           
    [0, 0]]
# without more work, it is not a matrix...
# failed matrices B and F have potential 


G = [[[[1, 2], 3], 1], 
    [1, 1]]
# similarly, higher order lists?

H = ((1, 2),                
    (3, 4))
# a tuple of tuples work as matrices, but for later programs
# they should not be used because tuples are immuatable


I = [(1, 2),    
    (3, 4)]
# list of tuples

J = ([1, 2],
    [3, 4])
# tuple of lists

# higher order tuples also




K = [[0.5, 0],
    [0, 1]]
# print(K[0][0][0]) pop an error, int and float are not scriptable 

L = [[2, [0,1]],
    [3, 4]]
print(len(L[1]))

print( [L[0] for i in range(len(L))] )







# comparing list comprehension and loops
x =[0, 0, 3, 5, 4, 0, 0]                        # initalize vector x with some zero and non-zero entries
print(x)
# we wish to extract the non-zero parts

# LIST COMP.
n = len(x)
v = [x[i] for i in range(n) if x[i] != 0]       # creates list of nonzero numbers x[i] in list (vector) x for all i = 0, 1, ..., n - 1
print(v)             
w = [x[i] for i in range(n) if x[i] == 0]       # creates list of zeros of length equal to the number of zeros in x
print(w)

# (or) REMOVE METHOD
y = x[:]  
print(y, x)                                                      
for i in range(len(w)):         # there are len(w) zeros in x
    y.remove(w[i])              # w[i] == 0 for all i, removing the first entry equal to zero from x in this case four times 0, 1, 2, 3
print(y, x)                        # be careful with indexes w/ looping over x.remove and x.pop



# (or) POP METHOD
y = x[:]
i = 0
n = len(y)
while i < n:                                # while i less than length of length of x
    if y[i] == 0:               # if x[i] is zero
        y.pop(i)                # x at the ith index is no long in x, x = x[0, 1, ..., i - 1, i + 1, ..., n - 1]
        n = n - 1               # length of x shurnk by one
    else:                                   # if x[i] is nonzero
        i = i + 1                           # keep it, look at the next entry of x
print(y, x)                                    # all non-zero entries of x

n = len(x)
# MORE LIST COMP. (which in RStudio)
j = [i for i in range(n) if x[i] == 0]          # indexes where x[i] == 0
k = [i for i in range(n) if x[i] != 0]          # indexes where x[i] != 0
print(j, 'location of zeros in x')
print(k, 'indexes of nonzeros in x')    
