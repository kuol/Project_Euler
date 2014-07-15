#! /Users/kuol/anaconda/bin/python

import numpy as np
def main():
    poker = np.genfromtxt('poker.txt', delimiter=' ', dtype=str)
    p1 = poker[:,0:5]
    p2 = poker[:,5:]
    del poker
    
    total = 0 
    for i in range(len(p1)):
        if p1Wins(TexasHoldem(p1[i,:]), TexasHoldem(p2[i,:])): 
            total = total + 1
            
    print "Total wins of Player 1 is: %d" %total

def p1Wins(s1, s2):
    for i in range(len(s1)):
        if s1[i] < s2[i]:
            return False
        elif s1[i] > s2[i]:
            return True


def TexasHoldem(hand):
    # ----------------------------------------------------
    # score[0] : rank score, 
    #         9: Royal Flush
    #         8: Straight Flush
    #         7: Four of a Kind
    #         6: Full House
    #         5: Flush
    #         4: Straight
    #         3: Three of a Kind
    #         2: Two Pairs
    #         1: One Pair
    #         0: High Card
    # ----------------------------------------------------
    # score[1:3]: rank cards order
    #             Only need 2 place-holders, since:
    #             9,8,5,4,0: will check all cards if tie
    #             6,2: only two kinds of rank cards
    #             7,3,1: only one kind of rankd cards
    # ----------------------------------------------------
    # score[3:8]:  all cards order
    #-----------------------------------------------------
    score = [0]*8
    
    myDict = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
              '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
              
    temp = ''.join(hand)
    suit = [ temp[i] for i in range(1,10,2) ]
    val =  [ myDict[temp[i]] for i in range(0,10,2) ]
    val.sort(reverse = True)
    # All cards order
    score[3:] = val 
    
    Flush = flush(suit)
    Straight = straight(val)
    
    if Flush:
        if Straight:
            if score[3] == 14:
                score[0] = 9 # Royal Flush
            else:
                score[0] = 8 # Straight Flush
        else:
            score[0] = 5 # Flush
            
    elif Straight:
        score[0] = 4 # Straight
    else:
        score[0:3] = pairTest(val) # return both rank and rank cards order
    
    return score
    
    
def flush(suit):
    flag = True
    for i in range(1,len(suit)):
        if suit[0] != suit[i]:
            flag = False
            break
    return flag
    
def straight(val):
    flag = True
    for i in range(1,len(val)):
        if val[0] != val[i] + i:
            flag = False
            break
    return flag
    
def pairTest(val):
    d = dict(zip(val,map(val.count,val)))
    size = len(d)
    score = [0]*3
    
    if size == 2: # either 'Four of a Kind' or 'Full House'
        if max( sorted(d.values()) ) == 4:
            score[0] = 7 # Four of a Kind
            for k,v in d.items():
                if v == 4:
                    score[1] = k
        else:
            score[0] = 6 # Full House
            score[1:3] = sorted(d.keys(), reverse=True)
            
    if size == 3: # either 'Three of a Kind' or 'Two Pairs'
        if max( sorted(d.values()) ) == 3:
            score[0] = 3 # Three of a Kind
            for k,v in d.items():
                if v == 3:
                    score[1] = k
        else:
            score[0] = 2 # Two pairs
            temp = [0]*2
            i = 0 
            for k,v in d.items():
                if v == 2:
                    temp[i] = k
                    i = i + 1
            score[1:3] = sorted(temp, reverse = True)
            
    if size == 4: # 'One Pair'
        score[0] = 1
        for k,v in d.items():
            if v == 2:
                score[1] = k
                
    return score



if __name__ == '__main__':
    main()













	













