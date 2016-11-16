import unittest
from selenium import webdriver

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_authorithation(self):
        # navigate to the application login page
        driver = self.driver
        driver.get("http://13.92.28.188:8090/secure/Dashboard.jspa")

        # check that login page was opened


    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()
