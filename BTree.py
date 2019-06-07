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

	def _splitChild(self, cur_node):
		currentParent = None
		splitIndex = self.degree / 2
		risingKey = cur_node.keys[splitIndex]
		right = BTreeNode(self.degree, cur_node.leaf)
		if cur_node.parent:
			currentParent = cur_node.parent
			i = 0
			while i < len(currentParent)+1 and currentParent.child[i] != cur_node:
				i += 1
			j = len(currentParent.keys)
			while j > i:
				currentParent.child[j+1] = currentParent.child[j]
				currentParent.keys[j] = currentParent.keys[j-1]
				j -= 1

			currentParent.keys[i] = risingKey
			currentParent.child[j+1] = right
			right.parent = currentParent

		i = splitIndex + 1
		while  i < (len(cur_node.keys)+1):
			right.child[i - splitIndex - 1]  = cur_node.child[i]
			if cur_node.child[i]:
				right.leaf = False
				if cur_node.child[i]:
					cur_node.child[i].parent = right
				cur_node.child[i] = None
			
		i = splitIndex + 1
		while i< len(cur_node.keys):
			right.keys[i - splitIndex - 1] = cur_node.keys[i]
		
		left = cur_node
		
		if cur_node.parent:
			return cur_node.parent
		
		else:
			self.root = BTreeNode(self.degree, cur_node.leaf)
			self.root.keys[0] = risingKey
			self.child[0] = left
			self.child[1] = right
			left.parent = self.root
			right.parent = self.root
			self.root.leaf = False
			return self.root
	
	def removeElement(self, key):
		if not self.root:
			print("The tree is empty\n")
			return
			
		_remove(self.root, key)
		
		if len(self.root.keys) == 0:
			tmp = self.root
			if root.leaf:
				self.root = None
			else
				self.root = self.root.child[0]
				self.root.parent = None
		
		return None
	
	def _remove(cur_node, key):
		del_node = search(key)
		if del_node == None:
			print("%d is not exist\n", key)
			return None
		
		i = len(del_node.keys) - 1
		temp = del_node.keys[i]
		
		if del_node.leaf:
			while i>0 and temp != key:
				del_node.keys[i-1] = temp
				temp = del_node.keys[i-1]
				i -= 1
			
			_balancingAfterDel(del_node)
		
		else:
			while i>0 and temp!=key:
				i -= 1
			
			del_node.keys[i] = del_node.child[i].keys[len(del_node.child[i]) - 1]
			_balancingAfterDel(del_node.child[i])
		
		return None
		
		
