def table (*size):
	size = int(raw_input("Enter a size of a multiplication table (from 3 to 12): "))
	i = 1
	while i <= int(size) :
		tmp1 = []
		tmp2 = ''
		tmp1 = [i*x for x in xrange(1, size+1)]
		width = size**2
		for a in tmp1 :
			tmp2 +=(' ' + str(a).rjust(len(str(width))))
		print (tmp2 + '\n')
		i += 1
table()