class AttrDict(object) :
	def __init__(self, key, value) :
		self.key = key
		self.value = value
	def __getitem__(self, key) :
		return self.value
	
x = AttrDict(1, 'One')
print x[1]
