import unittest
from trees.bst import BSTNode
import trees.traversal

class TraversalTestCase(unittest.TestCase):
    def testPreOrderRecursiveSingleNode(self):
        root = BSTNode(4)

        result = []
        trees.traversal.preorder_recursive(root, result)
        assert [4] == result

    def testPreOrderRecursive(self):
        root = BSTNode(4)
        root.insert(2)
        root.insert(3)
        root.insert(1)
        root.insert(6)
        root.insert(5)
        root.insert(7)

        result = []
        trees.traversal.preorder_recursive(root, result)
        assert [4, 2, 1, 3, 6, 5, 7] == result

    def testPreOrderIterativeSingleNode(self):
        root = BSTNode(4)

        result = []
        trees.traversal.preorder_iterative(root, result)
        assert [4] == result

    def testPreOrderIterative(self):
        root = BSTNode(4)
        root.insert(2)
        root.insert(3)
        root.insert(1)
        root.insert(6)
        root.insert(5)
        root.insert(7)

        result = []
        trees.traversal.preorder_iterative(root, result)
        assert [4, 2, 1, 3, 6, 5, 7] == result

    def testInOrderRecursiveSingleNode(self):
        root = BSTNode(4)

        result = []
        trees.traversal.inorder_recursive(root, result)
        assert [4] == result

    def testInOrderRecursive(self):
        root = BSTNode(4)
        root.insert(2)
        root.insert(3)
        root.insert(1)
        root.insert(6)
        root.insert(5)
        root.insert(7)

        result = []
        trees.traversal.inorder_recursive(root, result)
        assert [1, 2, 3, 4, 5, 6, 7] == result

    def testInOrderIterative(self):
        root = BSTNode(4)
        root.insert(2)
        root.insert(3)
        root.insert(1)
        root.insert(6)
        root.insert(5)
        root.insert(7)

        result = []
        trees.traversal.inorder_iterative(root, result)
        assert [1, 2, 3, 4, 5, 6, 7] == result

    def testPostOrderRecursiveSingleNode(self):
        root = BSTNode(4)

        result = []
        trees.traversal.postorder_recursive(root, result)
        assert [4] == result

    def testPostOrderRecursive(self):
        root = BSTNode(4)
        root.insert(2)
        root.insert(3)
        root.insert(1)
        root.insert(6)
        root.insert(5)
        root.insert(7)

        result = []
        trees.traversal.postorder_recursive(root, result)
        assert [1, 3, 2, 5, 7, 6, 4] == result

    def testPostOrderIterative(self):
        root = BSTNode(4)
        root.insert(2)
        root.insert(3)
        root.insert(1)
        root.insert(6)
        root.insert(5)
        root.insert(7)

        result = []
        trees.traversal.postorder_iterative(root, result)
        assert [1, 3, 2, 5, 7, 6, 4] == result

if __name__ == '__main__':
    unittest.main()
