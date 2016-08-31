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
        baseurl = 'http://192.168.11.102:18002/?site_id=&status=&sort=9'
        self.wait = 10 # seconds
        self.url = baseurl
        self.driver = webdriver.Chrome('../lib/chromedriver')
        self.dir = './saved/'
        self.new_fle_ext = '.txt'

    def tearDown(self):
        self.driver.quit()


    def test_login_out(self):
        self.driver.get( self.url )
        self.driver.send_keys()

if __name__ == "__main__":
  unittest.main()

