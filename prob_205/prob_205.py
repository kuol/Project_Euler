def main():
    """compute the probability that Pete beats Collin
    """
    p,c = float(4**9), float(6**6)
    pete = [0.0]*37
    colling = [0.0]*37
    for i in xrange(9,37):
        pete[i] = num_combine(i,9,4)
    for i in xrange(6,37):
        colling[i] = num_combine(i,6,6)
    
    pete = [x/p for x in pete]
    collin = [x/c for x in colling]
    prob = sum(collin[6:9])
    for i in xrange(9,36):
        prob += collin[i]*(sum(pete[i+1:]))

    print "The probability that Pete beats Collin is %.7f" %prob



def num_combine(N,M,k):
    if N > k*M or N < M:
        return 0
    if M == 1:
        return 1 if N <= k else 0
    else:
        s = 0
        for i in xrange(1,k+1):
            s += num_combine(N-i, M-1, k)
        return s


if __name__ == '__main__':
    main()
