import re
import itertools
import string

def faster_solve(formula):
    """
    Solve an alphametic puzzle such as:
        SEND + MORE == MONEY

    Each letter represents a unique digit (0–9).
    The function returns the formula with letters replaced by digits
    if a valid solution is found.
    """

    # Compile the formula into a callable lambda function
    # and extract the unique letters used in the formula
    f, letters = compile_formula(formula)

    # Try every permutation of digits (0–9) of the required length
    # Each permutation represents a possible digit assignment
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            # Call the compiled lambda with the current digit assignment
            # If the equation evaluates to True, we found a solution
            if f(*digits) is True:
                # Create a translation table mapping letters -> digits
                table = bytes.maketrans(
                    letters.encode(),
                    ''.join(map(str, digits)).encode()
                )

                # Replace letters in the original formula with digits
                return formula.translate(table)

        # Ignore invalid math operations (e.g., division by zero)
        except ArithmeticError:
            pass


def compile_formula(formula, verbose=False):
    """
    Convert the string formula into a lambda function that can be evaluated.

    Example:
        "SEND + MORE == MONEY"
    becomes something like:
        lambda S,E,N,D,M,O,R,Y: (1000*S + 100*E + 10*N + D) + ...
    """

    # Extract all unique capital letters used in the formula
    letters = ''.join(set(re.findall('[A-Z]', formula)))

    # Create a comma-separated parameter list for the lambda
    parms = ', '.join(letters)

    # Split the formula into tokens of:
    #   - uppercase words (SEND, MORE, etc.)
    #   - everything else (+, ==, spaces)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))

    # Reassemble the transformed tokens into a valid Python expression
    body = ''.join(tokens)

    # Build the lambda expression as a string
    f = 'lambda %s : %s' % (parms, body)

    # Optionally print the generated lambda for debugging
    if verbose:
        print(f)

    # Evaluate the lambda string into an actual function
    return eval(f), letters


def compile_word(word):
    """
    Convert an uppercase word (e.g. SEND) into a numeric expression.

    Example:
        SEND -> (1000*S + 100*E + 10*N + D)

    Non-uppercase tokens are returned unchanged.
    """

    # Only transform words made entirely of capital letters
    if word.isupper():
        # Create terms for each letter based on its place value
        terms = [
            '%s*%s' % (10**i, d)
            for (i, d) in enumerate(word[::-1])
        ]

        # Join the terms into a single numeric expression
        return '(' + '+'.join(terms) + ')'
    else:
        # Leave operators, spaces, and punctuation unchanged
        return word


# Example test cases
print(faster_solve("SEND + MORE == MONEY"))    # 9567 + 1085 == 10652
print(faster_solve("ODD + ODD == EVEN"))       # 655 + 655 == 1310
print(faster_solve("DONALD + GERALD == ROBERT"))  # 526485 + 197485 == 723970
print(faster_solve("EAT + THAT == APPLE"))     # 819 + 9219 == 10038
print(faster_solve("BASE + BALL == GAMES"))    # 7483 + 7455 == 14938
print(faster_solve("CROSS + ROADS == DENGER")) # 76833 + 68213 == 145046
print(faster_solve("BEST + MADE == MASER"))    # 9567 + 1085 == 10652
