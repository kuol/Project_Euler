def main():
    N = 100
    a = sieve_prime(N)
    total = 0
    for n in xrange(2,N+1):
        pfs = get_prime_factors(n,a)
        total += count_proper_fractions(n,pfs)
    print "Total reduced proper fraction is: %d" %total

def count_proper_fractions(denom, pfs):
    """count number of proper fractions with denominator: denom
    
    Parameters
    ----------
    denom : int
        denominator.

    pfs : list of int
        Prime facotors of "denom"

    Returns
    -------
    count : int
        Count of proper fractions with denominator: denom
    """
    count = denom
    m = len(pfs)
    for i in xrange(1, 2**m):
        pos, k = help_func(i,m)
        count += (-1)**k * (denom/multiply(pfs,pos))
    return count


def help_func(i,m):
    """ help function, return the position and number of 1's in inter i's binary form. 
    For example: i=10 and m= 4. Since 10's binary form is 0b1010, help_func(i,m) will 
    return: ([1,3],2)
    """
    pos = []
    k = 0
    for n in xrange(m):
        temp = i >> n & 1
        if temp:
            k += temp
            pos.append(n)
    return pos,k

def multiply(pfs, pos):
    result = 1
    for i in pos:
        result *= pfs[i]
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
