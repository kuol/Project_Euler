"""
Compute how many operations roughly needed for my algorithm
Roughly: 12587
"""

import numpy as np
n = 2776

s = 0
for i in xrange(int(np.sqrt(n))):
    s += n/(i+1)

print s
