def main():
    a = []
    for n in xrange(1,10000):
        candidate = []
        length = 0
        i = 1
        while length < 9:
            temp = list(str(n*i))
            candidate += [int(x) for x in temp]
            length = len(candidate)
            if length == 9:
                t = sorted(candidate)
                if t == range(1,10):
                    a.append(get_number(candidate))
                break
            i += 1
    print max(a)


def get_number(li):
    n = len(li)
    N = 0 
    for i in xrange(n):
        N += li[i]*10**(n-1-i)
    return N


if __name__ == '__main__':
    main()
