import timeit
def main():
    start = timeit.default_timer()
    a = prime(105000)
    end = timeit.default_timer()
    print "Time is: %f" %(end-start)
    print a[10000]

def prime(N):
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

if __name__ == '__main__':
    main()


