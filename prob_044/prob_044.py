# Let p1 > p2, q1 > q2 be petgonal numbers,
# p1 + p2 = q1
# p1 - p2 = q2
# where we want to minize p1-p2.
#
#The above is equivalent to 
# (q1 + q2) / 2 = p1
# (q1 - q2) / 2 = p2
# where we want to minize q2
#
# Testing if a number is petagonal is easy:
# n(3n-1)/2 = p
# ==> n = (1+ sqrt(1+24p)) / 6
#
# This code is not very good, because I don't know the upper limit
# of q2 for each fixed q1. I threw a random 3000 there....
#

from math import sqrt

def pentagonal(x):
    return x*(3*x-1)/2

def if_pent(x):
    test = (1+sqrt(1+24*x))/6
    return test == int(test)

N = 3000


for m in xrange(1,N+2):
    for n in xrange(m,N+2):
        q1 = pentagonal(m)
        q2 = pentagonal(n)
        if if_pent((q1+q2)/2.0) and if_pent((q2-q1)/2.0):
            print q1, q2

