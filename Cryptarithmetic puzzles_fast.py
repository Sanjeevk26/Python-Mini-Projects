import re,itertools,string

def faster_solve(formula):
	f, letters = compile_formula(formula)
	for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
		try:
			if f(*digits) is True:
				table = bytes.maketrans(letters.encode(), ''.join(map(str, digits)).encode())
				return(formula.translate(table))
		except ArithmeticError:
			pass
def compile_formula(formula, verbose=False):
        letters = ''.join(set(re.findall('[A-Z]',formula)))
        print(letters)
        parms = ', '.join(letters)
        print(parms)
        print(re.split('([A-Z]+)', formula))
        tokens = map(compile_word, re.split('([A-Z]+)', formula))
        #print(list(tokens))
        body = ''.join(tokens)
        print(body)
        f = 'lambda %s : %s' %(parms, body)
        if verbose : print(f)
        return eval(f),letters
def compile_word(word):
	if word.isupper():
		terms = [('%s*%s' % (10**i, d))
                            for (i, d) in enumerate(word[::-1])]
		return '(' + '+'.join(terms) + ')'
	else:
		return word
print(faster_solve("SEND + MORE == MONEY")) #9567 + 1085 == 10652
print(faster_solve("ODD + ODD == EVEN"))#655 + 655 == 1310
print(faster_solve("DONALD + GERALD == ROBERT"))#526485 + 197485 == 723970
print(faster_solve("EAT + THAT == APPLE"))#819 + 9219 == 10038
print(faster_solve("BASE + BALL == GAMES"))#7483 + 7455 == 14938
print(faster_solve("CROSS + ROADS == DENGER"))#76833 + 68213 == 145046
print(faster_solve("BEST + MADE == MASER"))#9567 + 1085 == 10652
print(faster_solve("BASE + BALL == GAMES"))#7483 + 7455 == 14938

