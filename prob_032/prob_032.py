"""Notice that the only possilbe multiplicand-multiplier 
combinations (in terms of number digits) are:
    1 4 4
    2 3 4
"""
def main():
    a = []
    for i in xrange(1,10):
        for j in xrange(1234,9877):
            if i*j > 9999:
                break
            elif check_pandigital(i,j):
                a.append(i*j)

    for i in xrange(12,99):
        for j in xrange(123,988):
            if i*j > 9999:
                break
            elif check_pandigital(i,j):
                a.append(i*j)

    print sum(set(a))

def check_pandigital(i,j):
    t = list(str(i)) + list(str(j)) + list(str(i*j))
    t = [int(x) for x in t]
    if sorted(t) == range(1,10):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
