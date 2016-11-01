import unittest
from sample_app.sample_app import *


class SortTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'setUpClass is executed once only, before all other methods'

    def setUp(self):
        print 'setUp is executed before each test method'
        self.li = [0, 3, 8, 1, 5,2,4]

    def test_sort1(self):
        self.assertEqual([0,1,2,3,4,5,8], sort(self.li))

    def test_sort2(self):
        pass  # implement

    def test_sort3(self):
        pass  # implement

    def tearDown(self):
        print 'tearDown is executed after each test method'

    @classmethod
    def tearDownClass(cls):
        print 'tearDownClass is executed once only, after all other methods'


if __name__ == '__main__':
    unittest.main()
