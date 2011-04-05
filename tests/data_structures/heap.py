import unittest
import random

from data_structures.heap import Heap
from data_structures.heap import heapsort

class HeapTest(unittest.TestCase):
    def testExtractMax(self):
        # Single element
        heap = Heap([1])

        assert heap.extract_max() == 1

        # Sorted, n = 2
        heap = Heap([1, 2])

        for i in [2, 1]:
            assert heap.extract_max() == i

        # Reversed, n = 2
        heap = Heap([2, 1])

        for i in [2, 1]:
            assert heap.extract_max() == i

        # Sorted, n = 3
        heap = Heap([1, 2, 3])

        for i in [3, 2, 1]:
            assert heap.extract_max() == i

        # Reversed, n = 3
        heap = Heap([3, 2, 1])

        for i in [3, 2, 1]:
            assert heap.extract_max() == i

        # Intercalated, n = 5
        heap = Heap([1, 5, 2, 3, 4])

        for i in [5, 4, 3, 2, 1]:
            assert heap.extract_max() == i

    def testHeapsort(self):
        # Single element
        sorted_data = heapsort([1])
        assert __is_sorted__(sorted_data), "The data is not sorted!"
        
        # 500 elements, increasing order
        sorted_data = heapsort(range(500))
        assert __is_sorted__(sorted_data), "The data is not sorted!"

        # 500 elements, decreasing order
        sorted_data = heapsort(range(500, 0, -1))
        assert __is_sorted__(sorted_data), "The data is not sorted!"

        # 256 random elements
        sorted_data = heapsort([random.randint(0, 1024) for i in range(256)])
        assert __is_sorted__(sorted_data), "The data is not sorted!"

# TODO: This should be moved to a test utilities module
def __is_sorted__(data):
    for i in range(1, len(data)):
        if data[i] < data[i-1]:
            return False

    return True

if __name__ == '__main__':
    unittest.main()
