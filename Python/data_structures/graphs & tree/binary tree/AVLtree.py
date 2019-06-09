'''
An auto-balanced binary tree
Problem of simple binary tree is that if input comes unbalenced, time spent for searching element will be almost same as O(n).
For Example
:
     1
      \
       2
        \
         4
        /  \
       3    5

in This case it is better to save this tree sturcture like this
:
    2
   / \
  1   4
     /  \
    3    5

AVL tree will automatically balce left and right balance level.
So that it`s efficience will be great.
Tool for balancing isfour kind of rotation.
1. leftrotation
2. rightrotation
3. rlrotation
4. lrrotation

Details are at it`s function.
'''

import math # Get math library
import random # Get random library

class my_queue: # Make structure of queue --> later used in traverse and show tree in right format.
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0
    def isEmpty(self):
        return self.head == self.tail
    def push(self,data):
        self.data.append(data)
        self.tail = self.tail + 1
    def pop(self):
        ret = self.data[self.head]
        self.head = self.head + 1
        return ret
    def count(self):
        return self.tail - self.head
    def print(self):
        print(self.data)
        print("**************")
        print(self.data[self.head:self.tail])
        
class my_node: # Make structure of node
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    def getdata(self):
        return self.data
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
    def getheight(self):
        return self.height
    def setdata(self,data):
        self.data = data
        return
    def setleft(self,node):
        self.left = node
        return
    def setright(self,node):
        self.right = node
        return
    def setheight(self,height):
        self.height = height
        return

def getheight(node):
    if node is None:
        return 0
    return node.getheight()

def my_max(a,b):
    if a > b:
        return a
    return b



