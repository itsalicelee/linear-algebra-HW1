from scipy.sparse import *
import numpy as np
'''
  Algorithm
    1. start from the original graph representation,
    multiply the current graph representation to the original graph representation
    2. if we find a value greater or equal to 1 in the diagonal of the matrix, return  True
    3. if we do n(number of nodes) times of the multiplication and all value in the diagonal are 0, return False
    
'''

def p2_has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not

    orig = csr_matrix(sets)
    cur = csr_matrix(sets)

    for i in range(len(sets)):
        cur = cur.dot(orig)
        if np.any(cur.diagonal() != 0):
            return True

    return False



