'''
- A linked list is similar to an array, it holds values. However, links in a linked list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
- A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer, together with next pointer and data which are there in singly linked list.
 - Advantages over SLL - IT can be traversed in both forward and backward direction.,Delete operation is more efficent
'''
from __future__ import print_function


class LinkedList:           #making main class named linked list
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertHead(self, x):
        newLink = Link(x)                            #Create a new link with a value attached to it
        if(self.isEmpty() == True):                  #Set the first element added to be the tail
            self.tail = newLink
        else:
            self.head.previous = newLink             # newLink <-- currenthead(head)
        newLink.next = self.head                     # newLink <--> currenthead(head)
        self.head = newLink                          # newLink(head) <--> oldhead
    
    def deleteHead(self):
        temp = self.head
        self.head = self.head.next                   # oldHead <--> 2ndElement(head) 
        self.head.previous = None                    # oldHead --> 2ndElement(head) nothing pointing at it so the old head will be removed
        if(self.head is None):
            self.tail = None                         #if empty linked list
        return temp
    
    def insertTail(self, x):
        newLink = Link(x)
        newLink.next = None                         # currentTail(tail)    newLink -->
        self.tail.next = newLink                    # currentTail(tail) --> newLink -->
        newLink.previous = self.tail                #currentTail(tail) <--> newLink -->
        self.tail = newLink                         # oldTail <--> newLink(tail) -->
    
    def deleteTail(self):
        temp = self.tail
        self.tail = self.tail.previous              # 2ndLast(tail) <--> oldTail --> None
        self.tail.next = None                       # 2ndlast(tail) --> None
        return temp
    
    def delete(self, x):                            #Find x and delete x in list.
        current = self.head
        
        while(current.value != x):                  # Find the position to delete
            current = current.next
            if current == None:
                return print("There is no ",x," in list")
        
        if(current == self.head):
            self.deleteHead()
            
        elif(current == self.tail):
            self.deleteTail()
            
        else: #Before: 1 <--> 2(current) <--> 3
            current.previous.next = current.next # 1 --> 3
            current.next.previous = current.previous # 1 <--> 3
    
    def isEmpty(self):                               #Will return True if the list is empty
        return(self.head is None)
        
    def display(self):                                #Prints contents of the list

        if self.head == None:                         #Print None if its empty
            print(None)
            return
        
        current = self.head
        while(current.next != None):
            current.displayLink()
            print("<-->", end=" ")
            current = current.next
        current.displayLink()
        print()

class Link:
    next = None                                       #This points to the link in front of the new link
    previous = None                                   #This points to the link behind the new link
    def __init__(self, x):
        self.value = x
    def displayLink(self):
        print("{}".format(self.value), end=" ")

if __name__=="__main__": # Test this data structure
    DL = LinkedList()
    if DL.isEmpty:
        print("Double Linked list Empty")
        print("Display list : ", end=" ")
        DL.display()    
    print("Insert Head 1 :\t", end=" ")
    DL.insertHead("1")
    DL.display()
    print("Insert Head 2 :\t", end=" ")
    DL.insertHead("2")
    DL.display()
    print("Insert Head 3 :\t", end=" ")
    DL.insertHead("3")
    DL.display()
    print("Delete Head :\t", end=" ")
    DL.deleteHead
    DL.display()
    print("Insert tail 4 :\t", end=" ")
    DL.insertTail("4")
    DL.display()
    print("Insert tail 5 :\t", end=" ")
    DL.insertTail("5")
    DL.display()
    print("Insert tail 6 :\t", end=" ")
    DL.insertTail("6")
    DL.display()
    print("Delete tail :\t", end=" ")
    DL.deleteTail()
    DL.display()
    x=input("Element you want to delete : ")
    DL.delete(x)
    print("After deleting ",x," :\t", end=" ")
    DL.display()
