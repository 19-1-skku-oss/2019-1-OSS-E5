class CList:
    class Node:
        def __init__(self, item,link):
            self.item = item
            self.next = link

    def __init__(self):
        self.last = None
        self.size = 0

    def no_items(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        n = self.Node(item, None)
        if self.is_empty():
            n.next = n
            self.last=n

        else:
            n.next = self.last.next
            self.last.next = n
        self.size += 1

    def first(self):
        if self.is_empty():
            raise EmptyError("Underflow")
        f = self.last.next
        return f.item

    def delete(self):
        if self.is_empty():
            raise EmptyError("Underflow")
        x = self.last.next
        if self.size == 1:
            self.last = None
        else:
            self.last.next = x.next
        self.size -=1

    def print_list(self):
        if self.is_empty():
            print("list is Empty")
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item,"->", end="")
                p = p.next
            print(p.item)

class EmptyError(Exception):
    pass
