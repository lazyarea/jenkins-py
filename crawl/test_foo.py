# -*- conding:utf8 -*-
import os
import re
import unittest
import utils
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
        self.dir = './saved/'
        self.new_fle_ext = '.txt'

    def tearDown(self):
        self.driver.quit()


    def test_login_out(self):
        csv = utils.load_csv('url.csv')
        for url in csv:
            u = url.split('//')

            self.driver.get( url )

            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            title = soup.find_all('title')
            time.sleep(1)

            list = soup.find_all( re.compile('script') )

            new_file = self.dir + re.sub(r'/', '_', u[1]) + self.new_fle_ext
            f = open(new_file, 'w')
            for i in list:
                f.write( str(i) )
            f.close()

            self.assertEqual(1,1)
            time.sleep(1)



if __name__ == "__main__":
  unittest.main()

