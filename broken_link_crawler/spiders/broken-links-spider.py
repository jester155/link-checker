__author__ = 'Mark'

from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from broken_links_crawler.items import BrokenItem
import broken_links_crawler.crawler_config as config


class BrokenSpider(CrawlSpider) :
    name = 'fpu'
    allowed_domains = config.allowed_domains
    start_urls = config.start_urls
    handle_httpstatus_list = [404]
    rules = (Rule(SgmlLinkExtractor() , callback='parse_items' , follow=True) ,)

    def parse_items(self , response) :
        if response.status != 200 and response.status != 301 :
            item = BrokenItem()
            item['url'] = response.url
            item['referer'] = response.request.headers.get('Referer')
            item['status'] = response.status

            yield item