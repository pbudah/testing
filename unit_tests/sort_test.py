import unittest
from sample_app.sample_app import *


class SortTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'setUpClass is executed once only, before all other methods'

    def setUp(self):
        print 'setUp is executed before each test method'

    def test_sort1(self):
        pass  # implement

    def test_sort2(self):
        pass  # implement

    def test_sort3(self):
        pass  # implement

    def tearDown(self):
        print 'tearDown is executed after each test method'

    @classmethod
    def tearDownClass(cls):
        print 'tearDownClass is executed once only, after all other methods'


