import sys
import unittest
from trees.bst import BSTNode

class BSTTestCase(unittest.TestCase):
    def testSearchSingleNodeTree(self):
        '''
            Tree:   10
        '''
        node = BSTNode(10)
       
        # Search for existing values  
        assert node.search(10) is node

        # Boundary tests
        assert node.search(9) is None
        assert node.search(11) is None

        assert node.search(0) is None
        assert node.search(sys.maxint) is None

    def testSearchNodeWithSingleChild(self):
        '''
            Tree:   10
                      \
                       11
        '''
        node = BSTNode(10)
        node.insert(11)

        # Search for existing values
        assert node.search(10) is node
        assert node.search(11) is not node
        assert node.search(11) is not None
        assert node.search(11).value == 11

        # Boundary tests
        assert node.search(9) is None
        assert node.search(12) is None

        assert node.search(0) is None
        assert node.search(sys.maxint) is None

    def testSearchNodeWithLeftGrandChild(self):
        '''
            Tree:   10
                      \
                       12
                      /
                    11
        '''
        # Note that the resulting tree depends on the insertion order.
        # This makes this a white-box test
        node = BSTNode(10)
        node.insert(12)
        node.insert(11)

        # Search for existing values
        assert node.search(10) is node
        assert node.search(11) is not node
        assert node.search(11) is not None
        assert node.search(11).value == 11
        assert node.search(12) is not node
        assert node.search(12) is not None
        assert node.search(12).value == 12

        # Boundary tests
        assert node.search(9) is None
        assert node.search(13) is None

        assert node.search(0) is None
        assert node.search(sys.maxint) is None

    def testSearchNodeWithRightGrandChild(self):
        '''
            Tree:   10
                   /   
                  8
                   \   
                    9
        '''
        # Note that the resulting tree depends on the insertion order.
        # This makes this a white-box test
        node = BSTNode(10)
        node.insert(8)
        node.insert(9)

        # Search for existing values
        assert node.search(10) is node
        assert node.search(8) is not node
        assert node.search(8) is not None
        assert node.search(8).value == 8
        assert node.search(9) is not node
        assert node.search(9) is not None
        assert node.search(9).value == 9

        # Boundary tests
        assert node.search(7) is None
        assert node.search(11) is None

        assert node.search(0) is None
        assert node.search(sys.maxint) is None

    def testSearchNodeWithTwoChildren(self):
        '''
            Tree:   10
                   /  \
                  8    12
        '''
        # Note that the resulting tree depends on the insertion order.
        # This makes this a white-box test
        node = BSTNode(10)
        node.insert(8)
        node.insert(12)

        # Search for existing values
        assert node.search(10) is node
        assert node.search(8) is not node
        assert node.search(8) is not None
        assert node.search(8).value == 8
        assert node.search(12) is not node
        assert node.search(12) is not None
        assert node.search(12).value == 12

        # Boundary tests
        assert node.search(7) is None
        assert node.search(9) is None
        assert node.search(11) is None
        assert node.search(13) is None

        assert node.search(0) is None
        assert node.search(sys.maxint) is None

    def _testRemoveRoot(self):
        node = BSTNode(10)

        assert node.value == 10
        
        node.delete(10)

        assert node.value is None

    def testRemoveCompleteTree(self):
        '''
            Builds a complete tree, then removes all its values but the root

            Tree:   10
                   /  \
                  8    12
                 / \   /  \
                7   9 11  13
        '''
        # Note that the resulting tree depends on the insertion order.
        # This makes this a white-box test
        node = BSTNode(10)
        node.insert(8)
        node.insert(9)
        node.insert(7)
        node.insert(12)
        node.insert(11)
        node.insert(13)

        for i in range(7, 13):
            assert node.search(i) is not None
            assert node.search(i).value == i

        # First case: remove root
        node.delete(10)
        assert node.search(10) is None

        for i in [7, 8, 9, 11, 12, 13]:
            assert node.search(i) is not None
            assert node.search(i).value == i
       
        # The new node value should be it's sucessor's, which is 11
        assert node.value == 11

        '''
            Partial Tree:   11
                           /  \
                          8    12
                         / \     \
                        7   9     13
        '''

        # Second case: remove node with single right child
        node.delete(12)
        assert node.search(12) is None

        for i in [7, 8, 9, 11, 13]:
            assert node.search(i) is not None
            assert node.search(i).value == i
        
        '''
            Partial Tree:   11
                           /  \
                          8    13
                         / \      
                        7   9     
        '''

        # Third case: remove node with no children
        node.delete(13)
        assert node.search(13) is None

        for i in [7, 8, 9, 11]:
            assert node.search(i) is not None
            assert node.search(i).value == i
        
        '''
            partial tree:   11
                           / 
                          8    
                         / \      
                        7   9     
        '''

        # Fourth case: remove children with a single left child
        # First, remove 9 to make 7 a single child
        node.delete(9)
        assert node.search(9) is None

        # Now, remove 8
        node.delete(8)
        assert node.search(8) is None

        for i in [7, 11]:
            assert node.search(i) is not None
            assert node.search(i).value == i

        '''
            partial tree:   11
                           / 
                          7
        '''

        # Remove 7 (single left child, again
        node.delete(7)
        assert node.search(7) is None
        
        assert node.search(11) is not None
        assert node.search(11).value == 11
        
        # Remove root
        node.delete(11)

        for i in range(7, 13):
            assert node.search(i) is None

    def testRotateRight(self):
        node = BSTNode(10)
        node.insert(8)
        node.insert(7)
        node.insert(9)
        node.insert(11)
        '''
              10             8
             /  \           /  \
            8    11   ==>  7    10
           / \                 /  \
          7   9               9    11
        '''

        assert node.value == 10
        assert node.left.value == 8
        assert node.left.left.value == 7
        assert node.left.right.value == 9
        assert node.right.value == 11

        # All nodes are reachable
        for i in range(7, 11):
            assert node.search(i) is not None and node.search(i).value == i

        node.rotate_right()

        assert node.left.left is None
        assert node.left.right is None

        assert node.value == 8
        assert node.left.value == 7
        assert node.right.value == 10
        assert node.right.left.value == 9
        assert node.right.right.value == 11

        assert node.parent is None
        assert node.left.parent is node
        assert node.right.parent is node
        assert node.right.left.parent is node.right
        assert node.right.right.parent is node.right

        # All nodes still are reachable
        for i in range(7, 11):
            assert node.search(i) is not None and node.search(i).value == i

    def testRotateRightSingleChild(self):
        node = BSTNode(10)
        node.insert(8)

        '''
              10      8
             /         \
            8     ==>   10
        '''

        node.rotate_right()

        assert node.left is None

        assert node.value == 8
        assert node.right.value == 10
        
        assert node.right.parent == node

    def testRotateRightTwoChildren(self):
        node = BSTNode(10)
        node.insert(8)
        node.insert(11)

        '''
              10         8
             /  \         \
            8    11 ==>   10
                            \
                             11
        '''

        node.rotate_right()

        assert node.left is None

        assert node.value == 8
        assert node.right.value == 10
        assert node.right.right.value == 11
        
        assert node.right.parent is node
        assert node.right.right.parent is node.right

    def testRotateLeft(self):
        node = BSTNode(9)
        node.insert(8)
        node.insert(11)
        node.insert(10)
        node.insert(12)
        '''
              9             11
             / \           /  \
            8   11   ==>  9    12
               /  \      / \       
              10  12    8   10
        '''

        assert node.value == 9
        assert node.left.value == 8
        assert node.right.value == 11
        assert node.right.left.value == 10
        assert node.right.right.value == 12

        # All nodes are reachable
        for i in range(8, 12):
            assert node.search(i) is not None and node.search(i).value == i

        node.rotate_left()

        assert node.right.left is None
        assert node.right.right is None

        assert node.value == 11
        assert node.left.value == 9
        assert node.left.left.value == 8
        assert node.left.right.value == 10
        assert node.right.value == 12
        
        assert node.parent is None
        assert node.right.parent is node
        assert node.left.parent is node
        assert node.left.left.parent is node.left
        assert node.left.right.parent is node.left

        # All nodes still are reachable
        for i in range(8, 12):
            assert node.search(i) is not None and node.search(i).value == i

if __name__ == '__main__':
    unittest.main()
