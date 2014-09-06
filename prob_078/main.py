# Implement with fixed size numpy array instead

import numpy as np
import timeit

start = timeit.default_timer()


n = 1000 
A = np.zeros((n,n), dtype='int64')
A[:,1] = 1

#B = np.empty(n)
#B[0] = 0 
#B[1] = 1
for k in xrange(2,n):
    A[0:k,k] = A[0:k,k-1]

    for j in xrange(2,k+1):
        for jj in xrange(1,j+1):
            A[k,j] = A[k,j] + A[k-jj][jj]
    
#    B[k] = A[k,k]
    if (A[k][k] % 1000000 == 0):
        print "Bingo! Smallest K is %d" %k
        break


stop = timeit.default_timer()
print "Time to run the program: %f" %(stop - start)

#print B
#np.savetxt("B.txt", B, delimiter='\n')
#np.savetxt("mat.txt", A, delimiter=', ')
#print A
#print "Failed"

