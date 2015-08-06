__author__ = 'Mark'

import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.item import Item , Field
from fpu_crawler.items import BrokenItem


class BrokenSpider(scrapy.Spider) :
    name = 'fpu'
    allowed_domains = ['floridapolytechnic.org']
    start_urls = ['https://floridapolytechnic.org']
    handle_httpstatus_list = [404]
    rules = (Rule(SgmlLinkExtractor() , callback='parse_item' , follow=True) ,)

    def parse_item(self , response) :
        if response.status == 404:
            item = BrokenItem()
            item['url'] = response.url
            item['referer'] = response.request.headers.get('Referer')
            item['status'] = response.status

            return item
