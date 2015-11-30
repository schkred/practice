def table (*size):
	size = raw_input("Enter a size of a multiplication table (from 3 to 12): ")
	i = 1
	while i <= int(size) :
		tmp = []
		tmp = [i*x for x in xrange(1, int(size))]
		print tmp
		i += 1
table()

