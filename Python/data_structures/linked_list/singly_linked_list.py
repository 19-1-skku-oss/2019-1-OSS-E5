'''
Singly linked list is basic form or linked list.
Which consist of :
[data/nextnode-]-->[data/nextnode-]-->[data/nextnode]

Study singly linked list first, also undertanding this will give you firtst step to learn data structure.
'''

from __future__ import print_function


class Node:  # Create a Node
    def __init__(self, data):
        self.data = data  # Given data
        self.next = None  # Given next to None


class Linked_List: # Linked list structure
    def __init__(self):
        self.Head = None    # Initialize Head to None
        
    def insert_tail(self, data): # Insert at tail
        if(self.Head is None): self.insert_head(data)    #If this is first node, call insert_head
        else:
            temp = self.Head
            while(temp.next != None):    #Traverse to last node
                temp = temp.next
            temp.next = Node(data)    #Create node & link to tail

    def insert_head(self, data): # Insert at head
        newNod = Node(data)    # Create a new node
        if self.Head != None:
            newNod.next = self.Head     # Link newNode to head
        self.Head = newNod    # Make NewNode as Head

    def printList(self):  # Print every node data
        if self == None:
		return print("None")
	tamp = self.Head
	print(tamp.data,end=" ")
        while tamp is not None:
            print("-->",tamp.data,end=" ")
            tamp = tamp.next
	print()

    def delete_head(self):  # Delete from head
        temp = self.Head
        if self.Head != None:
            self.Head = self.Head.next
            temp.next = None
        return temp
        
    def delete_tail(self):  # Delete from tail
        tamp = self.Head
        if self.Head != None:
            if(self.Head.next is None):    # if Head is the only Node in the Linked List
                self.Head = None
            else:
                while tamp.next.next is not None:  # find the 2nd last element
                    tamp = tamp.next
                tamp.next, tamp = None, tamp.next    #(2nd last element).next = None and tamp = last element 
        return tamp

    def isEmpty(self): # True if empty
        return self.Head is None  # Return if Head is none

    def reverse(self): # Make list go backward
        prev = None
        current = self.Head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.Head = prev

def main(): # Main for test
    A = Linked_List()
    print("Inserting 1st at Head")re
    a1=input()
    A.insert_head(a1)
    print("Inserting 2nd at Head")
    a2=input()
    A.insert_head(a2)
    print("\nPrint List : ")
    A.printList()
    print("\nInserting 1st at Tail")
    a3=input()    
    A.insert_tail(a3)
    print("Inserting 2nd at Tail")
    a4=input()
    A.insert_tail(a4)
    print("\nPrint List : ")
    A.printList()
    print("\nDelete Head")
    A.delete_head()
    print("Delete Tail")
    A.delete_tail()
    print("\nPrint List : ")
    A.printList()
    print("\nReverse Linked List")
    A.reverse()
    print("\nPrint List : ")
    A.printList()
    
if __name__ == '__main__':
	main()
