from scipy.sparse import *
import numpy as np

'''
Algorithm
  The loop starts from the first row to the last row(including appended rows)
  1. add first row(key row) to the second row
  2. if the start of the row is the same, and there is only one starting point and one ending point,
    append the added row to the last row of the matrix
  3. if we append any row, delete the first row(key row);
    else do not append and let start again from the next key
  4. if we get a row that is all zero, terminate
''' 
'''
How to implement row addition?
  1. Suppose current row has R rows, create an idenetity matrix I_{r-1}.
  2. Let a vector v a (r-1)*(1) col vector with all elements are 1, 
      and concatenate it to the left hand side of the identity matrix
      to create a assist matrix
  3. Multiply the assist matrix to the original matrix to get the target matrix.
    Each row of the target matrix is the row addition of the key row  
'''


def p1_has_cycle(sets):
    setLen = len(sets)  # total rows r 
    sets = csr_matrix(sets)
    while setLen > 1:  
        keyRow = sets[0]  #keyRow = csr_matrix(sets[i])

        idenMatrix = identity(setLen - 1)  # create an identity matrix with size setLen - 1
        vector = np.ones([setLen-1, 1], dtype = int)
        assistMatrix = hstack([csr_matrix(vector), idenMatrix])
        targetMatrix = assistMatrix.dot(sets)
        
        
        checkLst = np.diff(targetMatrix.indptr) != 0
        #print("target",targetMatrix.toarray())
        if False in checkLst:  # if gets all zeros, there is a cycle
            return True 
        
        startIndex = keyRow.argmin()
        endIndex = keyRow.argmax()  

        checkStart = targetMatrix.T[startIndex]  # check row of target matrix has the same start
        checkEnd = targetMatrix.T[endIndex]
 
        same_start = (checkStart == -1)
        connect = (checkEnd == 0)  # check row of target matrix is connected to key row

        appendBool = np.bitwise_and(same_start.toarray(),connect.toarray())
        appendBool = appendBool[0]
        #print("appendBool",appendBool)
        appendIndex = np.where(appendBool)
        #print("IndexLst",appendIndex)
    
        sets = vstack([sets] + [targetMatrix[appendIndex]])
        sets = sets[1:]  # if append delete the first row
        setLen = sets.shape[0]
    return False



''' 

def p1_has_cycle(sets):
    setLen = len(sets)  # total rows r 
    sets = csr_matrix(sets)
    i = 0
    while setLen > 0:  #while i < setLen:
        keyRow = csr_matrix(sets[0])  #keyRow = csr_matrix(sets[i])

        append = False

        idenMatrix = identity(setLen - 1)  # create an identity matrix with size setLen - 1
        vector = np.ones([setLen-1, 1], dtype = int)
        assistMatrix = hstack([csr_matrix(vector), idenMatrix])
        targetMatrix = assistMatrix.dot(sets)
        checkLst = np.diff(targetMatrix.indptr) != 0

        if False in checkLst:  # if gets all zeros, there is a cycle
            return True 

        negUnitvector = np.zeros([keyRow.shape[1], 1], dtype = int)
        startIndex = keyRow.toarray().tolist()[0].index(-1)  # needs modify 
        negUnitvector[startIndex][0] = - 1
        innerVector = targetMatrix.dot(negUnitvector)

        for row in range(targetMatrix.shape[0]):
            curRow = targetMatrix[row]
            comparasion = np.array_equal(curRow.data, np.array([1,-1]))
            comparasion2 = np.array_equal(curRow.data, np.array([-1,1]))
            if  comparasion or comparasion2: # this row has only -1 and 1
                if innerVector[row][0] == 1:  # and has the same start point as the key row
                    #print("!!")
                    #print("append this row",targetMatrix[row].toarray())
                    append = True
                    sets = vstack([sets, targetMatrix[row]])

        sets = sets[1:]  # if append delete the first row
        setLen = sets.shape[0]
    return False
'''