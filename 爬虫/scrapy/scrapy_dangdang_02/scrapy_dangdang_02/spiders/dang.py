import scrapy

from scrapy_dangdang_02.items import ScrapyDangdang02Item


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.01.01.00.00.00.html"]

    base_url = 'https://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        li_list = response.xpath('//ul[@id="component_59"]/li')
        # //ul[@id="component_59"]/li/a/img/@data-original
        # //ul[@id="component_59"]/li/p[@class="price"]/span[1]
        for li in li_list:
            # 存在懒加载，滑到指定位置src才会变为真的
            src = li.xpath('./a/img/@data-original').extract_first()
            if not src:
                src = li.xpath('./a/img/@src').extract_first()
            name = li.xpath('./a/img/@alt').extract_first()
            price = li.xpath('./p[@class="price"]/span[1]/text()').extract_first()
            # print(src, name, price)
            # pass
            book = ScrapyDangdang02Item(src=src, name=name, price=price)
            yield book
        if self.page < 20:
            self.page += 1
            url = self.base_url + str(self.page) + '-cp01.01.01.00.00.00.html'

            yield scrapy.Request(url=url, callback=self.parse)
