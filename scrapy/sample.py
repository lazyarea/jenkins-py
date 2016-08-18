# -*- coding: utf-8 -*-

import scrapy


class QiitaSpider(scrapy.Spider):
    name = 'casestudy_spider'

    start_urls = ['http://preview.tis.web-meister.jp/wmpreview/www.tis.jp/casestudy/']

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
    }

    def parse(self, response):
        for href in response.css('.adventCalendarList .adventCalendarList_calendarTitle > a::attr(href)'):
            full_url = response.urljoin(href.extract())

            yield scrapy.Request(full_url, callback=self.parse_item)

    def parse_item(self, response):

        urls = []
        for href in response.css('.adventCalendarItem_entry > a::attr(href)'):
            full_url = response.urljoin(href.extract())
            urls.append(full_url)

        yield {
            'title': response.css('h1::text').extract(),
            'urls': urls,
        }
