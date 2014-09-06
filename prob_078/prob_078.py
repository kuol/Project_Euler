import numpy as np

def fill_matrix(n):
    M = [[0,1],[0,1]]

    for k in xrange(2,n+1):
        for x in M:
            x.append(x[-1])
        
        M.append([0,1] + [0]*(k-1))
        for j in xrange(2,k+1):
            for jj in xrange(1,j+1):
                M[k][j] = M[k][j] + M[k-jj][jj]
        
        if (M[k][k] % 1000000 == 0 ):
            return k 
    
    print "Can't find such k given max trial size!"
    return 0

def print_2Dlist(M):
    size = len(M)
    for i in xrange(size):
        print M[i]

#M = fill_matrix(7)
#print_2Dlist(M)

#def fill_matrix1(max_size):
#    P = np.array((max_size, max_size))
#    P[0:2,0:2] = np.array([[0,1],[0,1]])
#
#    for n in xrange(2,max_size+1):
#
k = fill_matrix(5000)
print k
