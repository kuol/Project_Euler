# Numeritor: 11 ~ 98
# Denominator: 12 ~99
# Total candidates of two-digit numerators, denominators with value <1:
# 88 + 87 + 1 = 89 * 88 / 2 = 3916
import sys

def main():
    l = []
    for a in xrange(11, 99):
        for b in xrange(a+1, 100):
            if if_curious(a,b):
                l.append(Fraction(a,b))
    out = [str(x) for x in l]
    print out

    frac = reduce(lambda x, y: x*y, l)
    print frac.denominator


def if_curious(a, b):
    if a >= b:
        sys.exit("The numerator should be strictly less than the denominator!")

    a1, a2 = a%10, a/10
    b1, b2 = b%10, b/10

    f = Fraction(a, b)
    # Trivial case
    if a1 == 0 and b1 == 0:
        return False
    elif a1 != b1 and a1 != b2 and a2!=b1 and a2!=b2:
        return False
    
    # Have the same one digit
    if a1 == b1:
        f1 = Fraction(a2, b2)
    elif a1 == b2:
        f1 = Fraction(a2, b1)
    elif a2 == b1:
        f1 = Fraction(a1,b2)
    elif a2 == b2:
        f1 = Fraction(a1, b1)
    return True if f == f1 else False


class Fraction(object):
    def __init__(self, nu = 1, de = 1):
        # Original numerator & denominator
        self.nu = nu
        self.de = de
        # Simplified numerator & denominator
        t = self.gcd()
        self.numerator = self.nu / t
        self.denominator = self.de / t
        

    def gcd(self):
        # Make sure m > n
        m, n = self.de, self.nu
        if m < n:
            m, n = n, m
        if n == 0:
            return m
        while m % n:
            m, n = n, m%n
        return n

    def __str__(self):
        return "%s/%s" % (self.nu, self.de)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

if __name__ == "__main__":
    main()
