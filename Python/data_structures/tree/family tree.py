r'''
Not only binary but also varable tree exsist.
Tree is widely used data structure.
Tree is hierarchical structure that has one direct parent node and some direct child node.
Number of child node is not restricted to two.
If number of child node is restricted to two it is binary.
So in this code I will show you family tree, which you can simply find in daily life.
 '''

class Node: # This is the Class Node with constructor that contains data variable to type data and left,right pointers.
    def __init__(self, data):
        self.data = data
        self.son1 = None
        self.son2 = None
        self.daughter1 =None
        self.daughter2 =None

def display(tree): # Traversal of the tree --> display
    if tree is None: 
        return 0
    
    print(tree.data)

    if tree.son1 is not None:
        display(tree.son1)

    if tree.son2 is not None:
        display(tree.son2)

    if tree.daughter1 is not None:
        display(tree.daughter1)
        
    if tree.daughter2 is not None:
        display(tree.daughter2)

    return

def depth_of_tree(tree): #This is the recursive function to find the depth of binary tree.
    if tree is None:
        return 0
    else:
        depth_son1_tree = depth_of_tree(tree.son1)
        depth_son2_tree = depth_of_tree(tree.son2)
        depth_daughter1_tree = depth_of_tree(tree.daughter1)
        depth_daughter2_tree = depth_of_tree(tree.daughter2)

        if  depth_son1_tree >= depth_son2_tree and depth_son1_tree >=depth_daughter1_tree and depth_son1_tree >=depth_daughter2_tree:
            return 1 + depth_son1_tree
        elif  depth_son2_tree >= depth_son1_tree and depth_son2_tree >=depth_daughter1_tree and depth_son2_tree >=depth_daughter2_tree:
            return 1 + depth_son2_tree
        elif  depth_daughter1_tree >= depth_son1_tree and depth_daughter1_tree >= depth_son2_tree and depth_daughter1_tree >=depth_daughter2_tree:
            return 1 + depth_daughter1_tree
        else:
            return 1 + depth_daughter2_tree

def deleteTree(tree): # Delete tree
        tree.data = None
        tree.son1 = None
        tree.son2 = None
        tree.daughter1 =None
        tree.daughter2 =None


def main(): # Main func for testing.
    tree = Node("Jun")
    tree.son1 = Node("David")
    tree.son2 = Node("Krage")
    tree.son1.son1 = Node("Parker")
    tree.son2.son1 = Node("Josh")
    tree.son2.daughter1 = Node("Ash")
    tree.daughter1 = Node("Fay")
    tree.daughter1.daughter1 = Node("Cathy")
    tree.son2.son1 = Node("Cruze")

    print("Depth of this tree is : ", depth_of_tree(tree))
    print("Tree is: ")
    display(tree)
    
    deleteTree(tree)
    print("After deleting the tree is: ")
    display(tree)
    print("After deleting tree depth of this tree is : ", depth_of_tree(tree))


if __name__ == '__main__':
    main()
    
    r'''

    Example
    :               Jun
           /     /    \     \
       /       /        \     \
     David  Krage      Fay     None
    /       /  \          \
 parker Cruze   Ash      Cathy
    '''
