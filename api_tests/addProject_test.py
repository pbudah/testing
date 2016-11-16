import unittest, requests
#from sample_app.sample_app import *

class AddProjectTest(unittest.TestCase):

    def setUp(self):
        headers = {'Content-Type':'application/json'}
        data = {
            "fields": {
                "project": {
                    "key": "TEST"
                },
                "summary": "Not bad.",
                "description": "Creating new project"
            }
        }
        auth = ('restadmin', 'restadmin')
        self.prst = requests.post('http://13.92.28.188:8090/rest/api/2/project',data=data, auth=auth, headers=headers)

    def test_create(self):
        r = self.prst.status_code
        self.assertTrue(r == requests.codes.ok, 'request is not valid and the project could not be created')

    def tearDown(self):
        requests.delete('https://13.92.28.188:8090/rest/api/2/project/TEST', auth=('restadmin','restadmin'))


if __name__ == '__main__':
    unittest.main()
