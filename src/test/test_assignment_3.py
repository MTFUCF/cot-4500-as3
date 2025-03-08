import unittest
from src.main.assignment_3 import euler_method, runge_kutta_4, f

class TestNumericalMethods(unittest.TestCase):

    def test_euler_method(self):
        result = euler_method(f, 0, 1, 2, 10)
        expected = 1.2446380979332121
        self.assertAlmostEqual(result, expected, places=5)

    def test_runge_kutta_4(self):
        result = runge_kutta_4(f, 0, 1, 2, 10)
        expected = 1.251316587879806
        self.assertAlmostEqual(result, expected, places=5)

if __name__ == "__main__":
    unittest.main()
