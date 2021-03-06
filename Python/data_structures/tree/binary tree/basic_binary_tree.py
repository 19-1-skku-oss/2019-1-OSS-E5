r'''
basic_binary_tree is basic tree.
Node consist of two (left, right) target and data.
binary tree can be used in many ways. (EX. it can shorten searching time)
This is for understanding.
so I recommand you just to get some ideas for making more usefull binary tree.
 '''

class Node: # This is the Class Node with constructor that contains data variable to type data and left,right pointers.
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def display(tree): #In Order traversal of the tree
    if tree is None: 
        return 0

    if tree.left is not None:
        display(tree.left)

    print(tree.data)

    if tree.right is not None:
        display(tree.right)

    return

def depth_of_tree(tree): #This is the recursive function to find the depth of binary tree.
    if tree is None:
        return 0
    else:
        depth_l_tree = depth_of_tree(tree.left)
        depth_r_tree = depth_of_tree(tree.right)
        if depth_l_tree > depth_r_tree:
            return 1 + depth_l_tree
        else:
            return 1 + depth_r_tree


def is_full_binary_tree(tree): # This functions returns that is it full binary tree or not?
    if tree is None:
        return True
    if (tree.left is None) and (tree.right is None):
        return True
    if (tree.left is not None) and (tree.right is not None):
        return (is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right))
    else:
        return False

def deleteTree(tree): # Delete tree
        tree.left = None
        tree.right = None
        tree.data = None


def main(): # Main func for testing.
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)

    print(is_full_binary_tree(tree))
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
                    1
                 /     \
                2       3
               / \     / 
              4   5  7   
                 /  /
                6  8
                    \
                     9
    '''
