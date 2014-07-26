import numpy as np
from update import update

a = []
for line in open("sudoku.txt"):
    li=line.strip()
    if not li.startswith("Grid"):
        a = a + [int(x) for x in li]

# The first axis is "z"
b = np.array(a).reshape(50,9,9)



update(b[44,:,:])











