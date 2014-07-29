import numpy as np

def update(A,B,C):
	# 1) A, B, C should be mutable type, and will be modified by this function
	# 2) "update" returns whether conflict

	# Initialize the elements(treated as set here) in row[0-8], col[0,8], group[0-8]
	row = [set(A[i,:]) - set([0]) for i in xrange(9)]
	col = [set(A[:,i]) - set([0]) for i in xrange(9)]
	group = [set(list(A[i:i+3, j:j+3].flatten())) - set([0]) 
			for i in xrange(0,9,3) for j in xrange(0,9,3)]
    
	# Initialize option matrix B
	#  1. B has the same size as A
	#  2. If the position in A has already been filled, then the postion is 10 in B
	#     else, it shows how many options we have to fill this position 
	
	#one_opt = [] # if option is 1, store the option ([0-9])
	all_opts = set(range(1,10))
	one_ind = [] # a queue, if option is 1, store the index(i,j) for the element
	for i in xrange(9):
		for j in xrange(9):
			#compute Group Number by row,col
			k = i/3*3  + j/3
			if A[i,j] != 0:
				B[i,j] = 10
			else:
				known = row[i].union(col[j]).union(group[k])
				B[i,j] = 9 - len(known)
				C[i][j] = all_opts - known
				if B[i,j] == 0:
					return True
				if B[i,j] == 1:
					temp = all_opts - known
					A[i,j] = list(temp)[0] #list(temp) has only one elem, but it's a list
					B[i,j] = 10
					C[i][j] = 0
					one_ind.append((i,j))
					row[i] = row[i].union(temp)
					col[j] = col[j].union(temp)
					group[k] = group[k].union(temp)

	# Fill in all "one_opt" positions in current and consequent matrices
	while(len(one_ind) > 0):
		i1,j1 = one_ind.pop(0)
		k1_i, k1_j = i1/3, j1/3
		k1 = k1_i*3 + k1_j
		# update group
		for i in xrange(3*k1_i, 3*k1_i+3):
			for j in xrange(3*k1_j, 3*k1_j+3):
				if i != i1 and j != j1 and B[i,j]!=10:
					known = row[i].union(col[j]).union(group[k1])
					B[i,j] = 9 - len(known)
					C[i][j] = all_opts - known
					if B[i,j] == 0:
						return True
					if B[i,j] == 1:	
						temp = all_opts - known
						A[i,j] = list(temp)[0]
						B[i,j] = 10
						C[i][j] = 0 
						one_ind.append((i,j))
						row[i] = row[i].union(temp)
						col[j] = col[j].union(temp)
						group[k1] = group[k1].union(temp)
		# update row
		for j in xrange(9):
			if j != j1 and B[i1,j]!=10:
				k = i1/3*3 + j/3
				known = row[i1].union(col[j]).union(group[k])
				B[i1,j] = 9 - len(known)
				C[i1][j] = all_opts - known
				if B[i1,j] == 0:
					return True
				if B[i1,j] == 1:
					temp = all_opts - known
					A[i1,j] = list(temp)[0]
					B[i1,j] = 10
					C[i1][j] = 0 
					one_ind.append((i1,j))
					row[i1] = row[i1].union(temp)
					col[j] = col[j].union(temp)
					group[k] = group[k].union(temp)
		# update col
		for i in xrange(9):
			if i != i1 and B[i,j1]!=10:
				k = i/3*3 + j1/3
				known = row[i].union(col[j1]).union(group[k])
				B[i,j1] = 9 - len(known)
				C[i][j1] = all_opts - known
				if B[i,j1] == 0:
					return True 
				if B[i,j1] == 1:
					temp = all_opts - known
					A[i,j1] = list(temp)[0]
					B[i,j1] = 10
					C[i][j1] = 0 
					one_ind.append((i,j1))
					row[i] = row[i].union(temp)
					col[j1] = col[j1].union(temp)
					group[k] = group[k].union(temp)

#	print A
#	print "="*20
#	print B
	return False 
