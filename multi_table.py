def table (*size):
	size = raw_input("Enter a size of a multiplication table (from 3 to 12): ")
	i = 1
	while i <= int(size) :
		tmp1 = []
		tmp2 = []
		tmp1 = [i*x for x in xrange(1, int(size)+1)]
		width = int(size)**2
		for a in tmp1 :
			tmp2.append(str(a).rjust(len(str(width))))
		print tmp2
		i += 1
table()

