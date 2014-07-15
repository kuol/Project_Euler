import unittest
from prob_054 import *

# Flush
h1 = ['3H', '5H', '9H', '2H', 'JH']
s1 = [5,0,0,11,9,5,3,2]

# Straight
h2 = ['8S', '6D', '9S', '5H', '7C']
s2 = [4,0,0,9,8,7,6,5]

# Straight Flush
h3 = ['8S', 'TS', 'JS', '9S', 'QS']
s3 = [8,0,0,12,11,10,9,8]

# Royal Flush
h4 = ['KD', 'JD', 'QD', 'AD', 'TD']
s4 = [9,0,0,14,13,12,11,10]

# Four of a Kind
h5 = ['5S', '5C', '5D', '8S', '5H']
s5 = [7,5,0,8,5,5,5,5]

# Full House
h6 = ['TD', '6S', 'TH', 'TS', '6H']
s6 = [6,10,6,10,10,10,6,6]

# Three of a Kind
h7 = ['JH', '8D', 'JS', 'JC', 'AD']
s7 = [3,11,0,14,11,11,11,8]

# Two pairs
h8 = ['KD', 'TS', '2C', 'TD', '2H']
s8 = [2,10,2,13,10,10,2,2]

# One pair
h9 = ['AS', '8C', '9D', '6H', 'AC']
s9 = [1,14,0,14,14,9,8,6]

# High card
h10 = ['KS', 'JD', '2H', '5C', '7C']
s10 = [0,0,0,13,11,7,5,2]

#print TexasHoldem(h10)
print p1Wins(s1,s2)

class InequalityTest(unittest.TestCase):

    def testFlush(self):
        self.failUnlessEqual(TexasHoldem(h1), s1)

    def testStraight(self):
        self.failUnlessEqual(TexasHoldem(h2), s2)

    def testStraightFlush(self):
        self.failUnlessEqual(TexasHoldem(h3), s3)

    def testRoyalFlush(self):
        self.failUnlessEqual(TexasHoldem(h4), s4)

    def testFourOfAKind(self):
        self.failUnlessEqual(TexasHoldem(h5), s5)

    def testFullHouse(self):
        self.failUnlessEqual(TexasHoldem(h6), s6)

    def testThreeOfAKind(self):
        self.failUnlessEqual(TexasHoldem(h7), s7)

    def testTwoPairs(self):
        self.failUnlessEqual(TexasHoldem(h8), s8)

    def testOnePair(self):
        self.failUnlessEqual(TexasHoldem(h9), s9)

    def testHighCard(self):
        self.failUnlessEqual(TexasHoldem(h10), s10)

    def testP1Wins(self):
        self.assertTrue(p1Wins(s1,s2))


if __name__=='__main__':
    unittest.main()
