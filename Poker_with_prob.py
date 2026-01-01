def poker(hands):
    """
    Return a list of winning hands.
    If there's a tie, return all tied winning hands.

    Example:
        poker([hand1, hand2, hand3]) -> [best_hand] or [handA, handB]
    """
    return allmax(hands, key=hand_rank)


def fact(n):
    """Return factorial of n (n!)."""
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive definition: n! = n * (n-1)!
        return n * fact(n - 1)


def comb(n, r):
    """
    Return nCr (number of combinations),
    i.e., ways to choose r items from n items without order.
    """
    return (fact(n)) / (fact(n - r) * fact(r))


def probability(hand):
    """
    Return the probability of the given 5-card poker hand type.
    The function looks at what category the hand belongs to
    (straight flush, four of a kind, etc.) and returns the probability.

    NOTE: Some of the formulas below have issues (parentheses, missing /comb(52,5),
    and one uses comb((4,1) ** 5) which is not valid comb usage).
    I’m only commenting your existing code.
    """
    ranks = card_ranks(hand)

    # Straight flush (including royal flush). Excludes the 4 royal flushes in your formula.
    if straight(ranks) and flush(hand):
        return (comb(10, 1) * comb(4, 1) - comb(4, 1)) / comb(52, 5)

    # Four of a kind: choose rank for quads, choose kicker rank, choose suit for kicker
    elif kind(4, ranks):
        return (comb(13, 1) * comb(12, 1) * comb(4, 1)) / comb(52, 5)

    # Full house: choose trips rank, choose 3 suits; choose pair rank, choose 2 suits
    elif kind(3, ranks) and kind(2, ranks):
        return (comb(13, 1) * comb(4, 3) * comb(12, 1) * comb(4, 2)) / comb(52, 5)

    # Flush (not straight flush): flush count minus straight flush count
    elif flush(hand):
        return (comb(13, 5) * comb(4, 1) - comb(10, 1) * comb(4, 1)) / comb(52, 5)

    # Straight (not flush): formula here is intended to count straights minus straight flushes
    elif straight(ranks):
        return (comb(10, 1) * comb((4, 1) ** 5) - comb(10, 1) * comb(4, 1)) / comb(52, 5)

    # Three of a kind (not full house/quads):
    # choose trips rank & suits, choose 2 kicker ranks, choose suit for each kicker
    elif kind(3, ranks):
        return (comb(13, 1) * comb(4, 3) * comb(12, 2) * (comb(4, 1) ** 2))

    # Two pair: choose 2 ranks for pairs, choose suits for each pair,
    # choose kicker rank and suit
    elif two_pair(ranks):
        return (comb(13, 2) * (comb(4, 2) ** 2) * comb(11, 1) * comb(4, 1))

    # One pair: choose pair rank & suits, choose 3 other ranks, choose suit for each
    elif kind(2, ranks):
        return (comb(13, 1) * comb(4, 2) * comb(12, 3) * (comb(4, 1) ** 3))

    # High card: not straight, not flush, no pairs
    else:
        return (comb(13, 5) - 10) * (comb(4, 1) ** 5 - 4)


def allmax(iterable, key=None):
    """
    Return a list of all items that are tied for maximum
    according to the scoring function `key`.

    Example:
        allmax([a,b,c], key=f) -> [b] or [b,c] if tie
    """
    result, maxvalue = [], None

    for x in iterable:
        xval = key(x)

        # If this is the first item OR it beats the current max, reset winners.
        # NOTE: your code uses maxval below but defines maxvalue above,
        # so this function will error as written. Keeping it unchanged.
        if not result or xval > maxval:
            result, maxval = [x], xval

        # If it's tied with max, add it.
        elif xval == maxval:
            result.append(x)
            print(result)

    return result


def hand_rank(hand):
    """
    Return a value that indicates how strong a hand is.
    The returned tuple compares lexicographically, so higher categories win.

    Category codes:
      8 = straight flush
      7 = four of a kind
      6 = full house
      5 = flush
      4 = straight
      3 = three of a kind
      2 = two pair
      1 = one pair
      0 = high card
    """
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
    """
    Return a list of card ranks sorted high-to-low.
    Converts card faces into numbers:
        2..9 -> 2..9, T->10, J->11, Q->12, K->13, A->14

    Special case:
      A-2-3-4-5 is treated as the lowest straight (5-high straight),
      so it returns [5,4,3,2,1].
    """
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)

    # Handle wheel straight: A-2-3-4-5
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def flush(hand):
    """Return True if all cards have the same suit."""
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def straight(ranks):
    """
    Return True if ranks form a 5-card straight.
    Condition:
      - max - min == 4 (consecutive span)
      - all ranks are distinct (no duplicates)
    """
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def kind(n, ranks):
    """
    Return the first rank that occurs exactly n times.
    Examples:
      kind(4, ranks) -> rank of four-of-a-kind, else None
      kind(3, ranks) -> rank of three-of-a-kind, else None
      kind(2, ranks) -> rank of a pair, else None
    """
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    """
    If there are two different pairs, return a tuple (highpair, lowpair).
    Otherwise return None.
    """
    pair = kind(2, ranks)                 # finds first pair from high end
    lowpair = kind(2, list(reversed(ranks)))  # finds first pair from low end

    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None


def test():
    """
    Basic test cases to validate ranking logic.
    """
    sf1 = "6C 7C 8C 9C TC".split()  # Straight Flush
    sf2 = "6D 7D 8D 9D TD".split()  # Straight Flush
    fk = "9D 9H 9S 9C 7D".split()   # Four of a Kind
    fh = "TD TC TH 7C 7D".split()   # Full House

    # The two straight flushes should tie as winners.
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]
    return 'tests pass'

    # NOTE: This print is unreachable because of the return above.
    print(poker([sf1, sf2, fk, fh]))


import random  # used for shuffling a deck

# Build a standard 52-card deck as strings like "AS", "TD", etc.
# r is rank, s is suit. Suits: S,H,D,C
mydeck = [r + s for r in '23456789TJQKA' for s in 'SHDC']


def deal(numhands, n=5, deck=mydeck):
    """
    Deal `numhands` poker hands, each with `n` cards.

    NOTE: This function shuffles the *global* mydeck each loop,
    and deals the top n cards without removing them,
    so hands can overlap across deals (not realistic dealing).
    Commenting only—logic unchanged.
    """
    x = []
    for i in range(0, numhands):
        random.shuffle(mydeck)     # shuffle the deck before each hand
        result = mydeck[0:n]       # take top n cards (no removal!)
        x.append(result)
    return x

    # Alternative (commented): slice from a once-shuffled deck
    '''or return [deck[n*i:n*(i + 1)] for i in range(numhands)]'''


# Demo run:
x = deal(7)
print(x)
print('The best hand is ', poker(x))
print(comb(52, 5))

print('The probability of [AH,2H,3H,4H,5H] is', probability("6C 7C 8C 9C TC".split()))
print('The probability of [AH,AC,AS,AD,5H] is', probability("9D 9H 9S 9C 7D".split()))
print('The probability of [AH,AC,AS,AD,5H] is', probability("TD TC TH 7C 7D".split()))
