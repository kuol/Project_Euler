from math import factorial

def main():
    x = test_curious(2,if_curious,range(6),[5])

    a = [factorial(i) for i in xrange(10)]
    result = []
    for d in xrange(3,8):
        upper = 10**(d)
        lower = 10**(d-1)
        
        # Find largest possible digit: a[k]
        k_max = 0
        while a[k_max + 1] < upper:
            k_max += 1
            if k_max == 9:
                break
        
        # Find smallest possible digit that has to be there
        k_min = k_max
        while a[k_min - 1]*d > lower:
            k_min -= 1
            if k_min == 0:
                break

        for k in xrange(k_max, k_min-1, -1):
            most = upper/a[k]
            least = lower/a[k] + 1 if lower%a[k] else lower/a[k]
            if most >= d:
                result.append(test_curious(d-least, if_curious, range(k+1), [k]*least))
            else:
                for j in xrange(most,least-1,-1):
                    result.append(test_curious(d-j, if_curious, range(k), [k]*j))
   #print result

def test_curious(n,f,candidates,choosen,items=()):
    if n > 0:
        for x in candidates:
            test_curious(n-1,f,candidates,choosen,items+(x,))
    else:
        return f(list(items) + choosen)

def if_curious(a):
    fact = [factorial(i) for i in xrange(10)]
    n = 0  
    for x in a:
        n += fact[x]
    m = list(str(n))
    m = [int(x) for x in m]
    f = lambda x: x in a
    
    a.sort()
    m.sort()
    if a == m:
        print n
        #return n
    

if __name__ == '__main__':
    main()



