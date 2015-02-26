# For nexted for loop, see this post:
# http://stackoverflow.com/questions/25070766/nested-for-loops-recursion?rq=1

def main():
    L = 28123
    abundant = []
    primes = sieve_prime(L)

    for n in xrange(12, L+1):
        if n not in primes:
            if sum(proper_divisors(primes,n)) > n:
                abundant.append(n)

    numbers = range(L+1)
    for x in abundant:
        for y in abundant:
            if x+y <= L:
                numbers[x+y] = 0
    print sum(numbers)


def proper_divisors(primes, n):
    d = {}
    m = n/2
    for p in primes:
        if p > m:
            break
        else:
            while (n%p == 0):
                d[p] = d[p] + 1 if p in d.keys() else 1
                n /= p
    return help_func(d)


def help_func(d):
    l = []
    t = [[x,0] for x in d.keys()]
    while True:
        result = 1
        for x in t:
            result *= x[0]**x[1]
        l.append(result)
        if add_one(t, d.values()):
            break
    # don't return the number itself, but only proper divisors
    return l[0:-1]

def add_one(a, limits):
    for i in xrange(len(a)):
        a[i][1] += 1
        if a[i][1] <= limits[i]:
            return False
        a[i][1] = 0 
    return True



#def help_recursive(d, l):
#    if len(d) == 0:
#        return l
#    else:
#        for i 
#        l.append(d)

    

def sieve_prime(N):
    a = range(2,N+1)
    p = 2
    while p <= N:
        # sieve
        if 2 <= N/p:
            for i in xrange(2, N/p+1):
                if a[i*p-2]:
                    a[i*p-2] = 0
            p += 1
        else:
            return [x for x in a if x]


if __name__ == '__main__':
    main()
