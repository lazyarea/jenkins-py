# -*- conding:utf8 -*-

import unittest
import Crawler

class SimpleTest(unittest.TestCase):

    def test1(self):

        url = 'http://someurl'
        crawl = Crawler.Crawler()
        crawl.main(url)

        self.assertEqual(1,1)

if __name__ == "__main__":
    unittest.main()

