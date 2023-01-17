import unittest
from lib import fun

class InequalityTest(unittest.TestCase):

    def testEqual(self):
        self.assertEqual(fun.add(3, 6), 9)

if __name__ == '__main__':
    unittest.main()
