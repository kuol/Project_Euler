def main():
    permutation(range(1,11),5,10)
    #permutation(range(1,7),3,6)
    #print check_gon([6,4,2])

def permutation(li, m, n, start=0):
    """ A recursive algorithm to compute P(n,m)
    """
    if start == m-1:
        for i in xrange(start,n):
            li[i], li[start] = li[start], li[i]
            #print li[:m]
            if check_gon(li[:m]):
                print li[:m]
            li[i], li[start] = li[start], li[i]
    else:
        for i in xrange(start,n):
            li[i], li[start] = li[start], li[i]
            permutation(li, m, n, start+1)
            li[i], li[start] = li[start], li[i]


def check_gon(l):
    ll = l[1:] + [l[0]]
    ll = [x+y for x,y in zip(l,ll)]
    
    # r stores index of ll in the descending order of its elements
    # e.g. ll = [2,4,5,3,1]
    #       r = [2,1,3,0,4]
    n = len(ll)
    
    # r stores the index of items in ll in descending order
    r = [(x,i) for x,i in zip(ll, range(len(ll)))]
    r = sorted(r, key=lambda tup: tup[0], reverse=True)
    r = [x[1] for x in r]

    # Get all arm elements, i.e. element that is not in l
    a = range(1,2*n+1)
    for i in l:
        a[i-1] = 0
    aa = [x for x in a if x!=0]

    # Check if it's a gon
    count = 0
    s = ll[r[0]] + aa[0]
    for i in r:
        if s != ll[i] + aa[count]:
            return False
        count += 1
    return True



if __name__ == '__main__':
    main()
    
    



