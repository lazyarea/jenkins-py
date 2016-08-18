from selenium import webdriver
from bs4 import BeautifulSoup

class Crawler(object):

    def main(self, url):
        if url is not None:
            try:
                browser = webdriver.Chrome('/home/lazyarea/lib/chromedriver')
                browser.get(url)
            except:
                browser.quit()

        html_source = browser.page_source
        bs_obj = BeautifulSoup(html_source)

        print(url)
        print(html_source)
        print(bs_obj)
        browser.quit()
