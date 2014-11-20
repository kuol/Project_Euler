"""Explaination of the algorithm:
    * Notice that the minimum path sum of cells in each column only depends 
      on the column next to it on the left and it self. The minimu path sum
      of the first colum is itself. Thus if we can find minum sum of the 
      second column, we can similarly find the answers of all columns one
      by one

To solve for the second column:
    * Fisrt, solve the minimum path sum to each cell from left and down from
      bottom -- since for the bottom cell, the result is simply its left
      neighbor + itself
    * Then, compare the minimum path sum from top from the top row -- since
      after finish the previous step, the result of the top cell is simply 
      itself.
"""
import numpy as np

def main():
    A = np.genfromtxt('p082_matrix.txt', delimiter=',', dtype='int')
    print min(three_way(A)[:,-1])

def three_way(A):
    """Fine minimum path sum with 3 way moving (up, down, right),
    from any cell in the left most column to any cell in the right
    most column

    Parameters
    ----------
    A : numpy array of int
        Input matrix

    Returns
    -------
    B : numpy array of int 
        Output matrix, with each cell the value of the minium path 
        sum to it.
    """
    N = A.shape[0]
    B = np.zeros((N,N), dtype='int')

    B[:,0] = A[:,0]
    for i in xrange(N-1): # loop columns
        B[N-1,i+1] = B[N-1,i] + A[N-1,i+1]
        #loop rows from bottom, get minimum path from left,below
        for j in xrange(N-2,-1,-1): 
            B[j,i+1] = min(B[j,i], B[j+1,i+1]) + A[j,i+1]
        #loop rows from top, get minimum path from top,left,below
        for j in xrange(N-1):
            B[j+1,i+1] = min(B[j+1,i+1], B[j,i+1]+A[j+1,i+1])
    return B


if __name__ == '__main__':
    main()
