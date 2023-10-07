import scrapy

import json


class BaidufanyiSpider(scrapy.Spider):
    name = "baidufanyi"
    allowed_domains = ["fanyi.baidu.com"]

    # post请求 没有参数则请求无意义，parse方法也无意义
    # start_urls = ["https://fanyi.baidu.com/sug"]
    #
    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': 'final'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text

        obj = json.loads(content)
        print(obj)
