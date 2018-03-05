# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    theme = 'tecnologia'
    lang = ['es', 'mx']
    start_urls = [
        # 'https://blog.scrapinghub.com'
        'https://news.google.com/news/search/section/q/tecnologia/tecnologia?hl=es-419&gl=MX&ned=es_mx'
    ]
    def parse(self, response):
        for item in response.css('.qx0yFc'):
            yield{
                'title': item.css(".nuEeue.hzdq5d.ME7ew::text").extract(),
                'link': item.css(".nuEeue.hzdq5d.ME7ew::attr(href)").extract(),
                'images': item.css(".lmFAjc::attr(src)").extract(),
                'created_at': item.css(".d5kXP.YBZVLb::text").extract(),
                'created_by': item.css(".IH8C7b.Pc0Wt::text").extract()
            }