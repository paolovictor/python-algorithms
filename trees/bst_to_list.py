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

def __bst_to_list__(root):
    if not root: 
        return

    __bst_to_list__(root.left)
    __bst_to_list__(root.right)

    root.left = root.predecessor()
    if root.left: root.left.right = root

    root.right = root.successor()
    if root.right: root.right.left = root


def bst_to_list(root):
    '''
    Converts the BST with the given root node to a doubly
    linked list, on which left -> previous and right -> next

    It's actually arguable if it's really O(1) in memory, since
    you can't really ignore the function stack pointers.
    I've got to try an iterative implementation. 
    '''
    # Finding the start of the list
    s = root
    while s.left:
        s = s.left

    __bst_to_list__(root)

    return s
