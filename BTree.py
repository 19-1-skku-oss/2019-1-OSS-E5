class BTreeNode(object):
	def __init__(self, degree, leaf):
		self.leaf = leaf
		self.keys = []
		self.childs = []
		self.parent = None
		self.degree = degree

class BTree(object):
	def __init__(self, degree):
		self.degree = degree - 1
		self.root = None

	def traverse(self):
		if len(self.root.keys) != 0:
			_traverse(self.root)

	def _traverse(cur_node):
		for i in range(len(cur_node.keys)):
			if not cur_node.leaf:
				_traverse(cur_node.childs[i])
			
			print(" ");
			print(cur_node.keys[i])

		if not cur_node.leaf:
			traverse(cur_node.childs[len(cur_node.keys)]

	def search(self, key):
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

	def insertElement(self, key):
		if search(key) != None:
			print("The tree already has %d \n", key)
			return None

		if self.root == None:
			self.root = BTreeNode(self.degree, True)
			self.root.keys.append(key)

		else:
			_insert(self.root, key)

	def _insert(cur_node, key):
		i = len(cur_node.keys)

		if cur_node.leaf:
			while i>0 and cur_node.keys[i-1] > key:
				cur_node.keys[i] = cur_node->keys[i-1]
				i -= 1

			cur_node.keys[i] = key
			_balancing(cur_node)

		else:
			while i>0 and cur_node.keys[i-1] > key:
				i -= 1
			
			_insert(cur_node.childs[i], key)

	def _balancing(self, cur_node):
		if len(cur_node.keys) <= degree:
			return None
		
		elif not cur_node.parent:
			self.root = _splitChild(cur_node)
			return None

		else:
			parent = _splitChild(cur_node)
			_balancing(parent)

	
