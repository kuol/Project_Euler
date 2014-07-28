import numpy as np
from update import update
from collections import namedtuple

def main():
	a = []
	for line in open("sudoku.txt"):
		li=line.strip()
		if not li.startswith("Grid"):
			a = a + [int(x) for x in li]

	# The first axis is "z"
	b = np.array(a).reshape(50,9,9)
	#A = b[44,:,:]
	A = b[1,:,:]
	
	sudoku_print(A)
	print 
	sudoku(A)
	sudoku_print(A)
	
	result = "Yes!!" if if_solved(A) else "No :("
	print "Have I solved this sudoku? " + result  

def sudoku(A):
	# =====================================================================
	# A: 9x9 np.array int, stores the real sudoku matrix
	# B: 9x9 np.array int, corresponds to A
	#	 undecided position: stores number of options
	#    filled position: stores 10
	# C: 9x9 2d list set of int's
	#    undecided position: stores a set of  all options for each position
	#    filled position: 0
	# =====================================================================
	B = np.zeros((9,9), dtype=int)
	C = [[0 for x in xrange(9)] for x in xrange(9)]
	
	#pivot_stack: 
    #   A stack storing all pivot points that facilitate back-tracing algorithm	
	pivot_stack = []
	StackElem = namedtuple('StackElem', 'ind choice A')
	
	conflict = update(A,B,C)
	while(A.min() == 0):
		if(not conflict):
			i,j = get_leastopt_ind(B)
			elem = StackElem((i,j), list(C[i][j]), A)
			pivot_stack.append(elem)
		else:
			if(len(pivot_stack[-1].choice) > 1):
				del pivot_stack[-1].choice[0]
			else:
				del pivot_stack[-1]
				A = pivot_stack[-1].A
				del pivot_stack[-1].choice[0]
		i,j = pivot_stack[-1].ind
		A[i,j] = pivot_stack[-1].choice[0]
		conflict = update(A,B,C)
				

def get_leastopt_ind(B):
	temp = B.argmin()
	return temp/9, temp%9

def if_solved(A):
	row = [set(A[i,:]) for i in xrange(9)]
	col = [set(A[:,i]) for i in xrange(9)]
	group = [set(list(A[i:i+3, j:j+3].flatten()))
			for i in xrange(0,9,3) for j in xrange(0,9,3)]
	
	all_opts = set(range(1,10))
	for i in xrange(9):
		if row[i] != all_opts or col[i] != all_opts or group[i] != all_opts:
			return False
	return True
	

def sudoku_print(A):
	print '-'*28
	for i in xrange(9):
		for j in xrange(9):
			if j==0:
				print('|'),
			if j%3 == 2:
				print("%d|" %A[i,j]),
			else:
				print("%d " %A[i,j]),      
		print
		if i%3==2:
			print '-'*28 
	


if __name__ == '__main__':
	main()
	















