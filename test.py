import numpy as np
import hello
import unittest

class TestMethods(unittest.TestCase):
    def test_add(self):
        a = np.array([1, 2, 3])
        self.assertEqual(a[0], 1)

if __name__ == '__main__':
    unittest.main()
