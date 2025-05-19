import unittest
import Calculator_Logic

def test_add(self):
    test_cases = [(1, 2, 3),(-1, 1, 0),(0, 0, 0), (100, 200, 300),(-5, -5, -10)]
    for a, b, expected in test_cases:
        with self.subTest(a=a, b=b, expected=expected):
            result = Calculator_Logic.add(a, b)
            self.assertEqual(result, expected, f"Expected {a} + {b} = {expected}, but got {result}")


def test_sub(self):
    test_cases = [(1, 2, -1),(5, 5, 0),(7, 2, 5), (100, 10, 90),(4, 2, 2)]
    for a, b, expected in test_cases:
        with self.subTest(a=a, b=b, expected=expected):
            result = Calculator_Logic.sub(a, b)
            self.assertEqual(result, expected, f"Expected {a} - {b} = {expected}, but got {result}")

def test_mul(self):
    test_cases = [(1, 2, 2), (5, 5, 25), (0, 0, 0), (100, 10, 1000), (2, 2, 4)]
    for a, b, expected in test_cases:
        with self.subTest(a=a, b=b, expected=expected):
            result = Calculator_Logic.mul(a, b)
            self.assertEqual(result, expected, f"Expected {a} * {b} = {expected}, but got {result}")

if __name__ == '__main__':
    unittest.main()
