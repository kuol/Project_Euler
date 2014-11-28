def main():
    # Read in number, make it into a list of size 1000
    with open("number.txt", 'r') as f:
        a = f.readlines()

    a = [x.strip() for x in a]
    b = []
    for x in a:
        b += list(x)
    b = [int(x) for x in b]
    
    print multiple13(b)

def multiple13(b):
    mul = 0
    for i in xrange(12,1000):
        temp = 1
        for j in xrange(i-12,i+1):
            temp *= b[j]
        mul = temp if temp > mul else mul
    return mul

if __name__ == '__main__':
    main()



