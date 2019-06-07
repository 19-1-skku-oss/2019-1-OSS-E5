class BTreeNode:
	def __init__(self, degree, leaf):
		self.leaf = leaf
		self.keys = []
		self.childs = []
		self.degree = degree

class BTree:
	def __init__(self, degree):
		self.degree = degree - 1
		self.root = BTreeNode(degree, True)
