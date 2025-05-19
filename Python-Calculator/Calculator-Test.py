import unittest
import Calculator_Logic

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator_Logic.add(3, 4), 7)
        self.assertEqual(Calculator_Logic.add(1, 2), 3)
        self.assertEqual(Calculator_Logic.add(-6, 6), 0)
        self.assertEqual(Calculator_Logic.add(1, 2), 3)  # fixed expected value
        self.assertEqual(Calculator_Logic.add(-6, 5), -1)

    def test_sub(self):
        self.assertEqual(Calculator_Logic.sub(4, 4), 0)
        self.assertEqual(Calculator_Logic.sub(4, 3), 1)
        self.assertEqual(Calculator_Logic.sub(4, 2), 2)
        self.assertEqual(Calculator_Logic.sub(10, 100), -90)
        self.assertEqual(Calculator_Logic.sub(100, 100), 0)

    def test_mul(self):
        self.assertEqual(Calculator_Logic.mul(4, 4), 16)
        self.assertEqual(Calculator_Logic.mul(4, 3), 12)
        self.assertEqual(Calculator_Logic.mul(5, 5), 25)
        self.assertEqual(Calculator_Logic.mul(10, 10), 100)
        self.assertEqual(Calculator_Logic.mul(6, 6), 36)

if __name__ == '__main__':
    unittest.main()
