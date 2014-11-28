import timeit
def main():
    start = timeit.default_timer()
    a = sieve2_prime(2000000)
    end = timeit.default_timer()
    print a
    print "Time is: %f" %(end-start)


def brute_prime(N):
    """ Find primes numbers that are less than N
    """
    p  = [2]
    for i in xrange(3,N,2):
        flag = 1
        for j in p:
            if i%j == 0:
                flag = 0
        if flag:
            p.append(i)
    return p

# Time is: 1.107616
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
                return sum(a)
            else:
                p += 1
        p += 1
    return sum(a)

# Time is: 0.884902
# Modified Sieve, only check numbers > p*p
def sieve1_prime(N):
    a = range(2,N+1)
    p = 2
    while p <= N:
        # sieve
        if p <= N/p:
            for i in xrange(p, N/p+1):
                if a[i*p-2]:
                    a[i*p-2] = 0
        # move to the next prime
        while a[p-1] == 0:
            if p+1 >= N:
                return sum(a)
            else:
                p += 1
        p += 1
    return sum(a)

# Time is: 0.577991
# Modified Sieve, 
#    * only check numbers > p*p
#    * only check odd numbers
def sieve2_prime(N):
    a = [2] + range(3,N+1,2)
    p = 3 
    while p <= N:
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
                return sum(a)
            else:
                p += 2
                ind = (p-1)/2 + 1
        p += 2
    return sum(a)

if __name__ == '__main__':
    main()


