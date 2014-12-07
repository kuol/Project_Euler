from fractions import gcd
def main():
    seq = [2] 
    for k in xrange(1,34):
        seq += [1,2*k,1]
    #print approx_e(seq)
    a = list(numer(seq))
    a = [int(x) for x in a]
    print sum(a)

def numer(seq):
    N = len(seq)
    val = (seq[N-1],1)
    for i in xrange(N-1,0,-1):
        val = add(reciprocal(val), (seq[i-1],1))
    return str(val[0])

def add(r1, r2):
    a,b = r1
    c,d = r2
    r = (a*d+b*c, b*d)
    g = gcd(r[0], r[1])
    return (r[0]/g, r[1]/g)


def reciprocal(r):
    return (r[1], r[0])


def approx_e(seq):
    N = len(seq)
    val = seq[N-1]
    for i in xrange(N-1,0,-1):
        val = 1/float(val) + seq[i-1]
    return val

if __name__ == '__main__':
    main()
