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

    if root.left:
        __bst_to_list__(root.left)
        r = root.predecessor()
        if r: r.right = root

    if root.right:
        __bst_to_list__(root.right)
        r = root.successor()
        root.right = r

def bst_to_list(root):
    '''
    Converts the BST with the given root node to a doubly
    linked list, on which left -> previous and right -> next
    '''
    # Finding the start of the list
    s = root
    while s.left:
        s = s.left

    __bst_to_list__(root)

    # Fixing the "previous" pointers
    # TODO: That's a bit of a hack. I'll review the
    #       the code to be absolutely sure this is necessary.
    #       'til then, revel on the hackery!
    s1, s2 = s, s.right
    while s2:
        s2.left = s1
        s1, s2 = s2, s2.right
        
    return s
