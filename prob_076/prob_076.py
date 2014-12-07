""" This problem is very similar to Problem 78, but easier.
A dynamic programming can solve this easily. 

The idea is to build a matrix A, such that 
   * A[i][j]: # of ways to sum to i, where the largest summand is j
Denote:
   * l(i,j): # of ways to sum to i, where the larest summand <= j

Easy to see that, l(i,j) = sum(A[i][:j])
"""

def num_sum(N,k):
    """ Brute force:compute number of ways to add to sum: N, using
    at least two positive integers
    """
    if N < 0:
        return 0
    elif N==0:
        return 1
    else:
        s = 0
        for i in xrange(1,k+1): #largest component is i
            s += num_sum(N-i,i)
        return s

# Creating an extra row/col, thus index is easier to manipulate
N = 100
A = [[0,1] + [0]*(N-1) for _ in xrange(N+1)]

for i in xrange(2,N+1):
    A[i][i] = 1
    for j in xrange(2,i):
        k = min(j, i-j)
        A[i][j] = sum(A[i-j][:k+1])


print sum(A[100][:-1])
