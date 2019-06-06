'''
A binary search Tree is binary tree that automatically sort the input.
Sorting rules can be any thing upper or lower.
(EX. In thi example small order)
By using this datastructure searching time will be much less than by searching linerly.
'''
from __future__ import print_function
class Node:

    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        #Added in order to delete a node easier
        self.parent = parent

    # other class method is for tracking node
        
    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

class BinarySearchTree:

    def __init__(self): # Initalize tree. Root is for tracking starting node.
        self.root = None

    def insert(self, label): 
        # Create a new Node
        new_node = Node(label, None)
        # If Tree is empty
        if self.empty():
            self.root = new_node
        else:
            #If Tree is not empty
            curr_node = self.root
            #While we don't get to a leaf
            while curr_node is not None:
                #We keep reference of the parent node
                parent_node = curr_node
                #If node label is less than current node
                if new_node.getLabel() < curr_node.getLabel():
                #We go left
                    curr_node = curr_node.getLeft()
                else:
                    #Else we go right
                    curr_node = curr_node.getRight()
            #We insert the new node in a leaf
            if new_node.getLabel() < parent_node.getLabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)
            #Set parent to the new node
            new_node.setParent(parent_node)      
    
    def delete(self, label): # Delete selected label 
        if (not self.empty()):
            #Look for the node with that label
            node = self.getNode(label)
            #If the node exists
            if(node is not None):
                #If it has no children
                if(node.getLeft() is None and node.getRight() is None):
                    self.__reassignNodes(node, None)
                    node = None
                #Has only right children
                elif(node.getLeft() is None and node.getRight() is not None):
                    self.__reassignNodes(node, node.getRight())
                #Has only left children
                elif(node.getLeft() is not None and node.getRight() is None):
                    self.__reassignNodes(node, node.getLeft())
                #Has two children
                else:
                    #Gets the max value of the left branch
                    tmpNode = self.getMax(node.getLeft())
                    #Deletes the tmpNode
                    self.delete(tmpNode.getLabel())
                    #Assigns the value to the node to delete and keesp tree structure
                    node.setLabel(tmpNode.getLabel())
                    
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
    def __str__(self):
        list = self.__InOrderTraversal(self.root)
        str = ""
        for x in list:
            str = str + " " + x.getLabel().__str__()
        return str


def testBinarySearchTree():
    r'''
    Example
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13 
    '''

    r'''
    Example After Deletion
                  7
                 / \
                1   4

    '''
    t = BinarySearchTree()
    t.insert(8)
    t.insert(3)
    t.insert(6)
    t.insert(1)
    t.insert(10)
    t.insert(14)
    t.insert(13)
    t.insert(4)
    t.insert(7)

    #Prints all the elements of the list in order traversal
    print(t.__str__())

    if(t.getNode(6) is not None):
        print("The label 6 exists")
    else:
        print("The label 6 doesn't exist")

    if(t.getNode(-1) is not None):
        print("The label -1 exists")
    else:
        print("The label -1 doesn't exist")
    
    if(not t.empty()):
        print(("Max Value: ", t.getMax().getLabel()))
        print(("Min Value: ", t.getMin().getLabel()))
    
    t.delete(13)
    t.delete(10)
    t.delete(8)
    t.delete(3)
    t.delete(6)
    t.delete(14)

    #Gets all the elements of the tree In pre order
    #And it prints them
    list = t.traversalTree(PreOrder, t.root)
    for x in list:
        print(x)

if __name__ == "__main__":
    testBinarySearchTree()
