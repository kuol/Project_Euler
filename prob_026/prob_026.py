""" Write down how we transform a faction to decimal. For each step, 
if we have a remainder that appeared before, the decimal starts to recur.
"""
def main():
    c = 0
    for n in xrange(2,1000):
        temp = n_cycle(n)
        if temp > c:
            number = n
            c = temp 
    print "The number that gives the longest recurring cycle is: %d" %number
    print "The length of recurring cycle is: %d" %c


def n_cycle(n):
    previous = []
    remainder = 1
    dividend = 10
    while remainder not in previous:
        previous.append(remainder)
        remainder = dividend % n
        if not remainder:
            return 0
        dividend = remainder*10
    return len(previous) - previous.index(remainder)


if __name__ == '__main__':
    main()
