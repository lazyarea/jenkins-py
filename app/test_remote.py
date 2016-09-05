import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
#        self.driver = webdriver.Firefox()
#        driver = webdriver.Remote(
#           command_executor='http://127.0.0.1:4444/wd/hub',
#           desired_capabilities=DesiredCapabilities.CHROME)

#        driver = webdriver.Remote(
#            command_executor='http://127.0.0.1:4444/wd/hub',
#            desired_capabilities=DesiredCapabilities.OPERA)

#        driver = webdriver.Remote(
#            command_executor='http://127.0.0.1:4444/wd/hub',
#           desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)

        self.driver = webdriver.Remote(
            command_executor='http://192.168.100.103:4444/wd/hub',
           desired_capabilities=DesiredCapabilities.FIREFOX)



    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

