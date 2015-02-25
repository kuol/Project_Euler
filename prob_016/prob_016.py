"""
2**1000 = 1024**100 = (10**3 + 24)**100
"""
def main():
    print power(9)

def power(N):
    a = [1,0,2,4]
    for i in xrange(N):
        # 24*(1024**i)
        b = [0]*2 + [24*x for x in a]
        for j in xrange(len(b)-1,0,-1):
            if b[j]/10:
                b[j-1] += b[j]/10
                b[j] = b[j]%10
#        for j in xrange(2,len(b)):
#            h = b[j]/100
#            t = b[j]%100/10
#            o = b[j]%10
#            b[j-2] += h
#            b[j-1] += t
#            b[j] = o
#            
#            for k in xrange(1,j-2):
#                if b[j-k]/10:
#                    b[j-k-1] += 1
#                    b[j-k] = b[j-k]%10
            
        a = [0] + a + [0]*3 # 1000*(1024**i)

        for j in xrange(len(a)-1,0,-1):
            a[j] += b[j-2]
            if a[j]/10:
                a[j-1] += a[j]/10
                a[j] = a[j]%10
    return a

if __name__ == '__main__':
    main()
