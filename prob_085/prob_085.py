"""
1. For a grid with _m_ rows and _n_ columns, it's easy to see the number of 
   triangles are: (1+2+ ... + m)(1+2+ ... +n) = mn * (mn + m + n +1) / 4

2. Let a = mn, b = (m+n), we have:
    a*(a+b+1) = 8x10^6,
    subject to: b >= 2*sqrt(a)

3. From "2", plug in b = 2*sqrt(a), solve a quadratic equation, we have
   a_max = 2776
   i.e. the maximum of (mn) <= 2776 

Based on the above, I propose the following algorithm:
    Without loss of generality, assume m<=n:
"""

# Author: Kuo Liu
# Contact: liukuo99@gmail.com

import numpy as np

target = 2000000
a_max = 2776
m_max = int(np.ceil(np.sqrt(a_max)))

T,m,n,a= 0, 0, 0, 0
for i in xrange(1,m_max+1):
    n_max = int(np.ceil(float(a_max)/i))
    for j in xrange(n_max,0,-1):
        N = i*(i+1)*j*(j+1)/4
        if abs(N-target) < abs(T-target):
            T,m,n,a = N,i,j,i*j

print "T=%d\tm=%d\tn=%d\ta=%d" %(T,m,n,a)


