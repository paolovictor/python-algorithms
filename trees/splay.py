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

from bst import BSTNode

class SplayTreeNode(BSTNode):
    '''
        A Splay Tree implementation. Check: http://en.wikipedia.org/wiki/Splay_tree
    '''

    def splay_search(self, value):
        node = BSTNode.search(self, value)

        node.splay()

        return self # returns root, since node was moved to its place

    def insert(self, value):
        self.insert_node(SplayTreeNode(value))    

    def delete(self, value):
        # splay node to be deleted
        node = BSTNode.search(self, value)

        node.splay()

        # separate the left subtree, splay its successor to top
        node.left.parent = None
        node.left.successor().splay()
        
        # replace left subtree root with root
        node.value = node.left.value
        node.right = node.left.right
        node.left = node.left.left

        if node.left: node.left.parent = node
        if node.right: node.right.parent = node

    def splay(self):
        if self.parent is None: # The node is the root
            return

        if self.parent.parent is None: # If the parent is the root
            # Rotate on edge direction and splay parent
            if self is self.parent.left:
                self.parent.rotate_right()
            else:
                self.parent.rotate_left()
        else:
            # self and parent are both left or right children
            if self is self.parent.left and self.parent is self.parent.parent.left:
                self.parent.parent.rotate_right()
                self.parent.rotate_right()
            elif self is self.parent.right and self.parent is self.parent.parent.right:
                self.parent.parent.rotate_left()
                self.parent.rotate_left()
            elif self is self.parent.left and self.parent is self.parent.parent.right:
                self.parent.rotate_right()
                self.parent.parent.rotate_left()
            elif self is self.parent.right and self.parent is self.parent.parent.left:
                self.parent.rotate_left()
                self.parent.parent.rotate_right()

            self.parent.splay() # after the rotations, the parent has been replaced by self 
