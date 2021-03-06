# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import Selector
from ronmofang.items import RonmofangItem
import os
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import urlparse
import ronmofang.settings as setting
from scrapy import log
from scrapy.selector import HtmlXPathSelector
from treelib import Node, Tree
# the tool to create a tree. This tool is handy I think.
#  http://xiaming.me/treelib/examples.html#api-examples. install pip treelib
from scrapy.signalmanager import SignalManager
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import scrapy.exceptions
import json
class ronmofangSpider(CrawlSpider):
    # name is how the spider is located and instantiated by Spider. Must be unique.
    name = 'ronmofang'
    # A list of strings contains domains that this spider is allowed to crawl.
    # Request for URLs not belonging to the declared domains are also allowed, unless OffsiteMiddleware is disenabled
    allowed_domains = [
        'ronmofang.com'
    ]
    start_urls = [
        'http://www.rongmofang.com/',
       # 'http://stackoverflow.com/questions/12394184/scrapy-call-a-function-when-a-spider-quits'
    ]

    # http responde error code, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
    handle_httpstatus_list = [404, 500]

    def __init__(self, *args, **kwargs):
        super(ronmofangSpider, self).__init__(*args, **kwargs)
        #register  signal listeners through dispatcher to deal with some tasks before close the spider if necessary
        # two tasks are registered: task before close the spider, and handle errors
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        dispatcher.connect(self.spider_error, signals.spider_error)

    # define the rules to crawl web pages
    # usage: class scrapy.contrib.spiders.Rule(link_extractor, callback=None, cb_kwargs=None, follow=None,
    # process_links=None, process_request=None)
    # Ref. link Extractors http://doc.scrapy.org/en/latest/topics/link-extractors.html#topics-link-extractors
    # rules = (
    #   Rule(LinkExtractor(), callback='parse_item'),
    #)
    # 1. One way to start the request is like this. It will start a POST request, and handled by the callback
    # def start_requests(self):
    # return [scrapy.FormRequest("url",formdata={'user':'','pass':'secret'},
    #                            callback=self.logged_in)]

    def logged_in(self, response):
        pass

    # 2, another simple way is to implement the  callback (default parse). It returns Item and/or Request
    # It is invoked each time a response arrives

    tree = Tree()
    tree.create_node(start_urls[0], start_urls[0])

    def parse(self, response):

        # handle the response
        if response.status in self.handle_httpstatus_list:
            self.log('Http request failed! ')
            return
        self.log('A response from %s just arrived!' % response.url)
        item = RonmofangItem()
        external_link = []
        internal_link = []
        #sel =  Selector(response)
        #item['name'] = sel.xpath('//html/body/div[1]/div[4]/div/div[1]/p[5]/strong/text()').extract()
        soup = BeautifulSoup(response.body)
        for script in soup(["script", "style"]):
            script.extract()  # rip JavaScript code and style in a web page
        ronmofangSpider.save2file(soup.get_text())
        item['url'] = response.url
        item['text'] = soup.get_text()

        #print(soup.get_text().encode("GBK", "ignore"))
        # result = soup.find("div", {"class":"border home_left"})
        # print result.text.encode("GBK", "ignore")

        # item['description'] = result.text.encode('utf-8')
        for tag in soup.findAll('a', href=True):
            obtained_url = urlparse.urljoin(response.url, tag['href'])
            if ronmofangSpider.external_links(obtained_url, self.start_urls[0]):
                external_link.append(obtained_url)
            else:
                internal_link.append(obtained_url)
                if self.grow_tree(obtained_url, response.url):
                    current_node = self.tree.get_node(obtained_url)
                    current_level = self.tree.depth(current_node)
                    if current_level < setting.DEPTH:
                        self.log('make request from %s at level %s. ' % (obtained_url, current_level))
                        try:
                            yield self.make_requests_from_url(obtained_url).replace(callback=self.parse)
                        except Exception:
                            print "Something wrong with making a request !"
                            pass
                    else:
                        self.log('Stop growing the tree and sending requests at this node !')

        item['url_external'] = ronmofangSpider.remove_duplicate(external_link)
        item['url_internal'] = ronmofangSpider.remove_duplicate(internal_link)

        #or, use the following line to solve the encoding problem
        # http://www.crifan.com/unicodeencodeerror_gbk_codec_can_not_encode_character_in_position_illegal_multibyte_sequence/
        # print result.text.encode("GB18030")
        # yield new request and define the callback function
        # yield self.make_requests_from_url(url).replace(callback=self.parse_content)
        yield item

    def spider_closed(self, spider):
    # do the work that before the spider closed.
        self.log('If needed, do some works here before the spider is closed. ')
        #self.tree.save2file('E:\PythonProject\ronmofang\tree')
        data = self.tree.to_json()
        with open("tree.txt", "w+") as f:
            json.dump(data, f)

    def spider_error(self, spider):
    # handle http request error
        self.log('If needed, do some works to handle errors here. ')


    def grow_tree(self, url, parent_url):
        if self.tree.get_node(url) is None:
            self.tree.create_node(url, url, parent=parent_url)
            self.log('Add node  %s to the parent %s. ' % (self.tree.get_node(url).tag, self.tree.parent(url).tag))
            return True
        else:
            return False


    @staticmethod
    # Ref. http://stackoverflow.com/questions/22799990/beatifulsoup4-get-text-still-has-javascript
    # do the basic clean-up for the context
    def save2file(result):
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in result.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        with open("foo.txt", "a+") as f:
            f.write(text.encode('utf-8'))
            f.close()


    @staticmethod
    def external_links(link, url):
        external = True
        # ignore the URLs schema, e.g. http and https are the same domain
        if urlparse.urlparse(link).netloc == urlparse.urlparse(url).netloc:
            external = False
        return external

    @staticmethod
    def remove_duplicate(links):
        return list(set(links))

    @staticmethod
    def resolve_links(links):
        root = ronmofangSpider.guess_root(links)
        for link in links:
            if not link.startswith('http' or 'https'):
                link = urlparse.urljoin(root, link)
                yield link
    @staticmethod
    def guess_root(links):
        for link in links:
            if link.startswith('http' or 'https'):
                parsed_link = urlparse.urlparse(link)
                scheme = parsed_link.scheme + '://'
                netloc = parsed_link.netloc
            return scheme + netloc

