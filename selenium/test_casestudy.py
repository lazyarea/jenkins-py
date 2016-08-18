# -*- conding:utf8 -*-
import os
import unittest
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class TestSimple(unittest.TestCase):

    def setUp(self):
        self.wait = 10
        self.url = 'http://preview.tis.web-meister.jp/wmpreview/www.tis.jp/casestudy/'
        self.browser = webdriver.Chrome(os.getcwd() + '/lib/chromedriver')
        pass

    def tearDown(self):
        self.browser.quit()
        pass

    def test1(self):
        self.browser.get( self.url )
        try:
            elem = WebDriverWait(self.browser, self.wait).until(
                    EC.presence_of_element_located((By.ID, "selKey1"))
                    )
        finally:
            self.browser.quit()


        self.assertEqual(1,1)

if __name__ == "__main__":
    unittest.main()

