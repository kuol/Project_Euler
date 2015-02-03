""" The idea is that:
    1) Check each possible denominator: 1 ~ 1,000,000
    2) For each, the candidate for the numerator has to be: d*3/7
    3) Check if (n,d) == 1 and note down the difference between this number and 3/7
"""

from fractions import gcd 

D = 1000000
diff_min = float(3)/7  - float(2)/5
for d in xrange(9,D+1):
    n = d*3/7
    while gcd(n,d) != 1:
        n -= 1
    diff = float(3)/7 - float(n)/d
    if diff < diff_min:
        n_min, d_min, diff_min = n, d, diff

print "The numerator is %d and the denominator is %d" %(n_min, d_min)
