import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from crawlSpider.items import CrawlspiderItem


class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1107_1.html"]

    rules = (
        Rule(
            LinkExtractor(allow=r"/book/1107_(\d+)\.html"),  # 允许的url
            callback="parse_item",
            follow=False  # 表示是否跟随访问,即访问到第二页后还有满足的URL继续访问
        ),
    )

    def parse_item(self, response):

        img_list = response.xpath('//div[@class="bookslist"]//img')
        for img in img_list:
            src = img.xpath('./@data-original').extract_first()
            name = img.xpath('./@alt').extract_first()

            book = CrawlspiderItem(src=src, name=name)
            yield book

        # item = {}
        # # item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # # item["name"] = response.xpath('//div[@id="name"]').get()
        # # item["description"] = response.xpath('//div[@id="description"]').get()
        # return item
