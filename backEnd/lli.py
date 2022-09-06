import itertools

print("E => TE' ")
print("E' => +TE' ")
print("E' => -TE' ")
print("E' => @ ")
print("T => FT' ")
print("T' =>*FT' ")
print("T' => /FT' ")
print("T' => @' ")
print("F => (E) ")
print("F => n ")

global E, E1, T, T1, F





def E1():
	x = ["+", "T()"]
	x = ''.join(x)
	# y = "-", T(), "E1"
	return ["@", x, "λ"]

print(E1())

def T():
	# return [F(), T1()]
	return "T()"

def E():
	# return "E()"
	return [T(), E1()]

def T1():
	x = ["*", F(),"T1"]
	y = "/", F(), "T1"
	return ("@", x, y)


def F():
	x = ["(", E(), ")"]
	x = ''.join(x)
	return ["n", x]

print(F())
# 	return [F(), T1()]

# def E1():
# 	x = "+", T(), "E1"
# 	y = "-", T(), "E1"
# 	return ["@", x, y]


# print(E())

'''
[[['n', '(E)'], 
['@', ('*', ['n', '(E)'], 'T1'), ('/', ['n', '(E)'], 'T1')]], 
['@', ('+', [['n', '(E)'], ['@', ('*', ['n', '(E)'], 'T1'), ('/', ['n', '(E)'], 'T1')]], 'E1'), ('-', [['n', '(E)'], 
['@', ('*', ['n', '(E)'], 'T1'), ('/', ['n', '(E)'], 'T1')]], 'E1')]]

'''
