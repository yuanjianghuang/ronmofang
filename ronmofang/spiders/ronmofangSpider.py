# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import Selector
from ronmofang.items import RonmofangItem
import os

class ronmofangSpider(CrawlSpider):
    # name is how the spider is located and instantiated by Spider. Must be unique.
    name = 'ronmofang'
    # A list of strings contains domains that this spider is allowed to crawl.
    # Request for URLs not belonging to the declared domains are also allowed, unless OffsiteMiddleware is disenabled
    allowed_domains = [
        'ronmofang.com'
    ]
    # Declare the start URLs
    start_urls = [
      #  'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
         'http://www.rongmofang.com/information/infodetails/202'
        ]

    # define the rules to crawl web pages
    # usage: class scrapy.contrib.spiders.Rule(link_extractor, callback=None, cb_kwargs=None, follow=None,
    # process_links=None, process_request=None)
    # Ref. link Extractors http://doc.scrapy.org/en/latest/topics/link-extractors.html#topics-link-extractors
    #rules = (
     #   Rule(LinkExtractor(), callback='parse_item'),
    #)
    # 1. One way to start the request is like this. It will start a POST request, and handled by the callback
   # def start_requests(self):
      # return [scrapy.FormRequest("url",formdata={'user':'','pass':'secret'},
      #                            callback=self.logged_in)]

    def logged_in(self,response):
        pass

    # 2, another simple way is to implement the  callback (default parse). It returns Item and/or Request
    # It is invoked each time a response arrives

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        item = RonmofangItem()
        sel =  Selector(response)
        item['name'] = sel.xpath('//html/body/div[1]/div[6]/div/div/div[1]/p/text()').extract()

        with open("foo.txt", "w+") as f:
            f.write(item['name'][0].encode('utf-8'))
            f.close( )

        yield item
       # return item