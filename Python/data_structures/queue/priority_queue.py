"""Priority Queue represented by a python list"""
class PriorityQueue():
	"""A Priority Queue is an abstract dat type which is like a regular queue or
	stack data structure, but where additionally each element has a "priority"
	associated with it. In a priority queue, an element with high priority is served
	before an element with low priority.

	https://en.wikipedia.org/wiki/Priority_queue
	"""
	
	#Initialize constructor
	def __init__(self):
		self.queue = []
		self.length = 0
		self.front = 0

	#Output string
	def __str__(self):
		printed = '<' + str(self.queue)[self.front:self.front+self.length-1] + '>'
		return printed

	"""Enqueues {@code item}
	@param item
		item to enqueue
		regarding of order"""
	def put(self, item):
		for i in range(self.front, self.front+self.length):
			if(item > self.queue[i]):
				self.insert(i, item)
		self.length = self.length + 1
		return 1

	"""Dequeues {@code item}
	@return dequeued
		item that was dequeued"""
	def get(self):
		self.length = self.length - 1
		dequeued = self.queue[self.front]
		self.front += 1
		self.queue = self.queue[self.front:]
		return dequeued
	
	"""Returns item at from of self.queue"""
	def front(self):
		return self.queue[self.front]
	
	"""Returns the length of self.queue"""
	def size(self):
		return self.length
