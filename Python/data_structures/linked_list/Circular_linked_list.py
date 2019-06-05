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

    def is_empty(self): #Check if Circular list is empty
        return self.size == 0

    def insert(self, item): # inserting new node to circular list
        n = self.Node(item, None)

        if self.is_empty():
            n.next = n
            self.last=n
        else:
            n.next = self.last.next
            self.last.next = n
        self.size += 1

    def first(self): # Show first item
        if self.is_empty():
            raise EmptyError("List is empty")
        f = self.last.next
        return f.item

    def delete_first(self): # delete first node
        if self.is_empty():
            raise EmptyError("List is empty")
        x = self.last.next
        if self.size == 1:
            self.last = None
        else:
            self.last.next = x.next
        self.size -=1

    def delete_last(self):
        return 0

    def insert_select(self):
        return 0
    
    def delete_select(self):
        return 0

    def print_list(self):
        if self.is_empty():
            print("list is Empty")
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item,"-> ", end="")
                p = p.next
            print(p.item)

class EmptyError(Exception):
    pass

if __name__=="__main__":
    s = CList()
    s.insert("pear")
    s.insert("cherry")
    s.insert("orange")
    s.insert("apple")
    s.print_list()
    print("Length of S is :",s.lens())
    print("First node of S",s.first())
    s.delete_first()
    print("Afeter deleting first node :",end="")
    s.print_list()
    print("Length of S is :",s.lens())
    print("First node of S",s.first())
    s.delete_first()
    print("Afeter deleting first node :",end="")
    s.print_list()
    s.delete_first()
    print("Afeter deleting first node :",end="")
    s.print_list()
    s.delete_first()
    print("Afeter deleting first node :",end="")
    s.print_list()
