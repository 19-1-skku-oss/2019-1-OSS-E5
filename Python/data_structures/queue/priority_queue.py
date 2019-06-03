class PriorityQueue():
	def __init__(self):
		self.queue = []
		self.length = 0
		self.front = 0

	def __str__(self):
		printed = '<' + str(self.stack)[1:-1] + '>'
		return printed

	def put(self, item):
		for i in range(self.length):
			if(item > self.queue[i]):
				self.insert(i, item)
		self.length = self.length + 1

	def get(self):
		self.length = self.length - 1
		dequeued = self.queue[self.front]
		self.front += 1
		self.queue = self.queue[self.front:]
		return dequeued

	def front(self):
		return self.queue[0]
	
	def size(self):
		return self.length
