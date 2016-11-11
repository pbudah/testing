import unittest, requests

class AddIssueTest(unittest.TestCase):

    def setUp(self):
        headers = {'Content-Type':'application/json'}
        data = {
            "fields": {
                "project": {
                    "key": "MED"
                },
                "summary": "Not bad.",
                "description": "Creating new issue",
                "issuetype": {
                    "id": "35"
                }
            }
        }
        auth = ('restadmin', 'restadmin')
        self.prst = requests.post('http://13.92.28.188:8090/rest/api/2/issue',data=data, auth=auth, headers=headers)

    def test_create(self):
        #r = self.prst.status_code
        self.assertTrue(self.prst.status_code == requests.codes.ok, 'request is not valid and the issue could not be created')

    def tearDown(self):
        requests.delete('https://13.92.28.188:8090/rest/api/2/issue/MED-35', auth=('restadmin','restadmin'))


if __name__ == '__main__':
    unittest.main()
