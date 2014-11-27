import timeit
def main():
#    start = timeit.default_timer()
#    a = prime(2000000)
#    end = timeit.default_timer()
#    print sum(a)
#    print "Time is: %f" %(end-start)

    print sieve_prime(2000000)

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


if __name__ == '__main__':
    main()


