class AttrDict(dict) :
	def __init__(self, key, value) :
		self.key = key
		self.value = value
	def __getitem__(self, key) :
		return self.value
	def __setitem__(self, key, value) :
		return 