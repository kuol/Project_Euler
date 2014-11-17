import numpy as np

A = np.genfromtxt('p081_matrix.txt', delimiter=',', dtype='int')
N = A.shape[0]
B = np.zeros((N,N), dtype='int')

B[0,:] = [sum(A[0,:i+1]) for i in xrange(N)]
B[1:,0] = [sum(A[0,:i+1]) for i in xrange(1,N)]
for i in xrange(1,N):
    for j in xrange(1,N):
        B[i,j] = min(B[i-1,j], B[i,j-1]) + A[i,j]

print B[N-1,N-1]


