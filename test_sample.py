import unittest

from calc import add, subtract
from greet import greet, farewell


class SampleTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_greet(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_farewell(self):
        self.assertEqual(farewell("Ada"), "Goodbye, Ada!")


if __name__ == "__main__":
    unittest.main()
