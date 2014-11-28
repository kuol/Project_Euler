import numpy as np

def main():
    N = 600851475143
    M = int(np.sqrt(N))
    a = sieve_prime(M)
    a = [x for x in a if x!=0]

    pf,deg = [],[]
    for x in a:
        if N%x == 0:
            pf.append(x)
            d = 1
            while N%((d+1)*x) == 0:
                d += 1
            deg.append(d)
    print pf[-1]

def sieve_prime(N):
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
                return a
            else:
                p += 2
                ind = (p-1)/2 + 1
        p += 2
    return a

if __name__ == '__main__':
    main()
