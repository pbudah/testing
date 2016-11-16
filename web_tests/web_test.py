import unittest
from selenium import webdriver

class AuthorithationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get("http://13.92.28.188:8090/secure/Dashboard.jspa")


    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()
