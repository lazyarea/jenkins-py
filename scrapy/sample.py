# -*- coding: utf-8 -*-

import scrapy


class QiitaSpider(scrapy.Spider):
    name = 'qiita_spider'

    # Gh|CgiN[OðJn·éURLðLÚ·éj
    start_urls = ['http://qiita.com/advent-calendar/2015/categories/programming_languages']

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
    }

    # URLÌoðLÚ
    def parse(self, response):
        for href in response.css('.adventCalendarList .adventCalendarList_calendarTitle > a::attr(href)'):
            full_url = response.urljoin(href.extract())

            # oµ½URLð³ÉRequestðì¬µA_E[h·é
            yield scrapy.Request(full_url, callback=self.parse_item)

    # _E[hµ½y[Wð³ÉAàeðoµÛ¶·éItemðì¬
    def parse_item(self, response):

        urls = []
        for href in response.css('.adventCalendarItem_entry > a::attr(href)'):
            full_url = response.urljoin(href.extract())
            urls.append(full_url)

        yield {
            'title': response.css('h1::text').extract(),
            'urls': urls,
        }
