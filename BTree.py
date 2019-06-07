class BTreeNode(object):
	def __init__(self, degree, leaf):
		self.leaf = leaf
		self.keys = []
		self.childs = []
		self.degree = degree

class BTree(object):
	def __init__(self, degree):
		self.degree = degree - 1
		self.root = BTreeNode(degree, True)

	def traverse(cur_node):
		if len(self.root.keys) != 0:
			for i in range(len(cur_node.keys)):
				if not cur_node.leaf:
					traverse(cur_node.childs[i])
				print(" ");
				print(cur_node.keys[i])

		if not cur_node.leaf:
			traverse(cur_node.childs[len(cur_node.keys)]

	
