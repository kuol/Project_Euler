import numpy as np
from fractions import gcd

def main():
    thres = 1000000
    low, high = 1800, 1850
    cond = getCentroid((low+high)/2) > thres
    auxcond = getCentroid((low+high)/2 -1) < thres

    while not (cond and auxcond):
        if cond:
            low = (low+high)/2
        else:
            high = (low+high)/2
        cond = getCentroid((low+high)/2) > thres
        auxcond = getCentroid((low+high)/2 -1) < thres
    print("The least value of M is: %d") %(low+high)/2

def getCentroid(M):
    triples = genPrimitiveTriples(M, 2*M)
    
    count = 0
    for x in triples:
        K = min(M/x[0], 2*M/x[1])
        for k in xrange(1,K+1):
            a,b = k*x[0], k*x[1]
            #for i in xrange(1,a/2):
            #    L,W,H = i,a-i,b
            #    print ("%d, %d, %d") %(L,W,H)
            #if b/2>a:
            #    for i in xrange(b/2, a+1):
            #        L,W,H = b-i,i,a
            #        print("%d, %d, %d") %(L,W,H)
            if b <= M:
                num = a/2 if b/2>a else a/2 + b/2 - (b-a-1)
            else:
                num = 0 if b/2>a else b/2 - (b-a-1)
            count += num
            #print("[%d, %d, %d]: %d") %(a,b,k*x[2],num)
    return count


def genPrimitiveTriples(A1,A2):
    """Generate Pythagorean primitive triples using Euclid's formula:
        * a = m^2 - n^2
        * b = 2mn
        * c = m^2 + n^2
      Parameters
      ----------
      A1: int
          Maximum of shorter leg
      A2: int
          Maximum of longer leg
      
      Returns
      -------
      triples: list of tuples (int, int, int)
        All Pythagorean primitive triples
    """
    triples = []
    M = A1 
    for m in xrange(2,M+1):
        for n in xrange(1,m):
            a,b,c = m*m-n*n, 2*m*n, m*m+n*n
            a,b = min(a,b), max(a,b)
            condition = min(a,b) < A1 and max(a,b) < A2
            if gcd(m,n)==1 and (m-n)%2 and condition:
                #print("[%d, %d]: (%d, %d, %d)") %(m,n,m*m-n*n, 2*m*n, m*m+n*n)
                triples.append((a,b,c))
    return triples

#thres = 1000000
#low, high = 1800, 1850
#cond = getCentroid((low+high)/2) > thres
#auxcond = getCentroid((low+high)/2 -1) < thres
#
#while not (cond and auxcond):
#    if cond:
#        low = (low+high)/2
#    else:
#        high = (low+high)/2
#    cond = getCentroid((low+high)/2) > thres
#    auxcond = getCentroid((low+high)/2 -1) < thres
#print("The least value of M is: %d") % (low+high)/2


if __name__ == "__main__":
    main()
