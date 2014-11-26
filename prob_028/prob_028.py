"""
Level: distance from side to center
Size : length of each side
Difference: within each level and with the end of previous level
Start: start value of each level
End  : end value of each level
============================================
Level    Size    Difference    Start    End
n        2n+1    2n          
0        1       0             1        1
1        3       2             3        9
2        5       4             13       25
"""

N = 1001/2
end = 1
count = 1
for n in xrange(1,N+1):
    start = end + 2*n
    end = start + 2*n*3
    s = (start + end)*2
    count += s

print "Sum of diagonals is: %d" %count
