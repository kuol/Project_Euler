"""
The idea is: consider 
    the first position is: a1 * 9!
    the second position  : a2 * 8!
    ...
    the 10th position    : a10*0!
"""
from math import factorial

N = 1000000
m = 10
a = [0]*m

residual = N-1
for i in xrange(m):
    base = factorial(m-1-i)
    a[i] = residual/base
    residual -= a[i]*base

aa = range(m)
b = [0]*m
for i in xrange(m):
    b[i] = aa[a[i]]
    aa.pop(a[i])
b = [str(x) for x in b]

print ''.join(b)
