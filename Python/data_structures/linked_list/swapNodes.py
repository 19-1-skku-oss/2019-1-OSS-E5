'''
In this py code you can learn swaping node.
'''
class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None


class Linkedlist:
    def __init__(self): # Track only by head
        self.head = None 

    def print_list(self): # Display linked list
        if self.head == None:
            return print("None")
        temp = self.head
        print(temp.data,end=" ")
        temp = temp.next
        while temp is not None:
            print("-->",temp.data,end=" ")
            temp = temp.next
        print()
# Adding nodes
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

# Swapping nodes (Look carefully to execption : head node)
    def swapNodes(self, d1, d2):
        prevD1 = None
        prevD2 = None
        if d1 == d2:
            return
        else:
            # Find d1
            D1 = self.head
            while D1 is not None and D1.data != d1:
                prevD1 = D1
                D1 = D1.next
            # Find d2
            D2 = self.head
            while D2 is not None and D2.data != d2:
                prevD2 = D2
                D2 = D2.next
            if D1 is None and D2 is None:
                return
            # If D1 is head
            if prevD1 is not None:
                prevD1.next = D2
            else:
                self.head = D2
            # If D2 is head
            if prevD2 is not None:
                prevD2.next = D1
            else:
                self.head = D1
                
            temp = D1.next
            D1.next = D2.next
            D2.next = temp

# Swapping code ends here



if __name__ == '__main__': # Main for test
    list = Linkedlist()
    list.push(5)
    list.push(4)
    list.push(3)
    list.push(2)
    list.push(1)
    
    list.print_list()

    list.swapNodes(1, 4)
    print("After swapping")
    list.print_list()
