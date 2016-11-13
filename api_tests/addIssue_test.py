import unittest, requests

ADDED = 201

class AddIssueTest(unittest.TestCase):

    def setUp(self):
        headers = {'Content-Type':'application/json'}
        payload = "{\r\n            \"fields\": {\r\n                \"project\": {\r\n                    \"key\": \"MED\"\r\n                },\r\n                \"summary\": \"Not bad.\",\r\n                \"description\": \"Creating new issue\",\r\n                \"issuetype\": {\r\n                    \"name\": \"Bug\"\r\n                }\r\n            }\r\n        }\r\n        "
        auth = ('restadmin', 'restadmin')
        self.prst = requests.post('http://13.92.28.188:8090/rest/api/2/issue',data=payload, auth=auth, headers=headers)
        p_json = self.prst.json()
        self.k = p_json['key']

    def test_create(self):
        r = self.prst.status_code
        self.assertEqual(r, ADDED, 'request is not valid and the issue could not be created')

        #print self.p_json['key']

    def tearDown(self):
        requests.delete('http://13.92.28.188:8090/rest/api/2/issue/'+ self.k, auth=('restadmin','restadmin'))


if __name__ == '__main__':
    unittest.main()
