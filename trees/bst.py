'''
Copyright (C) 2011 by Paolo Victor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

class BSTNode(object):
    '''
    A binary search tree (BST) node
    '''

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def search(self, value):
        if self.value == value:
            return self

        if self.left is not None and self.value > value:
            return self.left.search(value)
        elif self.right is not None:
            return self.right.search(value)

        return None

    def insert(self, value):
        '''
        Inserts a value to the tree with self as root
        
        @param value The value to be inserted
        '''
        # Base case: empty root node
        if self.value is None:
            self.value = value
            return

        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
                self.left.parent = self
            else:
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = BSTNode(value)
                self.right.parent = self
            else:
                self.right.insert(value)
        else:
            pass # Duplicate values are ignored

    def delete(self, value):
        # Base case: root node
        if self.value == value:
            self.__delete_node__()
        elif value < self.value and self.left is not None:
            self.left.delete(value)
        elif self.right is not None:
            self.right.delete(value)

    def __delete_node__(self):
        '''
        Removes the node from its tree, updating its children node pointers, if any.

        @param parent the node's parent
        '''
        if self.right and self.left:
            # Node has two children Replace value with successor s and delete s
            if self.right:
                s = self.successor()
                self.value = s.value
                s.__delete_node__()
        elif self.right or self.left:
            # Node has single child. Replace it with only child
            child = self.right is not None and self.right or self.left

            self.value = child.value

            self.left = child.left
            self.right = child.right

            if self.left : self.left.parent = self
            if self.right : self.right.parent = self
        else:
            # None has no children, erase value and update parent
            self.value = None

            if self.parent:
                if self is self.parent.left:
                    self.parent.left = None
                else:
                    self.parent.right = None

    def successor(self):
        s = None

        if self.right:
            s = self.right
            while s.left:
                s = s.left

        return s

    def predecessor(self):
        s = None

        if self.left:
            s = self.left
            while s.right:
                s = s.right

        return s

    def __str__(self):
        return "(%s, l: %s, r: %s)" % (self.value, self.left is not None and self.left.value or 'N', self.right is not None and self.right.value or 'N')
