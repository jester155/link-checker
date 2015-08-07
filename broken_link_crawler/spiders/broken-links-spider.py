__author__ = 'Mark'

from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from broken_link_crawler.items import BrokenItem
import broken_link_crawler.crawler_config as config


class BrokenSpider(CrawlSpider) :
    name = config.name
    allowed_domains = config.allowed_domains
    start_urls = config.start_urls
    handle_httpstatus_list = [400 , 404 , 500 , 503]
    rules = (Rule(SgmlLinkExtractor() , callback='parse_items' , follow=True) ,)

    def parse_items(self , response) :
        if response.status != 200 and response.status != 301 :
            item = BrokenItem()
            item['url'] = response.url
            item['referer'] = response.request.headers.get('Referer')
            item['status'] = response.status

            yield item