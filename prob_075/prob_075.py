import numpy as np
from fractions import gcd

def main():
    L = 1500000
    primTri = genPrimitiveTriples(L)
    print len(primTri)


def genPrimitiveTriples(L):
    """Generate Pythagorean primitive triples using Euclid's formula:
        * a = m^2 - n^2
        * b = 2mn
        * c = m^2 + n^2
      Parameters
      ----------
      L: int
         Maximum of sum of all sides

      Returns
      -------
      triples: list of tuples (int, int, int)
        All Pythagorean primitive triples
    """
    triples = []
    M = int(np.sqrt(L))
    for m in xrange(2,M+1):
        for n in xrange(1,m):
            if gcd(m,n)==1 and (m-n)%2 and 2*m*(m+n) <= L:
                #print("[%d, %d]: (%d, %d, %d)") %(m,n,m*m-n*n, 2*m*n, m*m+n*n)
                triples.append((m*m-n*n, 2*m*n, m*m+n*n))
    return triples




if __name__ == "__main__":
    main()
