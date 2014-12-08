digit_sum = 0 
for i in xrange(1,100):
    for j in xrange(1,100):
        a = list(str(i**j))
        s = sum([int(x) for x in a])
        if s > digit_sum:
            digit_sum = s
print "the maximum digit sum is: %d" %digit_sum
