
def main():
#    N = 10000
    N = 10000000
    # a: records what number the chain will end up with
    # 0: the chain ends up with 1
    # 1: the chain ends up with 89
    # 2: to be determined
    k = 567
    a = [2]*(k+1)
    a[1] = 0
    a[89] = 1
   
    for n in xrange(1,k):
        if a[n] != 2:
            continue
        else:
            temp = [n]
            s = digit_sum(n)
            while a[s] ==2 and s != 1 and s != 89:
                if s < k and a[s] != 2:
                    a[n] = a[s]
                    break
                temp.append(s)
                s = digit_sum(s)

            if a[s]==0 or s == 1:
                for t in temp:
                    if t < k:
                        a[t] = 0
            elif a[s]==1 or s == 89:
                for t in temp:
                    if t < k:
                        a[t] = 1

    count = sum(a[1:])
    for n in xrange(k+1, N):
        s = digit_sum(n)
        if a[s] == 1:
            count += 1

    print count

def digit_sum(n):
    digits = [int(x) for x in list(str(n))]
    return sum([x*x for x in digits])


if __name__ == "__main__":
    main()
