# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RonmofangItem(scrapy.Item):
    '''
     Define items that we need
    '''
    url = scrapy.Field()
    text = scrapy.Field()
    url_internal = scrapy.Field()
    url_external = scrapy.Field()

