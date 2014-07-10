#!/home/kuol/anaconda/bin/python
from pylab import *


def main():
    nT,nP,nH = 285.0,165.0,143.0
    #Error tolerance
    eTH = abs(nT/nH - 2.0)
    eTP = abs(nT/nP - sqrt(3))

    flag = True
    while (flag):
        nT = nT + 1
        nP, nH = nT/sqrt(3), nT/2.0
        nP1, nP2 = floor(nP), ceil(nP)
        nH1, nH2 = floor(nH), ceil(nH)

        T = Tri(nT)
        if (Pen(nP1) == T or Pen(nP2) == T) and (Hex(nH1) == T or Hex(nH2) == T):
            flag = False                 
    nP = nP1 if Pen(nP1) == T else nP2
    nH = nH1 if Hex(nH1) == T else nH2

    print "nT = %d, nP = %d, nH = %d" %(nT, nP, nH)
    print "The nex triangle number Tn is: %d" %Tri(nT)
            


def Tri(n):
    return n*(n+1)/2.0

def Pen(n):
    return n*(3*n-1)/2.0

def Hex(n):
    return n*(2*n-1)



if __name__ == '__main__':
    main()
