"""Circular Queue represented by a python list"""
class CircularQueue:

	def __init__(self):
		self.queue = []
		self.head = 0
		self.tail = 0
		self.max = 20

	def __str__(self):
		printed = '<' + str(self.queue)[self.head:self.tail] + '>'
		return printed
	
	"""Returns the length of self.queue"""
	def size(self):
		if self.tail >= self.head:
			return (self.tail - self.head)
		return (self.max - (self.head - self.tail))
	
	"""Enqueues {@code item}
	@param item
		item to enqueue"""
	def enqueue(self, item):
		if self.size() == self.max
			return False
		self.queue.insert(self.tail, item)
		self.tail = (self.tail + 1) % self.max
		return True

	"""Dequeues {@code item}
	@requirement: self.sie > 0
	@return dequeued
		item that was dequeued"""
	def dequeue(self):
		if self.size() == 0:
			return false
		data = self.queue[self.head]
		self.head = (self.head + 1) % self.max
		return data

	"""Returns item at head of self.queue"""
	def head(self):
		return self.queue[self.head]
	
	"""Returns item at tail of self.queue"""
	def tail(self):
		return self.queue[self.tail]
