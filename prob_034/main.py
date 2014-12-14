import numpy as np
from math import factorial

with open('result.txt') as f:
    a = f.readlines()
a = np.unique([int(x.strip()) for x in a])

print a
print sum(a)
