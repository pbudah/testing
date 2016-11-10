import unittest, requests
#from sample_app.sample_app import *

class AddProjectTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'setUpClass is executed once only, before all other methods'

    def setUp(self):
        payload = {'name': 'Example', 'key': 'HEX'}
        auth = ('restadmin', 'restadmin')
        self.prst = requests.post('http://13.92.28.188:8090/rest/api/2/project',params=payload, auth=auth)

    def test_create(self):
        r = self.prst.status_code
        self.assertTrue(r == requests.codes.ok, 'request is not valid and the project could not be created')

    def tearDown(self):
        requests.delete('https://13.92.28.188:8090/rest/api/2/project/HEX', auth=('restadmin','restadmin'))

    @classmethod
    def tearDownClass(cls):
        print 'tearDownClass is executed once only, after all other methods'

if __name__ == '__main__':
    unittest.main()
