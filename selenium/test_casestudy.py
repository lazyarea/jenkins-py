# -*- conding:utf8 -*-

import unittest
import Crawler

class SimpleTest(unittest.TestCase):

    def test1(self):

        url = 'http://preview.tis.web-meister.jp/wmpreview/www.tis.jp/casestudy/?k=selKey2,selKey9'
        crawl = Crawler.Crawler()
        crawl.main(url)

        self.assertEqual(1,1)

if __name__ == "__main__":
    unittest.main()

