import numpy as np
from prob_96 import color_print

A = np.array(range(81)).reshape(9,9)
B = np.copy(A)
B[4,4], B[4,5], B[4,6] = 0, 0, 0

color_print(A,B)

