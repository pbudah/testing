import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USR = 'restadmin'
PWD = 'restadmin'

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
        loginButtonXpath = "//input[@value='Log In']"

        # check that login page was opened
        self.assertIn("System Dashboard - JIRA", driver.title, 'incorrect page or page was not opened')

        # filling login forms
        name = driver.find_element_by_id("login-form-username")
        name.clear()
        name.send_keys(USR)
        pwd = driver.find_element_by_id("login-form-password")
        pwd.clear()
        pwd.send_keys(PWD)
        loginButton = driver.find_element_by_xpath(loginButtonXpath)
        loginButton.click()




    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()
