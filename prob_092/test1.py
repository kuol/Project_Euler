def perm(digits, k):
    n = len(digits)
    if k == n-1:
        print digits
    else:
        for i in xrange(k,n):
            digits[k], digits[i] = digits[i], digits[k]
            perm(digits, k+1)
            digits[k], digits[i] = digits[i], digits[k]


perm([1,2,3,4],0)
