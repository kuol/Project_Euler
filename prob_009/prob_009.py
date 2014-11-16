import numpy as np
from fractions import gcd

def main():
    M = 1000
    triples = genPrimitiveTriples(M)
    for x in triples:
        if 1000%sum(x) == 0:
            k = 1000/sum(x)
            print("The product is: %d") %(k*x[0]*k*x[1]*k*x[2])
            #The following "break" is necessary, since the primitive triples are:(15,8,17)
            # sum = 40, thus 40,80... There are many triples, whose sum can divide 1000 
            # evenly
            break
            
def genPrimitiveTriples(C):
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
    M = int(np.sqrt(C-1)) 
    for m in xrange(2,M+1):
        for n in xrange(1,m):
            if gcd(m,n)==1 and (m-n)%2 and m*m+n*n <= C:
                #print("[%d, %d]: (%d, %d, %d)") %(m,n,m*m-n*n, 2*m*n, m*m+n*n)
                triples.append((m*m-n*n, 2*m*n, m*m+n*n))
    return triples




if __name__ == "__main__":
    main()
