
def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)


def fact(n):
    '''Returns factorial of a number'''
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
    
def comb(n,r):
    '''Useful for finding combination i.e. nCr'''
    return (fact(n)) / (fact(n - r) * fact(r))

def probability(hand):
    '''Returns the probability of the hand'''
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (comb(10,1) * comb(4,1) - comb(4,1)) / comb(52,5)
    elif kind(4, ranks):
        return (comb(13,1) * comb(12,1) * comb(4,1)) / comb(52,5)
    elif kind(3, ranks) and kind(2, ranks):
        return (comb(13,1) * comb(4,3) * comb(12,1) * comb(4,2)) / comb(52,5)
    elif flush(hand):
        return(comb(13,5)*comb(4,1) - comb(10,1)*comb(4,1)) / comb(52,5)
    elif straight(ranks):
        return (comb(10,1) * comb((4,1) ** 5) - comb(10,1) * comb(4,1)) / comb(52,5)
    elif kind(3, ranks):
        return (comb(13,1) * comb(4,3) * comb(12,2) * (comb(4,1) ** 2))
    elif two_pair(ranks):
        return (comb(13,2) * (comb(4,2) ** 2) * comb(11,1) * comb(4,1))
    elif kind(2, ranks):
        return (comb(13,1) * comb(4,2) * comb(12,3) * (comb(4,1) ** 3))
    else:
        return (comb(13,5) - 10) * (comb(4,1) ** 5 - 4)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    result,maxvalue = [],None
    #key = key or (lambda x : x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result,maxval = [x],xval
        elif xval == maxval:
            result.append(x)   
            print(result)
    return result
    

def hand_rank(hand):
    '''Return a value indicating the ranking of a hand.'''
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def card_ranks(hand):
    '''Return a list of the ranks, sorted with higher first.'''
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    '''Return True if all the cards have the same suit.'''
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    '''Return True if the ordered ranks form a 5-card straight.'''
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has exactly n-of-a-kind of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    "If there are two pair here, return the two ranks of the two pairs, else None."
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

def test():
    '''Test cases for the functions in poker program.'''
    sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
    sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2] 
    return 'tests pass'
    print(poker([sf1, sf2, fk, fh]))
import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. 
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    x = []
    for i in range(0,numhands):
        random.shuffle(mydeck)
        result = mydeck[0:n]
        x.append(result)
    return x
    '''or return [deck[n*i:n*(i + 1)] for i in range(numhands)]'''
x = deal(7)
print(x)
print('The best hand is ',poker(x))
print(comb(52,5))
print('The probability of [AH,2H,3H,4H,5H] is',probability("6C 7C 8C 9C TC".split()))
print('The probability of [AH,AC,AS,AD,5H] is',probability("9D 9H 9S 9C 7D".split()))
print('The probability of [AH,AC,AS,AD,5H] is',probability("TD TC TH 7C 7D".split()))
