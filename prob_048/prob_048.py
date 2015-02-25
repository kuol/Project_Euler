from math import log

N = 9999999999
M = 10000000000
result = 1
for n in xrange(2, 1001): # start from 2 to avoid log(N)/log(1) = infity
    max_power = int(log(N)/log(n))
    if n < max_power:
        current = n**n
    else:
        current = n**max_power
        for i in xrange(max_power+1, n+1):
            current *= n
            current %= M 
    result += current
result = result % M 
print "The last 10 digits are: %d" %result
