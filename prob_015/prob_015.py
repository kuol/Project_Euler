#!/home/kuol/anaconda/bin/python
import numpy as np

# Recursive + Memorization Table
# Recursive by itself if too slow....


#def f(m,n,M,N):
#    if (m == M) and (n == N):
#        return 1
#    elif m == M:
#        return f(m,n+1,M,N)
#    elif n == N:
#        return f(m+1,n,M,N)
#    else:
#        return f(m+1,n,M,N) + f(m,n+1,M,N)

M, N = 20, 20

A = np.zeros((M+1,N+1))
A[M][:] = 1  # bottom
# right-most (can't initialize as for rows using numpy.array...)
for i in range(M+1):
    A[i][N] = 1

for m in range(M-1,-1,-1):
    for n in range(N-1,-1,-1):
        A[m][n] = A[m+1][n] + A[m][n+1]



print "Total number of routes: %d" %A[0][0]

