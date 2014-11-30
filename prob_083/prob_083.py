import numpy as np

A = np.genfromtxt('p083_matrix.txt', delimiter=',', dtype='int')
M,N = A.shape
B = np.zeros((M,N), dtype='int')

B[0,0] = A[0,0]
branches = [A[0,0]]
bran_ind = [(0,0)]
while B[M-1,N-2]==0 or B[M-2,N-1]==0:
    item = min(branches)
    k = branches.index(item)
    i,j = bran_ind[k]
    if (i-1) >= 0 and B[i-1,j] == 0: #up
        B[i-1,j] = A[i-1,j] + B[i,j]
        branches.append(B[i-1,j])
        bran_ind.append((i-1,j))
    if (i+1) < M and B[i+1,j] == 0: #down
        B[i+1,j] = A[i+1,j] + B[i,j]
        branches.append(B[i+1,j])
        bran_ind.append((i+1,j))
    if (j-1) >= 0 and B[i,j-1] == 0: #left
        B[i,j-1] = A[i,j-1] + B[i,j]
        branches.append(B[i,j-1])
        bran_ind.append((i,j-1))
    if (j+1) < N and B[i,j+1] == 0: #right
        B[i,j+1] = A[i,j+1] + B[i,j]
        branches.append(B[i,j+1])
        bran_ind.append((i,j+1))
    del branches[k]
    del bran_ind[k]

print "left is: %d" %B[M-1,N-2]
print "up is: %d" %B[M-2,N-1]
B[M-1,N-1] = min(B[M-1,N-2], B[M-2,N-1]) + A[M-1,N-1]

print B[M-1, N-1]









