import scrapy

from scrapy_baidu_01.items import ScrapyBaidu01Item


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        print("----------------------------------")
