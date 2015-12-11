__author__ = 'Schkred'
def divisibles(quantity, x, y) :
	divbyx = []
	divbyy = []
	i = 1
	while len(divbyx) < quantity :
		if i%y == 0 :
			pass
		elif i%x == 0 :
			divbyx.append(i)
		i += 1
	i = 1
	while len(divbyy) < quantity :
		if i%x == 0 :
			pass
		elif i%y == 0 :
			divbyy.append(i)
		i += 1
	print("Found " + str(quantity) + " elements divisible by " + str(x) + " and " + str(y) + " but not both.")
	print divbyx
	print divbyy

divisibles(10, 3, 5)