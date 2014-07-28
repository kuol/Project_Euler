import numpy as np

A = np.array(range(9)).reshape(3,3)

def modify(A):
	for i in xrange(3):
		for j in xrange(3):
			if A[i,j]%3 == 1:
				A[i,j] = 0

print A
modify(A)
print A
