import numpy as np

def main():
    a = sieve_prime(100)
    #n = 224 
    n = 1 
    cond = True
    while cond:
        tri = (n+1)*n/2
        _,deg = get_prime_factors(tri,a)
        if len(deg) > 0:
            cond = reduce(lambda x,y: x*y, map(lambda x: x+1, deg)) <= 500
        else:
            cond = True
        n += 1
    print "The first triangle number that have over 500 divisor is: %d" %tri


def get_prime_factors(N,a):
    #a = sieve_prime(N)
    pf,deg = [],[]
    for x in a:
        if N%x == 0:
            pf.append(x)
            d = 1
            while N%(x**(d+1)) == 0:
                d += 1
            deg.append(d)
    return pf,deg



def sieve_prime(N):
    """Return all prime numbers that is <= N
    """
    a = [2] + range(3,N+1,2)
    p = 3
    while (p < N and N%2) or (p < N-1 and N%2 ==0):
        # sieve
        if p <= N/p:
            for i in xrange(p, N/p+1, 2):
                ind = (i*p-1)/2
                if a[ind]:
                    a[ind] = 0
        # move to the next prime
        ind = (p-1)/2+1
        while a[ind] == 0:
            if (p+2 > N-1 and N%2 == 1) or (p+2 > N-2 and N%2 == 0):
                return [x for x in a if x!=0]
            else:
                p += 2
                ind = (p-1)/2 + 1
        p += 2
    
    return [x for x in a if x!=0] 

if __name__ == '__main__':
    main()
