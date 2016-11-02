import unittest
from sample_app.sample_app import *

class IntersectTest(unittest.TestCase):

    def setUp(self):
        self.a = [1,0,-1,8,"hello"]
        self.b = [0,8,None]
        self.result = [0,8]

    def test_inter1(self):
        self.assertEqual(self.result, intersect(self.a, self.b))

    def test_inter2(self):
        self.assertNotIn(self.result, self.a)
        self.assertNotIn(self.result, self.b)

    def test_inter3(self):
        self.assertEqual([], intersect(self.a, []))
        self.assertEqual([], intersect([],[]))
        self.assertEqual([], intersect([],self.b))

    def tearDown(self):
        print 'tearDown is executed after each test method'

if __name__ == '__main__':
    unittest.main()
