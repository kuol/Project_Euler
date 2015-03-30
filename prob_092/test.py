#def perm(digits, k, result):
#    n = len(digits)
#    if k == n-1:
#        result.append(list(digits)) #Attention: list(digits) makes a copy of digits
#    else:
#        for i in xrange(k,n):
#            digits[k], digits[i] = digits[i], digits[k]
#            perm(digits, k+1, result)
#            digits[k], digits[i] = digits[i], digits[k]

def perm1(digits, k, result):
    n = len(digits)
    if k == n-1:
        aa = list(digits)
        bb = int(''.join([str(x) for x in aa]))
        print bb
        result.append(bb) # list(digits) makes a copy of digits
    else:
        for i in xrange(k,n):
            digits[k], digits[i] = digits[i], digits[k]
            perm1(digits, k+1, result)
            digits[k], digits[i] = digits[i], digits[k]

a = []
perm1([1,2,3],0,a)
print a
