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

def preorder_recursive(root, result):
    ''' 
    Pre-order recursive traversal. The nodes' values are
    appended to the result list in traversal order
    '''
    if not root:
        return
    
    result.append(root.value)

    preorder_recursive(root.left, result)
    preorder_recursive(root.right, result)

def inorder_recursive(root, result):
    ''' 
    In-order recursive traversal. The nodes' values are
    appended to the result list in traversal order
    '''
    if not root:
        return
    
    inorder_recursive(root.left, result)

    result.append(root.value)

    inorder_recursive(root.right, result)

def postorder_recursive(root, result):
    ''' 
    Post-order recursive traversal. The nodes' values are
    appended to the result list in traversal order
    '''
    if not root:
        return
    
    postorder_recursive(root.left, result)
    postorder_recursive(root.right, result)

    result.append(root.value)

def preorder_iterative(root, result):
    ''' 
    Pre-order iterative traversal. The nodes' values are
    appended to the result list in traversal order
    '''
    if not root:
        return

    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()

        result.append(node.value)

        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)    

def inorder_iterative(root, result):
    ''' 
    In-order iterative traversal. The nodes' values are
    appended to the result list in traversal order
    '''
    if not root:
        return

    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            1result.append(node.value)
            node = node.right

def postorder_iterative(root, result):
    ''' 
    Post-order iterative traversal. The nodes' values are
    appended to the result list in traversal order
    '''
    if not root:
        return

    visited = set()

    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()

            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.value)
                node = None
