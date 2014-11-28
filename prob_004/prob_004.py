panlindrome = 0
for i in xrange(999,99,-1):
    for j in xrange(i,99,-1):
        a = [0]*6
        m = i*j
        for k in xrange(5,-1,-1):
            a[k] = m/(10**k)
            m = m - a[k]*(10**k)
        end = 5 if a[5] else 4
        if a[0] == a[end] and a[1] == a[end-1] and a[2] == a[end-2]:
            panlindrome = i*j if panlindrome < i*j else panlindrome

print "The largest planlindrome made by product of two 3-digit numbers is: %d." %panlindrome
