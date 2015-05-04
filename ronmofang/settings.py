# -*- coding: utf-8 -*-

# Scrapy settings for ronmofang project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ronmofang'

SPIDER_MODULES = ['ronmofang.spiders']
NEWSPIDER_MODULE = 'ronmofang.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ronmofang (+http://www.yourdomain.com)'
# To activate an item pipeline. It is allowed to have many pipelines
ITEM_PIPELINES = {
   # 'ronmofang.pipelines.RonmofangPipeline': 20,
   # 'ronmofang.pipelines.RonmofangPipelineAlternative': 21,
    #   'ronmofang.pipelines.FilterWordsPipeline': 22
     }

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "ronmofangDB"
MONGODB_COLLECTION = "ronmofangCollection"

# download delay
DOWNLOAD_DELAY = 5