def leftrotation(node):# If left side of tree is deeper(left side child + left side child), than leftrotation makes total tree balanced.
    r'''
            A                      B
           / \                    / \
          B   C                  Bl  A
         / \       -->          /   / \
        Bl  Br                 UB Br  C
       /
     UB
  
    UB = unbalanced node  
    '''
    print("left rotation node:",node.getdata())
    ret = node.getleft()
    node.setleft(ret.getright())
    ret.setright(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    h2 = my_max(getheight(ret.getright()),getheight(ret.getleft())) + 1         
    ret.setheight(h2)
    return ret

def rightrotation(node): # If right side of tree is deeper(right side child + right side child), than rightrotation makes total tree balanced.
    '''
        a mirror symmetry rotation of the leftrotation
    '''
    print("right rotation node:",node.getdata())
    ret = node.getright()
    node.setright(ret.getleft())
    ret.setleft(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    h2 = my_max(getheight(ret.getright()),getheight(ret.getleft())) + 1         
    ret.setheight(h2)
    return ret

def rlrotation(node):  # If right side of tree is deeper(right side child + left side child), than rightrotation makes total tree balanced.
    r'''
    Two steps :
            A              A                    Br      
           / \            / \                  /  \
          B   C    RR    Br  C       LL       B    A
         / \       -->  /  \         -->    /     / \    == RL
        Bl  Br         B   UB              Bl    UB  C  
             \        /
             UB     Bl
    RR = rightrotation   LR = leftrotation
    '''
    node.setleft(rightrotation(node.getleft()))
    return leftrotation(node)

def lrrotation(node): # If right side of tree is deeper(left side child + right side child), than rightrotation makes total tree balanced.
    '''
        a mirror symmetry rotation of the lrrotation
        Two steps : LL --> RL  == LR
    '''
    node.setright(leftrotation(node.getright()))
    return rightrotation(node)


def insert_node(node,data): # Insert node following AVLTree rule.
    if node is None:
        return my_node(data)
    if data < node.getdata():
        node.setleft(insert_node(node.getleft(),data))
        if getheight(node.getleft()) - getheight(node.getright()) == 2: #an unbalance detected
            if data < node.getleft().getdata():       #new node is the left child of the left child
                node = leftrotation(node)
            else:
                node = rlrotation(node)             #new node is the right child of the left child
    else:
        node.setright(insert_node(node.getright(),data))
        if getheight(node.getright()) - getheight(node.getleft()) == 2:
            if data < node.getright().getdata():
                node = lrrotation(node)
            else:
                node = rightrotation(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    return node

def getRightMost(root): # Right most child
    while root.getright() is not None:
        root = root.getright()
    return root.getdata()
def getLeftMost(root): # Left most child
    while root.getleft() is not None:
        root = root.getleft()
    return root.getdata()

def del_node(root,data): # Delet node following AVLTree rule.
    if root.getdata() == data:
        if root.getleft() is not None and root.getright() is not None:
            temp_data = getLeftMost(root.getright())
            root.setdata(temp_data)
            root.setright(del_node(root.getright(),temp_data))
        elif root.getleft() is not None:
            root = root.getleft()
        else:
            root = root.getright()
    elif root.getdata() > data:
        if root.getleft() is None:
            print("No such data")
            return root
        else:
            root.setleft(del_node(root.getleft(),data))
    elif root.getdata() < data:
        if root.getright() is None:
            return root
        else:
            root.setright(del_node(root.getright(),data))
    if root is None:
        return root
    if getheight(root.getright()) - getheight(root.getleft()) == 2:
        if getheight(root.getright().getright()) > getheight(root.getright().getleft()):
            root = rightrotation(root)
        else:
            root = lrrotation(root)
    elif getheight(root.getright()) - getheight(root.getleft()) == -2:
        if getheight(root.getleft().getleft()) > getheight(root.getleft().getright()):
            root = leftrotation(root)
        else:
            root = rlrotation(root)
    height = my_max(getheight(root.getright()),getheight(root.getleft())) + 1
    root.setheight(height)
    return root

class AVLtree: # Integrate made functions to AVLTree for efficiency and to see balancing work of tree
    def __init__(self):
        self.root = None
    def getheight(self):
        return getheight(self.root)
    def insert(self,data):# Show inserting process
        print("insert:"+str(data))
        self.root = insert_node(self.root,data)
        
    def del_node(self,data): # Show deleting process.
        print("delete:"+str(data))
        if self.root is None:
            print("Tree is empty!")
            return
        self.root = del_node(self.root,data)
    def traversale(self): #a level traversale, gives a more intuitive look on the tree
        q = my_queue()
        q.push(self.root)
        layer = self.getheight()
        if layer == 0:
            return
        cnt = 0
        while not q.isEmpty():
            node = q.pop()
            space = " "*int(math.pow(2,layer-1))
            print(space,end = "")
            if node is None:
                print("*",end = "")
                q.push(None)
                q.push(None)
            else:
                print(node.getdata(),end = "")
                q.push(node.getleft())
                q.push(node.getright())
            print(space,end = "")
            cnt = cnt + 1
            for i in range(100):
                if cnt == math.pow(2,i) - 1:
                    layer = layer -1 
                    if layer == 0:
                        print()
                        print("*************************************")
                        return
                    print()
                    break
        print()
        print("*************************************")
        return

        
if __name__ == "__main__": # Main for test : It prints AVLTree process.
    t = AVLtree()
    t.traversale()
    l = list(range(10))
    random.shuffle(l)
    for i in l:
        t.insert(i)
        t.traversale()
        
    random.shuffle(l)
    for i in l:
        t.del_node(i)
        t.traversale()




    '''
    You can add more function in basic search tree by changing little code.
    But I will not include this for understaning AVLTree easily.
    
    For Example :
    
        def deleteTree(self): # Delete total tree
        self.root= None
    
    def getNode(self, label): # Search for label
        curr_node = None
        #If the tree is not empty
        if(not self.empty()):
            #Get tree root
            curr_node = self.getRoot()
            #While we don't find the node we look for
            #I am using lazy evaluation here to avoid NoneType Attribute error
            while curr_node is not None and curr_node.getLabel() is not label:
                #If node label is less than current node
                if label < curr_node.getLabel():
                    #We go left
                    curr_node = curr_node.getLeft()
                else:
                    #Else we go right
                    curr_node = curr_node.getRight()
        return curr_node

    def getMax(self, root = None): # Find max node
        if(root is not None):
            curr_node = root
        else:
            #We go deep on the right branch
            curr_node = self.getRoot()
        if(not self.empty()):
            while(curr_node.getRight() is not None):
                curr_node = curr_node.getRight()
        return curr_node

    def getMin(self, root = None): # Find min node
        if(root is not None):
            curr_node = root
        else:
            #We go deep on the left branch
            curr_node = self.getRoot()
        if(not self.empty()):
            curr_node = self.getRoot()
            while(curr_node.getLeft() is not None):
                curr_node = curr_node.getLeft()
        return curr_node

    def empty(self): # Check tree this is empty
        if self.root is None:
            return True
        return False

    def __InOrderTraversal(self, curr_node): # Traverse tree (Inorder: There are three ways to traverse 1)
        nodeList = []
        if curr_node is not None:
            nodeList.insert(0, curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
        return nodeList

    def PreOrder(curr_node): # Traverse tree (PreOrder: There are three ways to traverse 2)
        nodeList = []
        if curr_node is not None:
            nodeList = nodeList + PreOrder(curr_node.getLeft())
            nodeList.insert(0, curr_node.getLabel())
            nodeList = nodeList + PreOrder(curr_node.getRight())
        return nodeList

    def PostOrder(curr_node): # Traverse tree (PostOrder: There are three ways to traverse 3)
        nodeList = []
        if curr_node is not None:
            nodeList = nodeList + PostOrder(curr_node.getLeft())
            nodeList = nodeList + PostOrder(curr_node.getRight())
            nodeList.insert(0, curr_node.getLabel())
        return nodeList

    def getRoot(self): #Get root for OOP disign
        return self.root

    def __isRightChildren(self, node): # Tell if node is in rightchild
        if(node == node.getParent().getRight()):
            return True
        return False

    def __reassignNodes(self, node, newChildren): # Reassignnode for edit
        if(newChildren is not None):
            newChildren.setParent(node.getParent())
        if(node.getParent() is not None):
            #If it is the Right Children
            if(self.__isRightChildren(node)):
                node.getParent().setRight(newChildren)
            else:
                #Else it is the left children
                node.getParent().setLeft(newChildren)

    #This function traversal the tree. By default it returns an
    #In order traversal list. You can pass a function to traversal
    #The tree as needed by client code
    def traversalTree(self, traversalFunction = None, root = None):
        if(traversalFunction is None):
            #Returns a list of nodes in preOrder by default
            return self.__InOrderTraversal(self.root)
        else:
            #Returns a list of nodes in the order that the users wants to
            return traversalFunction(self.root)

    #Returns an string of all the nodes labels in the list 
    #In Order Traversal
    '''
