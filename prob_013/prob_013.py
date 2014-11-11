import numpy as np

def main():
    a = np.empty((100,12),dtype='int')

    # Read file
    i = 0
    with open ('numbers.txt') as f:
        for line in f:
            a[i,:] = [int(x) for x in line.strip('\n')][:12]
            i += 1
    f.close()
    
    b = np.sum(a, axis=0)

    digits = [0]*14
    for i in xrange(12):
        h,t,o = digitize(b[i])
        digits[i] += h
        digits[i+1] += t
        digits[i+2] += o

    carry_over = 0
    for i in xrange(13,-1,-1):
        digits[i] += carry_over
        carry_over = digits[i]/10
        digits[i] %= 10

    print "The first 10 digits are:"
    print digits[:10]
    print ''.join(str(x) for x in digits[:10])
        




def digitize(x):
    h = x/100
    t = (x - h*100)/10
    o = x%10
    return h,t,o

if __name__ == '__main__':
    main()
    
