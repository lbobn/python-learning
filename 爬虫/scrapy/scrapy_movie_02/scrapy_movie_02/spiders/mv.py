import scrapy

from scrapy_movie_02.items import ScrapyMovie02Item


class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["www.dytt.to"]
    start_urls = ["https://www.dytt.to/html/gndy/dyzz/index.html"]

    def parse(self, response):
        # print("--------------------------------------------")
        a_list = response.xpath('//div[@class="co_content8"]//a[@class="ulink"]')
        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            # print('000000000000000000000000000000000000000000')
            # print(name)
            # print(href)
            # 第二页地址
            # https://www.dytt.to/html/gndy/dyzz/20221013/63055.html
            # href的
            # /html/gndy/dyzz/20221013/63055.html
            url = 'https://www.dytt.to' + str(href)

            # 对第二页链接访问
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})
        # pass

    def parse_second(self, response):
        src = response.xpath('//div[@class="co_content8"]//img/@src').extract_first()
        name = response.meta['name']
        movie = ScrapyMovie02Item(name=name, src=src)
        yield movie
        # print('11111111111111111111111111111111111111111111111111')
        # print(src)
        # pass
