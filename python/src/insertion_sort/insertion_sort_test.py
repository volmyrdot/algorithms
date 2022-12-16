import numpy as np
import unittest

from python.src.insertion_sort.insertion_sort import insertion_sort


class Tests(unittest.TestCase):
    # Repeating terms.
    def test_repeating_terms(self):
        self.assertEqual([1, 1, 3, 5, 11, 51], insertion_sort([11, 1, 51, 1, 5, 3]))

    # Empty list should return empty list.
    def test_empty_list(self):
        self.assertEqual([], insertion_sort([]))

    # Negative number.
    def test_negative_number(self):
        self.assertEqual([-5, 1, 1, 6], insertion_sort([1, 1, -5, 6]))

    # Float and int, testing numpy array.
    def test_float_int(self):
        self.assertEqual([-20, -4, 11, 13.5, 15, 20], insertion_sort([11, -4, 20, 15, 13.5, -20]))

    # Already sorted array.
    def test_already_sorted(self):
        a = np.array(range(50))
        b = np.copy(a)

        self.assertEqual(b.tolist(), insertion_sort(a.tolist()))

    # Array in reversed sorted order.
    def test_reversed_sorted(self):
        a = np.arange(50, 0, -5)
        b = np.sort(np.copy(a))

        self.assertEqual(b.tolist(), insertion_sort(a.tolist()))

    # Large array.
    def test_large_array(self):
        a = np.random.randint(-5000, 5000, size=1000)
        b = np.sort(np.copy(a))

        self.assertEqual(b.tolist(), insertion_sort(a.tolist()))


if __name__ == '__main__':
    unittest.main()
