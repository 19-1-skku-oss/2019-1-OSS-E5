'''
Recomand studying segment tree first.
Fanwick tree is made to save more memory space(than segment).
So it is upgrade version of segment tree.
Its time complexity iof update is O(log N) and use less memory.
Crusal point of fenwick tree is that partcial sum algorithms can make interval sum.

'''
from __future__ import print_function
class FenwickTree:

    def __init__(self, SIZE): # Create fenwick tree with size SIZE
        self.Size = SIZE
        self.ft = [0 for i in range (0,SIZE)]

    def update(self, i, val): # Update data (adding) in index i in O(lg N)
        while (i < self.Size):
            self.ft[i] += val
            i += i & (-i)
            # i += i & (-i) this means adding 1 to lowest "1" location.
            # Need to understand bit operation.

    def query(self, i): # Query cumulative data from index 0 to i in O(lg N)
        ret = 0
        while (i > 0):
            ret += self.ft[i]
            i -= i & (-i)
            # i += i & (-i) this means adding 1 to lowest "1" location.
        return ret
            
if __name__ == '__main__': # Main for test
    f = FenwickTree(100)
    f.update(1,20)
    f.update(4,4)
    print (f.query(1))
    print (f.query(3))
    print (f.query(4))
    f.update(2,-5)
    print (f.query(1))
    print (f.query(3))
