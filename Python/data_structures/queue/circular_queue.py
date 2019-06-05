class CircularQueue:

	#Initialize constructor
	def __init__(self):
		self.queue = []
		self.head = 0
		self.tail = 0
		self.max = 20

	#Output string
	def __str__(self):
		printed = '<' + str(self.queue)[self.head:self.tail] + '>'
		return printed
	
	#Current size of queue
	def size(self):
		if self.tail >= self.head:
			return (self.tail - self.head)
		return (self.max - (self.head - self.tail))
		
	#Push element to the queue
	def enqueue(self, data):
		if self.size() == self.max
			return False
		self.queue.insert(self.tail, data)
		self.tail = (self.tail + 1) % self.max
		return True

	#Pop element from the queue
	def dequeue(self):
		if self.size() == 0:
			return false
		data = self.queue[self.head]
		self.head = (self.head + 1) % self.max
		return data

	#Data in head
	def head(self):
		return self.queue[self.head]
	
	#Data in tail
	def tail(self):
		return self.queue[self.tail]
