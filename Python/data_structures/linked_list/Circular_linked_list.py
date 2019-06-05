class CList:
    class Node:
        def __init__(self, item,nexts): # Make Node : item for storage, next linking next node 
            self.item = item
            self.next = nexts

    def __init__(self): #Starting CList initializing
        self.last = None
        self.size = 0

    def lens(self): #lens : number of items in linked list
        return self.size

    def is_empty(self): # Check if Circular list is empty
        return self.size == 0

    def insert_first(self, item): # Inserting new node to first circular list
        n = self.Node(item, None)

        if self.is_empty():
            n.next = n
            self.last=n
        else:
            n.next = self.last.next
            self.last.next = n
        self.size += 1

    def insert_last(self, item): # Inserting new node to first circular list
        n = self.Node(item, None)

        if self.is_empty():
            n.next = n
            self.last=n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n
        self.size += 1

    def first(self): # Show first item
        if self.is_empty():
            raise EmptyError("List is empty")
        f = self.last.next
        return f.item

    def print_list(self): # Print and show the linked list
        if self.is_empty():
            print("list is empty")
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item,"-> ", end="")
                p = p.next
            print(p.item)

    def delete_first(self): # Delete first node
        if self.is_empty():
            raise EmptyError("List is empty")
        x = self.last.next
        if self.size == 1:
            self.last = None
        else:
            self.last.next = x.next
        self.size -=1

    def delete_last(self): # Delete last node
        if self.is_empty():
            raise EmptyError("List is empty")
        x = self.last
        if self.size == 1:
            self.last = None
        else:
            while(x.next != self.last):
                x = x.next
            self.last = x
            self.last.next=x.next.next

        self.size -=1

            
    def search_by_name(self,name): # Search item by it`s name
        if self.is_empty():
            raise EmptyError("List is empty")
        f = self.last.next
        x = f
        count = 0
        while (x.item != name):
            if (x.next == f):
               return "There is no item with such name"
            count = count + 1
            x = x.next
        return count

class EmptyError(Exception):
    pass

if __name__=="__main__": # Test this data structure
    c = CList()
    c.insert_first("b")
    c.insert_last("c")
    c.insert_first("a")
    c.insert_last("d")
    c.print_list()
    print("Find index of node item(c) :", c.search_by_name("c"))
    print("Length of S is :",c.lens())
    print("First node of S",c.first())
    c.delete_last()
    print("Afeter deleting last node :",end="")
    c.print_list()
    print("Length of S is :",c.lens())
    print("First node of S",c.first())
    c.delete_last()
    print("Afeter deleting last node :",end="")
    c.print_list()
    c.delete_first()
    print("Afeter deleting first node :",end="")
    c.print_list()
    c.delete_first()
    print("Afeter deleting first node :",end="")
    c.print_list()
