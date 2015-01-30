from math import sqrt, factorial

def main():
    test_primes = sieve_prime( int(sqrt(987654321)) + 1 )
    temp = 0
    for i in xrange(9,3,-1):
        temp = max(temp, largest(i,test_primes))
        if temp:
            print temp
            return 0
    return -1


def largest(n, primes):
    """
    Test if n-digit pandigital number is a prime number.
    If so, return the largest n-digit pandigital number,
    otherwise, return 0

    Parameters
    ----------
    n : int
        n-digit pandigital numbers to test, must satisfy 1 <= n <= 9

    primes : list of int
        All potential prime divisors, i.e. all prime number 
        <= ceil(sqrt(987654321)) 
    
    Returns
    -------
    int :
        The largest prime number of n-digit pandigital number;
        or 0, if not found
    """
    l = range(1,n+1)
    a = permute(l,primes)
    return max(a) if a else 0


def permute(l, primes, m=0, a=[]):
    """ Generate all pandigital numbers that is made up by digits in l,
    test if they are prime numbers by using primes.

    Parameters
    ----------
    l : list of int
        Must be 1--n, where 1<=n<=9.

    primes: list of int
        Prime numbers that are candidates to test if the pandigital number
        is a prime number.
    
    m : int, default 0
        The starting position for recursion.

    Returns
    -------
    a : list of int, default []
        The list that stores all pandigital prime numbers that is made from
        digits in list l. 
    """
    n = len(l)
    if m < n-1:
        for i in xrange(m,n):
            l[m], l[i] = l[i], l[m]
            permute(l, primes, m+1, a)
            l[m], l[i] = l[i], l[m]
    else:
        N = 0
        for i in xrange(n):
            N += l[i]*10**i
        N_sqrt = sqrt(N)
        for x in primes:
            if x > N_sqrt:
                a.append(N)
                break
            elif not(N%x): # N is not a prime number
                break
    return a


def sieve_prime(N):
    a = range(2,N+1)
    p = 2
    while p <= N:
        # sieve
        if 2 <= N/p:
            for i in xrange(2, N/p+1):
                if a[i*p-2]:
                    a[i*p-2] = 0
        # move to the next prime
        while a[p-1] == 0:
            if p+1 >= N:
                return [x for x in a if x!=0]
            else:
                p += 1
        p += 1
    return [x for x in a if x!=0]

if __name__ == '__main__':
    main()
