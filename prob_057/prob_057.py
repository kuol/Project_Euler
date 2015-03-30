# Fixed point iteration:
# 1 / (a_{n+1} - 1) = a_n + 1
# Or:
# a_{n+1} = 1 / (a_n + 1) + 1

from fractions import gcd
def main():
    count = 0 
    a = (3,2)
    for n in xrange(1,1000):
        a = iterate(a)
        if num_digits(a[0]) > num_digits(a[1]):
            count += 1
    print count

def num_digits(n):
    count = 1
    while n/10:
        n /= 10
        count += 1
    return count

def iterate(a):
    """ Get next iterate: a_{n+1} = 1 / (a_n + 1) + 1

    Parameters
    ----------
    a : tuple of int of size 2, (int, int)
        Current iterate.

    Returns
    -------
    out : tuple of int of size 2, (int, int)
        Next iterate.
    """
    t = add_rational(a, (1,1))
    t = inv_rational(t)
    return add_rational(t, (1,1))

def add_rational(a,b):
    """ Add two rational numbers a,b.
    
    Parameters
    ----------
    a : tuple of int of size 2, (int, int)
        Summand, a rational number, a[0] numerator, a[1] denominator.
    
    b : tuple of int of size 2, (int, int)
        Another summand, a rational number, b[0] numerator, b[1] denominator.

    Returns
    -------
    out : tuple of int of size 2, (int, int)
        Sum, a rational number, sum[0] is the numerator, sum[1] is the denominator.
    """
    nu = a[0]*b[1] + a[1]*b[0]
    de = a[1]*b[1]
    div = gcd(nu,de)
    return (nu/div, de/div)

def inv_rational(a):
    """ Invert a rational number.
    
    Parameters
    ----------
    a : tuple of int of size 2, (int, int)
        The rational number to be inverted.

    Returns
    -------
    out : tuple of int of size 2, (int, int)
        The inverted rational number.
    """
    return (a[1],a[0])


if __name__ == '__main__':
    main()
