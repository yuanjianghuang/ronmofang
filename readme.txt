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

 Low scalability
 https://github.com/monsterxx03/yeeyan-spider 抓译言网 // note 它定位了所有资源的位置。
 good example but need to know the location of the resources. DOWNLOADER_MIDDLEWARES, change the user-agent
 https://github.com/chenghao/TBSpiders 淘宝
 https://github.com/pengyuan/oscbot 爬取OSCHINA（开源中国社区）

 https://github.com/gnemoug/distribute_crawler 使用scrapy,redis, mongodb,graphite实现的一个分布式网络爬虫(good)


  https://github.com/clasense4/scrapy-blog-crawler  crawl URLs in a blog, and store it. CAN BE VERY USEFUL.
  https://github.com/Zozoz/crawler_images scrapy + redis + monodb
  https://github.com/johncadigan/scrapy-sci Improve scraping with machine learning based pipelines
  https://github.com/yoyzhou/weibo_scrapy    Weibo
  https://github.com/immzz/zhihu-scrapy  Zhihu
  https://github.com/nautilus28/linkedpy linkedin


  https://github.com/darthbear/scrapy-mongodb-pipeline  MongoDB and scrapy // incomplete
  https://github.com/paulproteus/autoresponse  http auto-response no use

  TODO:
  - text clean up
  - obtain the target terms
  - segment text (Chinese)
  - word frequency, distribution of term frequencies.
  - word clouds
  - identify frequent items and associations

  Ref. Web Data Mining 2nd
  - opinion mining and sentiment analysis
  -

jieba 采用IF-IDF提取文档特征 （核心是寻找最能体现文档特征以及体现与其他文档的区分度的词汇。）
http://zh.wikipedia.org/wiki/TF-IDF
TFIDF算法是建立在这样一个假设之上的：对区别文档最有意义的词语应该是那些在文档中出现频率高(TF)，
而在整个文档集合的其他文档中出现频率少的词语 (IDF)，所以如果特征空间坐标系取TF词频作为测度，就可以体现同类文本的特点。