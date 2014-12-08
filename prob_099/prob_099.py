"""Not very good solution, should have used b*log(a)
"""

import numpy as np

def main():
    a = np.genfromtxt('p099_base_exp.txt', dtype='int', delimiter=',')
    
    big = a[0]
    line = 1
    for i in xrange(1,len(a)):
        big,flag = compare(big,a[i])
        line = i if flag else line
    print big,line

def compare(x,y):
    a,b = x
    c,d = y
#    if a**(b/float(d)) > c:
    if b*np.log(a) > d*np.log(c):
        return x,0
    else:
        return y,1

if __name__ == '__main__':
    main()
