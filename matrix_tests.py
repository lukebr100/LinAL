def test_VectNum(x):
    # function: input any object
    # output: binary True correspond to a 'list of numbers', ie, vector
    # False correspond to the elements of x[i] are and object different than a scalar
    if isinstance(x, (list, tuple)) == True:
        # if the object x is a list, then
        L = len(x[:])
        # store length of x in L
        if L == 0:
            # empty list
            return True, L
            # vacuously
        elif L == 1 and isinstance(x[0], (int, float, complex)) == True:
            # list of one element
            return True, L
            # list of one element 1-by-1 matrix
        elif L == 1 and isinstance(x[0], (list, tuple)) == True:
            return test_VectNum(x[0])
        elif L > 1:
            # list w/ 2 or more elements
            for i in range(L):
                # any element of x
                if isinstance(x[i], (int, float, complex)) == False:
                    # is NOT scalar: 
                    return False, L
                    # not a vector of numbers
            return True, L
            # if we get through the whole loop and all elements of x are scalars, it is vector if numbers


def test_MatrixVect(A):
    if test_VectNum(A)[0] == True:
        return True
    if isinstance(A, (list, tuple)) == True:
        L = len(A[:])
        if L == 1 and isinstance(A[0], (list, tuple)) == True:
            return test_MatrixVect(A[0])
        elif L > 1:
            K = [0 for _ in range(L)]
            for i in range(L):
                if isinstance(A[i], (list, tuple)) == True:
                    t = test_VectNum(A[i][:])
                    if t[0] == True:
                        K[i] = t[1]
                    elif t[0] == False:
                        return False
            s = K[0]
            if K.count(s) == len(K):
                return True
            else:
                return False