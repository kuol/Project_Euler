import math

def main():
    N = 10000
    amicable = []
    for i in xrange(N):
        if i not in amicable:
            j = get_proper_divisors_sum(i)
            if j != i and get_proper_divisors_sum(j) == i:
                amicable += [i,j]

    print amicable
    print "Sum of all amicable pairs under %d is: %d" %(N,sum(amicable))


def get_proper_divisors_sum(N):
    M = int(math.sqrt(N))
    pd = [1]
    for i in xrange(2,M+1):
        if not(N%i):
            pd = pd + [i,N/i]
    return sum(pd)
            
if __name__ == '__main__':
    main()


