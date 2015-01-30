def main():
    d = range(10)
    p = [2,3,5,7,11,13,17]
    a = permute(d, p)
    print sum(a)

def permute(l, primes, m=0, a=[]):
    """ Generate all pandigital numbers that is made up by digits in l,
    test if they are prime numbers by using primes.

    Parameters
    ----------
    l : list of int
        Must be 1--n, where 1<=n<=9.

    primes: list of int
        Prime numbers that are candidates to test if the pandigital number
        satisfies the substring divisibility rule.
    
    m : int, default 0
        The starting position for recursion.

    Returns
    -------
    a : list of int, default []
        The list that stores all pandigital prime numbers that satisfy the
        substring divisibility rule.
    """
    n = len(l)
    if m < n-1:
        for i in xrange(m,n):
            l[m], l[i] = l[i], l[m]
            permute(l, primes, m+1, a)
            l[m], l[i] = l[i], l[m]
    elif l[0]:
        for i in xrange(1,8):
            M = l[i]*100 + l[i+1]*10 + l[i+2]
            if M%primes[i-1]:
                break
            elif i==7:
                N = 0 
                for j in xrange(10):
                    N += l[9-j] * 10**j
                a.append(N)
    return a


if __name__ == '__main__':
    main()
