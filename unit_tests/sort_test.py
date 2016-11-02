import unittest
from sample_app.sample_app import *


class SortTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'setUpClass is executed once only, before all other methods'

    def setUp(self):
        print 'setUp is executed before each test method'
        self.li = [0, 3, 8, 1, 5,2,4]
        self.li2 = [0,1,2,3,4,5,8]

    def test_sort1(self):                                # Check sort method with order of elements
        self.assertEqual([0,1,2,3,4,5,8], sort(self.li))

    def test_sort2(self):                                # Check sort method with already sorted list
        self.assertEqual(self.li2, sort(self.li2))

    def test_sort3(self):                                # Check that sort method is not None
        self.assertIsNotNone(sort(self.li))

    def test_sort4(self):                                # Check sort method with negative values
        self.li3 = [-6, 6, 0, -5, 8, -99]
        self.assertEqual([-99, -6, -5, 0, 6, 8], sort(self.li3))

    def tearDown(self):
        print 'tearDown is executed after each test method'

    @classmethod
    def tearDownClass(cls):
        print 'tearDownClass is executed once only, after all other methods'


if __name__ == '__main__':
    unittest.main()
