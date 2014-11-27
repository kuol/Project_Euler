def main():
    with open('p089_roman.txt') as f:
        raw = f.readlines()
    lines = [x.strip() for x in raw]
    arabic = map(readRoman, lines)
    efficient_roman = map(writeRoman, arabic)
    
#    n = len(lines)
#    with open('results.txt', 'a') as f:
#        for i in xrange(n):
#            f.write("%s %s %s\n" %(lines[i], arabic[i], efficient_roman[i]))
    old = sum([len(x) for x in lines])
    new = sum([len(x) for x in efficient_roman])
    print old - new

def readRoman(roman):
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    r = list(roman)
    n = len(r)
    arabic = 0

    i = 0
    while i < n-1: # loop up to the second to the last element
        if r[i] is 'I' and r[i+1] is 'V':
            number = 4
            i += 2
        elif r[i] is 'I' and r[i+1] is 'X':
            number = 9
            i += 2
        elif r[i] is 'X' and r[i+1] is 'L':
            number = 40
            i += 2
        elif r[i] is 'X' and r[i+1] is 'C':
            number = 90
            i += 2
        elif r[i] is 'C' and r[i+1] is 'D':
            number = 400
            i += 2
        elif r[i] is 'C' and r[i+1] is 'M':
            number = 900
            i += 2
        else:
            number = d[r[i]]
            i += 1
        arabic += number

    if i == n-1: # The last two Roman numerals don't form a subtractive pair
        arabic += d[r[i]]

    return arabic

def writeRoman(arabic):
    helper = {'M':0, 'D':0, 'C':0, 'L':0, 'X':0, 'V':0, 'I':0,
            'IV':0, 'IX':0, 'XL':0, 'XC':0, 'CD':0, 'CM':0}
    d = [('M',1000), ('D',500), ('C',100), ('L',50), ('X',10), ('V',5), ('I',1)]
    # Without subtractive pairs
    for r,n in d:
        helper[r] = arabic/n
        arabic %= n
    # Add subtractive pairs when possible
    if helper['C'] == 4:
        if helper['D'] == 1:
            helper['CM'] = 1
        else:
            helper['CD'] = 1
        helper['C'], helper['D'] = 0,0
    
    if helper['X'] == 4:
        if helper['L'] == 1:
            helper['XC'] = 1
        else:
            helper['XL'] = 1
        helper['X'], helper['L'] = 0,0

    if helper['I'] == 4:
        if helper['V'] == 1:
            helper['IX'] = 1
        else:
            helper['IV'] = 1
        helper['I'], helper['V'] = 0,0

#    print helper
    roman = 'M'*helper['M'] + 'CM'*helper['CM'] + 'D'*helper['D'] + 'CD'*helper['CD'] + 'C'*helper['C'] + 'XC'*helper['XC'] + 'L'*helper['L'] + 'XL'*helper['XL'] + 'X'*helper['X'] + 'IX'*helper['IX'] + 'V'*helper['V'] + 'IV'*helper['IV'] + 'I'*helper['I']
    return roman


if __name__ == '__main__':
    main()





