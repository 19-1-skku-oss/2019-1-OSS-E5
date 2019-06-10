class BTreeNode(object):
	def __init__(self, degree, leaf):
		#leaf is boolean variable that means cur_node is leaf or not
		#현 node가 leaf인지 아닌지에 대한 변수
		self.leaf = leaf

		#keys that cur_node has
		#현 node가 가지는 keys
 		self.keys = []
		
		#childs that cur_node has
		#현 node가 가지는 childs
		self.childs = []

		#parent of cur_node
		#현 node의 parent
		self.parent = None

		#degree of BTree
		#BTree의 degree
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
		if len(self.root.keys) == 0:
			return None
		else:
			return _search(self.root, key)

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
				cur_node.keys[i] = cur_node.keys[i-1]
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
		
	def _balancingAfterDel(self, cur_node):
		minKeys = (degree+2)/2 - 1
		parentIndex = 0
		
		if len(cur_node.keys) < minKeys:
			if not cur_node.parent:
				if len(cur_node.keys) == 0:
					self.root = cur_node.child[0]
					if self.root:
						self.root.parent = None
			else:
				parent = cur_node.parent
				while parent.child[parentIndex] != cur_node:
					parentIndex += 1
				if parentIndex > 0 and len(parent.child[parentIndex-1].keys) > minKeys:
					_borrowFromLeft(cur_node, parentIndex)
				elif parentIndex < len(parent.keys) and len(parent.child[parentIndex+1].keys) > minKeys:
					_borrowFromRight(cur_node, parentIndex)
				elif parentIndex==0:
					next = _merge(cur_node)
					_balancingAfterDel(next.parent)
	
	def _borrowFromRight(cur_node, parentIdx):
		parentNode = cur_node.parent
		
		rightSib = parentNode.child[parentIdx + 1]
		present->keys[len(cur_node.keys) - 1] = parentNode.keys[parentIdx]
		parentNode.keys[parentIdx] = rightSib.keys[0]
		
		
		if not cur_node.leaf:
			cur_node.child[len(present.keys)] = rightSib.child[0]
			cur_node.child[len(present.keys)] = cur_node
			
			for i in range(len(rightSib.keys) + 1):
				rightSib.child[i-1] = rightSib.child[i]
				
		for i in range(len(rightSib.keys)):
			rightSib.keys[i-1] = rightSib.keys[i]
	
	def _borrowFromLeft(cur_node, parentIdx):
		parentNode = cur_node.parent
		
		i = len(cur_node.keys) - 1
		while i > 0:
			cur_node.keys[i] = cur_node.keys[i-1]
			i--
		leftSib = parentNode.child[parentIdx - 1]
		
		if not cur_node.leaf:
			i = len(cur_node.keys)
			while i > 0:
				cur_node.child[i] = cur_node.child[i-1]
				i--
			
			cur_node.child[0] = leftSib.child[len(leftSib.keys)]
			leftSib.child[len(leftSib.keys)] = None
			cur_node.child[0].parent = cur_node
		
		cur_node.keys[0] = parentNode.keys[parentIdx-1]
		parentNode.keys[parentIdx-1] = leftSib.keys[len(leftSib.keys) - 1]
		
	def _merge(cur_node):
		parentNode = cur_node.parent
		parentIndex = 0
		
		while parentNode.child[parentIndex] != cur_node:
			parentIndex += 1
		
		rightSib = parentNode.child[parentIndex + 1]
		
		cur_node.keys[len(cur_node.keys)] = parentNode.keys[parentIndex]
		fromParentIndex = len(present.keys)
		
		for i in range(len(rightSib.keys)):
			cur_node.keys[len(cur_node) + 1 + i] = rightSib.keys[i]
		
		if not cur_node.leaf:
			for i in range(len(rightSib.keys)):
				cur_node.child[len(cur_node) + 1 + i] = rightSib.child[i]
				cur_node.child[len(cur_node) + 1 + i] = cur_node
			
		i = parentIndex + 1
		while i < len(parentNode.keys):
			parentNode.child[i] = parentNode.child[i + 1]
			parentNdoe.keys[i-1] = parentNode.keys[i]
			
		return cur_node
		
	
