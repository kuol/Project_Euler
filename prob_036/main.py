#!/Users/kuol/anaconda/bin/python

def main():
	mysum = 0 
	# 6 digits:
	dec_digits = [0]*6
	for i in range(1,10,2):
		for j in range(10):
			for k in range(10):
				dec_digits[0], dec_digits[5] = i, i
				dec_digits[1], dec_digits[4] = j, j
				dec_digits[2], dec_digits[3] = k, k
				mysum = mysum + verify(dec_digits)
				print dec_digits

	# 5 digits:
	dec_digits = [0]*6
	for i in range(1,10,2):
		for j in range(10):
			for k in range(10):
				dec_digits[1], dec_digits[5] = i, i
				dec_digits[2], dec_digits[4] = j, j
				dec_digits[3] = k
				mysum = mysum + verify(dec_digits)
				print dec_digits

	# 4 digits:
	dec_digits = [0]*6
	for i in range(1,10,2):
		for j in range(10):
			dec_digits[2], dec_digits[5] = i, i
			dec_digits[3], dec_digits[4] = j, j
			mysum = mysum + verify(dec_digits)
			print dec_digits

	# 3 digits:
	dec_digits = [0]*6
	for i in range(1,10,2):
		for j in range(10):
			dec_digits[3], dec_digits[5] = i, i
			dec_digits[4] = j
			mysum = mysum + verify(dec_digits)
			print dec_digits

	# 2 digits:
	dec_digits = [0]*6
	for i in range(1,10,2):
		dec_digits[4], dec_digits[5] = i,i
		mysum = mysum + verify(dec_digits)
		print dec_digits

	# 1 digit:
	dec_digits = [0]*6
	for i in range(1,10,2):
		dec_digits[5] = i
		mysum = mysum + verify(dec_digits)
		print dec_digits

	print "The sum of double-base palindrome numbers within 1,000,000 is: %d" %mysum


def verify(mylist):
	val = 0 
	for i in range(6):
		val = val + 10**(5-i)*mylist[i]
	
	size = val.bit_length()
	size_half = size/2
	bin_digits = [0]*20
	for i in range(size):
		bin_digits[i] = val >> i & 1
	
	flag = True
	for i in range(size_half):
		if bin_digits[i] != bin_digits[size-i-1]:
			flag = False
			break
	
	if flag:
		print val 
		return val
	else:
		return 0 
	
if __name__ == "__main__":
	main()


	



























