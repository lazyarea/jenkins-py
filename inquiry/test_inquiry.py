# -*- conding:utf8 -*-
import os
import re
import time
import unittest
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class TestSimple(unittest.TestCase):

    def setUp(self):
        self.wait = 10 # seconds
        self.url = 'http://preview.tis.web-meister.jp/wmpreview/www.tis.jp/casestudy/'
        self.browser = webdriver.Chrome(os.getcwd() + '/lib/chromedriver')
        # self.browser.manage().timeouts().implicitlyWait(self.wait, TimeUnit.SECONDS);
        pass

    def tearDown(self):
        self.browser.quit()
        pass

    def test1(self):
        self.browser.implicitly_wait( self.wait ) # seconds
        self.browser.get( self.url )
        try:
            elem = self.browser.find_element_by_id("selKey1")
            print ("OK, page loaded")
        except:
            print("timeout")

        html = self.browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        kwd = []
        gyo = []
        kwd = soup.find_all('label', attrs={"for": re.compile("^selKey") })
        for i in kwd :
           print(i)

        self.assertEqual(1,1)

if __name__ == "__main__":
    unittest.main()

