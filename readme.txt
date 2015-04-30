Scrapy Tutorial http://doc.scrapy.org/en/latest/intro/overview.html

-  scrapy -h
   asking for help
-  scrapy startproject ronmofang
- scrapy crawl spiderName
    start a spider, this command can be followed with some other options,
     see shell command http://doc.scrapy.org/en/latest/topics/commands.html#custom-project-commands
     and it accepts extra parameters http://doc.scrapy.org/en/latest/topics/spiders.html
- Scrapyd http://scrapyd.readthedocs.org/en/latest/
  deploy scrapy in product

- start MongoDB
     execute mongod and specify the folder where data will dump into, e.g.
       C:\mongodb\bin\mongod.exe --dbpath d:\test\mongodb\data

- Reference
 https://github.com/monsterxx03/yeeyan-spider 抓译言网
 https://github.com/tpeng/googlesearch Scrape the google advanced search
 https://github.com/darthbear/scrapy-mongodb-pipeline  MongoDB and scrapy
  https://github.com/gnemoug/distribute_crawler
  https://github.com/clasense4/scrapy-blog-crawler  crawl URLs in a blog, and store it.
  https://github.com/Zozoz/crawler_images scrapy + redis + monodb
  https://github.com/hackrole/blog-scrapy  抓博客
  https://github.com/paulproteus/autoresponse  http auto-response
  https://github.com/johncadigan/scrapy-sci Improve scraping with machine learning based pipelines
  https://github.com/yoyzhou/weibo_scrapy    Weibo
  https://github.com/immzz/zhihu-scrapy  Zhihu
  https://github.com/nautilus28/linkedpy linkedin
  https://github.com/pengyuan/oscbot 爬取OSCHINA（开源中国社区）
  https://github.com/chenghao/TBSpiders 淘宝
  https://github.com/gnemoug/distribute_crawler  使用scrapy,redis, mongodb,graphite实现的一个分布式网络爬虫