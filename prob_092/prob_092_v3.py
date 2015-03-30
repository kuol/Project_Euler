
def main():
#    N = 10000
    N = 10000000
    # a: records what number the chain will end up with
    # 0: the chain ends up with 1
    # 1: the chain ends up with 89
    # 2: to be determined
    a = [2]*N
    a[1] = 0
    a[89] = 1
   
    for n in xrange(1,N):
        if a[n] != 2:
            continue
        else:
            digits = get_digits(n) 
            all_perm = []
            perm(list(digits),0,all_perm)
            temp = list(all_perm)
            s = sum([x*x for x in digits])
            while a[s] ==2 and s != 1 and s != 89:
                if s < N and a[s] != 2:
                    a[n] = a[s]
                    break
                digits = get_digits(s) 
                all_perm = []
                perm(list(digits),0,all_perm)
                temp = temp + list(all_perm)
                s = sum([x*x for x in digits])
            
            if a[s]==0 or s == 1:
                for t in temp:
                    if t < N:
                        a[t] = 0
            elif a[s]==1 or s == 89:
                for t in temp:
                    if t < N:
                        a[t] = 1

    print sum(a[1:])
#    for n in xrange(N):
#        print "%d: %d" %(n, a[n])

def perm(digits, k, result):
    n = len(digits)
    if k == n-1:
        aa = list(digits)
        bb = int(''.join([str(x) for x in aa]))
        result.append(bb) # list(digits) makes a copy of digits
    else:
        for i in xrange(k,n):
            digits[k], digits[i] = digits[i], digits[k]
            perm(digits, k+1, result)
            digits[k], digits[i] = digits[i], digits[k]



def get_digits(n):
    return [int(x) for x in list(str(n))]


if __name__ == "__main__":
    main()
