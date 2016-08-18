# -*- conding:utf8 -*-
import os
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
        self.wait = 10
        self.url = 'http://preview.tis.web-meister.jp/wmpreview/www.tis.jp/casestudy/'
        self.browser = webdriver.Chrome(os.getcwd() + '/lib/chromedriver')
        # self.browser.manage().timeouts().implicitlyWait(self.wait, TimeUnit.SECONDS);
        pass

    def tearDown(self):
        self.browser.quit()
        pass

    def test1(self):
        try:
            #self.browser.get( self.url )
            #element = WebDriverWait(driver, 10).until(
            element = WebDriverWait( self.browser, 10).until(
                 EC.presence_of_element_located((By.ID, "js_k_words")))
        finally:
            self.browser.quit()

        print( [driver.find_element_by_name("q")] )
        #html = elem.page_source
        #bs_src = bs4(html)

        # print(html)
        self.assertEqual(1,1)

if __name__ == "__main__":
    unittest.main()

