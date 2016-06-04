# 2 <= a <= 100
# 2 <= b <= 100
# Number of distinct terms of a^b?

from math import log
# 1. Brute force:
def brute():
    l = []
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            l.append(a**b)
    print(len(set(l)))

def smart():
    count = 0
    for a in xrange(2, 101):
        count += int(log(100,a))



