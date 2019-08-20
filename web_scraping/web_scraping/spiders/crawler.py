from scrapy.http.request import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import WebScrapingItem


class ExampleSpider(CrawlSpider):
    name = 'my-crawler'
    allowed_domains = ["gov.np", "starternepal.com"]
    start_urls = [l.strip() for l in open('urls.txt').readlines()]

    rules = [
             Rule(LinkExtractor(allow=()), callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        print('Got response from %s .' % response.url)
        item = WebScrapingItem()
        item['start_url'] = response.request.url
        # paragraph = response.css('p::text').extract()
        item['h3'] = response.css('h3::text').extract()
        item['h2'] = response.css('h2::text').extract()
        item.save()
        # yield {
        #     'url': start_url,
        #     # 'paragraph': paragraph,
        #     'h3': h3,
        #     'h2': h2,
        # }
        yield item
