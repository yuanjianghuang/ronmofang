# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
import sys


class RonmofangPipeline(object):

    '''
        http://api.mongodb.org/python/current/tutorial.html
        How to manage pymongo database
        To start a MongoDB, e.g.: mongod --dbpath "E:\Github\MongoDB\data"
    '''
    def __init__(self):
        try:
            connection = MongoClient(
                settings['MONGODB_SERVER'],
                settings['MONGODB_PORT']
            )
            db = connection[settings['MONGODB_DB']] # Getting a databse
            self.collection = db[settings['MONGODB_COLLECTION']]  # Getting a collection
        except ConnectionFailure, e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            # insert a collection, the primary key is auto-generated, with name _id (96bit)
            # safe property will make sure that it is synchronous writes (it works in most cases)
            self.collection.insert(dict(item))
            log.msg("added to MongoDB database!", safe = True,
                    level=log.DEBUG, spider=spider)
        return item
# define other pipeline to process data
class RonmofangPipelineAlternative(object):

    def process_item(self, item, spider):
        log.msg("Alternative pipeline!",
                    level=log.DEBUG, spider=spider)
        return item

# filter pipeline
class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in unicode(item['description']).lower():
                raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item