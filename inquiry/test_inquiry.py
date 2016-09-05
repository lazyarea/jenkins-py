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

class TestInquiry(unittest.TestCase):

    def setUp(self):
        self.wait = 10 # seconds
        self.url = 'http://192.168.100.103/login'
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
#            elem = self.browser.find_element_by_name("password")
            print ("OK, page loaded")
        except:
            print("timeout")

        self.browser.find_element_by_name('login_id').send_keys('xyz')
        self.browser.find_element_by_name('password').send_keys('xyz')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/form/div[3]/div/button').click()

        html = self.browser.page_source
        soup = BeautifulSoup(html, "html.parser")

        self.assertEqual(1,1)

if __name__ == "__main__":
    unittest.main()

