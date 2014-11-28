import math

a = str(math.factorial(100))
a = list(a)
a = [int(x) for x in a]
print sum(a)
