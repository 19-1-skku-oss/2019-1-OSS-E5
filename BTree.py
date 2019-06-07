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

	def search(int key):
		return len(self.root.keys)==0?None:_search(self.root, key)

	def _search(cur_node, key):
		i=0
		while i<len(cur_node.keys) and key > cur_node.keys[i]:
			i += 1

		if cur_node.keys[i] == key
			return cur_node

		if cur_node.leaf:
			return None

		return _search(cur_node.childs[i], key)
