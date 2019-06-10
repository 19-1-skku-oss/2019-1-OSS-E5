'''
Segment tree is fast at finding interval sum.
Parents node have integrated data of child nodes
So its time complexity of getting sum of interval or editing is O(log n)
which is way faster than basic binary tree.
Because of is fast speed, studying about segment tree is one of the essential part of studing datastructure.
'''

from __future__ import print_function
import math # Get math library

'''
Storing tree in array
:
      3
    /  \
  1     5   == [3,1,5,0,2,None,6]
 / \   / \
0   2 X   6


'''


class SegmentTree: # Use array to store tree
    
    def __init__(self, A):
        self.N = len(A)
        self.st = [0] * (4 * self.N) # approximate the overall size of segment tree with array N
        self.build(1, 0, self.N - 1)
        
    def left(self, idx):  # Jump to left index 
        return idx * 2

    def right(self, idx): # Jump to right index
        return idx * 2 + 1

    def build(self, idx, l, r):# Build segment tree 
        if l == r:
            self.st[idx] = A[l]
        else:
            mid = (l + r) // 2
            self.build(self.left(idx), l, mid)
            self.build(self.right(idx), mid + 1, r)
            self.st[idx] = max(self.st[self.left(idx)] , self.st[self.right(idx)])
    
    def update(self, a, b, val):
        return self.update_recursive(1, 0, self.N - 1, a - 1, b - 1, val)
    
    def update_recursive(self, idx, l, r, a, b, val): # update(1, 1, N, a, b, v) for update val v to [a,b]
        if r < a or l > b:
            return True
        if l == r :
            self.st[idx] = val
            return True
        mid = (l+r)//2
        self.update_recursive(self.left(idx), l, mid, a, b, val)
        self.update_recursive(self.right(idx), mid+1, r, a, b, val)
        self.st[idx] = max(self.st[self.left(idx)] , self.st[self.right(idx)])
        return True

    def query(self, a, b):
        return self.query_recursive(1, 0, self.N - 1, a - 1, b - 1)

    def query_recursive(self, idx, l, r, a, b): #query(1, 1, N, a, b) for query max of [a,b]
        if r < a or l > b:
            return -math.inf
        if l >= a and r <= b:
            return self.st[idx]
        mid = (l+r)//2
        q1 = self.query_recursive(self.left(idx), l, mid, a, b)
        q2 = self.query_recursive(self.right(idx), mid + 1, r, a, b)
        return max(q1, q2)

    def showData(self): # Display
        showList = []
        for i in range(1,N+1):
            showList += [self.query(i, i)]
        print (showList)
            

if __name__ == '__main__': # Main for testing
    A = [1,2,-4,7,3,-5,6,11,-20,9,14,15,5,2,-8]
    N = 15
    segt = SegmentTree(A)
    print (segt.query(4, 6))
    print (segt.query(7, 11))
    print (segt.query(7, 12))
    segt.update(1,3,111)
    print (segt.query(1, 15))
    segt.update(7,8,235)
    segt.showData()
