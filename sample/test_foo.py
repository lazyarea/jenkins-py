# -*- conding:utf8 -*-
import login
import os
import unittest
import utils
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://yahoo.co.jp'
        caps = DesiredCapabilities.FIREFOX.copy()
        caps["marionette"] = True

        hub = "http://192.168.56.102:4444/wd/hub/"
#        self.driver = webdriver.Remote(command_executor=hub, desired_capabilities=caps)
        self.driver =driver = webdriver.Remote(
              command_executor='http://192.168.56.102:4444/wd/hub',
              desired_capabilities=DesiredCapabilities.FIREFOX)


    def tearDown(self):
        self.driver.quit()


    def test_login_out(self):
        driver = self.driver
        driver.get(self.url)

if __name__ == "__main__":
  unittest.main()

