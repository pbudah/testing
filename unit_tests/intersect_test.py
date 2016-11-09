import unittest
from sample_app.sample_app import *

class IntersectTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.a = [1,0,-1,8,"hello"]
        cls.b = [0,8,None]
        cls.result = [0,8]

    def test_inter1(self):
        res = intersect(self.a,self.b)
        self.assertEqual(self.result, res,'unexpected result')

    def test_inter2(self):
        self.assertNotIn(self.result, self.a, 'set is in result set')
        self.assertNotIn(self.result, self.b, 'set is in result set')

    def test_inter3(self):
        res1 = intersect(self.a, [])
        res2 = intersect([],[])
        res3 = intersect([],self.b)
        self.assertEqual([], res1, 'incorrect intersection with an empty list')
        self.assertEqual([], res2, 'incorrect intersection of two empty lists')
        self.assertEqual([], res3, 'incorrect intersection with an empty list')

    def tearDown(self):
        print 'tearDown is executed after each test method'

if __name__ == '__main__':
    unittest.main()
