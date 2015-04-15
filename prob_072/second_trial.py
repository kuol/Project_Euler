def main():
    N = 100
    a = sieve_prime(N)
    total = 0
    for n in xrange(2,N+1):
        total += totient(n,a)
    print "Total reduced proper fraction is: %d" %total




def totient(n, a):
    pfs = get_prime_factors(n,a)
    pfs_minus_one = [x-1 for x in pfs]
    denom = multiply(pfs)
    numer = multiply(pfs_minus_one)
    return n*numer/denom


def multiply(l):
    result = 1
    for x in l:
        result *= x
    return result

def get_prime_factors(N,a):
    #a = sieve_prime(N)
    pf = []
    for x in a:
        if x >= N:
            return pf
        elif N%x == 0:
            pf.append(x)
    return pf



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
