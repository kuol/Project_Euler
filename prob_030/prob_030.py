"""
Note: increasing digit, the number itself increases exponentially, 
      while the sum([d**5 for d in digits]) only increases linearly.
      So such numbers can't be of many digits.

For 7 digit numbers:
largest sum of **5 is:  9**5x7 = 59,049x7 = 413,343
smallest number    is:  1,000,000

Therefore, such numbers have to have less than 7 digits. 
"""

#for x in xrange(100,1000):
#    h = x/100
#    t = (x-h*100)/10
#    o = x%10
#
#    if h**5 + t**5 + o**5 == x:
#        print x
#
result = []
a = [0]*6

for x in xrange(1000,10000):
    a[0] = x/1000
    a[1] = x/100%10
    a[2] = x/10%10
    a[3] = x%10

    if sum([k**5 for k in a]) == x:
        result.append(x)

for x in xrange(10000,100000):
    a[0] = x/10000
    a[1] = x/1000%10
    a[2] = x/100%10
    a[3] = x/10%10
    a[4] = x%10

    if sum([k**5 for k in a]) == x:
        result.append(x)


for x in xrange(100000,1000000):
    a[0] = x/100000
    a[1] = x/10000%10
    a[2] = x/1000%10
    a[3] = x/100%10
    a[4] = x/10%10
    a[5] = x%10

    if sum([k**5 for k in a]) == x:
        result.append(x)
   
print sum(result)
