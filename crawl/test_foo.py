# -*- conding:utf8 -*-
import os
import re
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class SimpleTest(unittest.TestCase):
    def setUp(self):
        baseurl = 'http://yahoo.co.jp'
        self.wait = 10 # seconds
        self.url = baseurl
        self.driver = webdriver.Chrome('../lib/chromedriver')

    def tearDown(self):
        self.driver.quit()


    def test_login_out(self):
        email   = "sudo_0826"
        passwd  = "wilkinson"
        login.login(self.driver, self.url, email, passwd)
        time.sleep(5)

        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find_all('title')
        self.assertEqual(login.check_logged_in(soup, 'h3', 'sudo_0826'), 1)
        time.sleep(1)

        list = soup.find_all( re.compile('script') )
        f = open('workfile', 'w')
        for i in list:
            f.write( str(i) )

        f.close()

        login.logout(self.driver)
        self.assertEqual(login.divide(2,2),1)
        time.sleep(1)



if __name__ == "__main__":
  unittest.main()

