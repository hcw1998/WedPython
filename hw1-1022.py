# coding: utf-8
class Card:
    SUITS = ["♠", "♥", "♣","♦"]
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    def __init__(self, s ,r):
        self.suit = s
        self.rank = r
        
    def __repr__(self):
        thecard = self.SUITS[self.suit] + self.RANKS[self.rank]
        return thecard
pip_p1 = input("0-12>>")
suit_p1 = input("0-3>>")
pip_p2 = input("0-12>>")
suit_p2 = input("0-3>>")
if(pip_p1 > pip_p2):
    p = pip_p1
    s = suit_p1
elif(pip_p1 < pip_p2):
    p = pip_p2
    s = suit_p2
elif(pip_p1 == pip_p2):
    if(suit_p1 < suit_p2):
        p = pip_p1
        s = suit_p1
    else:
        p = pip_p2
        s = suit_p2
p = int(p)
s = int(s)
card_bigger = Card(s,p)
card_bigger
