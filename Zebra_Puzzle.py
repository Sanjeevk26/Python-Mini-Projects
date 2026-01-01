from itertools import permutations


# ============================================================
# ZEBRA PUZZLE (EINSTEIN'S RIDDLE)
#
# There are five houses in a row, each painted a different color.
# In each house lives a person of a different nationality.
# Each person drinks a different beverage, smokes a different brand
# of cigarettes, and owns a different pet.
#
# GIVEN THE FOLLOWING CLUES:
#
#  1. The Englishman lives in the red house.
#  2. The Spaniard owns the dog.
#  3. Coffee is drunk in the green house.
#  4. The Ukrainian drinks tea.
#  5. The green house is immediately to the right of the ivory house.
#  6. The Old Gold smoker owns snails.
#  7. Kools are smoked in the yellow house.
#  8. Milk is drunk in the middle house.
#  9. The Norwegian lives in the first house.
# 10. The man who smokes Chesterfields lives next to the man with the fox.
# 11. Kools are smoked in the house next to the house where the horse is kept.
# 12. The Lucky Strike smoker drinks orange juice.
# 13. The Japanese smokes Parliaments.
# 14. The Norwegian lives next to the blue house.
#
# QUESTION:
#   Who drinks water?
#   Who owns the zebra?
#
# ============================================================


def immright(h1, h2):
    """
    Return True if house h1 is immediately to the right of house h2.
    Example: h1 = 3, h2 = 2 → True
    """
    return h1 - h2 == 1


def nextto(h1, h2):
    """
    Return True if two houses are adjacent (next to each other),
    regardless of order.
    """
    return h2 - h1 == 1 or h1 - h2 == 1


def zebra_puzzle():
    """
    Solve the Zebra Puzzle using brute-force search with constraints.

    Returns:
        [house_that_drinks_water, house_that_owns_zebra]
    """

    # House positions numbered 1 through 5 (left to right)
    houses = [First, _, Middle, _, _] = [1, 2, 3, 4, 5]

    # Generate all possible permutations of house positions.
    # Each permutation assigns one attribute value to one house.
    orderings = list(permutations(houses))

    # Search for the first arrangement that satisfies all clues
    return next([Water, Zebra]

        # ----------------------------------------------------
        # Nationalities
        # ----------------------------------------------------
        for (English, Spaniard, Ukranian, Norwegian, Japanese) in orderings
        if Norwegian is First                 # Clue 9

        # ----------------------------------------------------
        # House colors
        # ----------------------------------------------------
        for (Red, Green, Ivory, Yellow, Blue) in orderings
        if English is Red                     # Clue 1
        if nextto(Norwegian, Blue)            # Clue 14
        if immright(Green, Ivory)             # Clue 5

        # ----------------------------------------------------
        # Drinks
        # ----------------------------------------------------
        for (Milk, Oj, Tea, Coffee, Water) in orderings
        if Coffee is Green                    # Clue 3
        if Ukranian is Tea                    # Clue 4
        if Milk is Middle                     # Clue 8

        # ----------------------------------------------------
        # Pets
        # ----------------------------------------------------
        for (Dog, Zebra, Snails, Horse, Fox) in orderings
        if Spaniard is Dog                    # Clue 2

        # ----------------------------------------------------
        # Cigarettes
        # ----------------------------------------------------
        for (OldGold, Kools, Chesterfield, LucyStrike, Parliaments) in orderings
        if OldGold is Snails                  # Clue 6
        if Kools is Yellow                    # Clue 7
        if nextto(Chesterfield, Fox)          # Clue 10
        if nextto(Kools, Horse)               # Clue 11
        if LucyStrike is Oj                   # Clue 12
        if Japanese is Parliaments            # Clue 13
    )


print(zebra_puzzle())
