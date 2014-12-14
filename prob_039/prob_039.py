import numpy as np
from fractions import gcd

def main():
    N = 1000
    count = {}
    prim_tri = genPrimitiveTriples(N)
    for x in prim_tri:
        p = sum(x)
        count[p] = count[p] + 1 if p in count else 1

        n = 2
        while p*n < N:
            count[p*n] = count[p*n] + 1 if p*n in count else 1
            n += 1
    
    m = 0
    for key in count:
        if count[key] > m:
            m = count[key]
            max_p = key
    print max_p
            



def genPrimitiveTriples(P):
    """Generate Pythagorean primitive triples using Euclid's formula:
        * a = m^2 - n^2
        * b = 2mn
        * c = m^2 + n^2
      Parameters
      ----------
      C: int
         Maximum of of longest side
      
      Returns
      -------
      triples: list of tuples (int, int, int)
        All Pythagorean primitive triples
    """
    triples = []
    M = int(np.sqrt(P)/2) + 1 
    for m in xrange(2,M+1):
        for n in xrange(1,m):
            if gcd(m,n)==1 and (m-n)%2 and 2*m*(m+n) <= P:
                triples.append((m*m-n*n, 2*m*n, m*m+n*n))
    return triples




if __name__ == "__main__":
    main()
